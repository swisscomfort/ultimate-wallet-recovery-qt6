#!/usr/bin/env python3
"""
Ultimate Wallet Recovery Tool - Scanner Widget
Hauptfunktionalität: Seed/Key Input und Multi-Blockchain Scanning
"""

import asyncio
from typing import List, Dict, Any, Optional
from pathlib import Path

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QTextEdit, QPushButton, QProgressBar, QCheckBox,
    QComboBox, QTableWidget, QTableWidgetItem, QHeaderView,
    QGroupBox, QTabWidget, QLineEdit, QSpinBox, QMessageBox,
    QFrame, QSplitter
)
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QFont, QPalette, QColor

# Import Core Logic
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from core.blockchain.networks import NETWORKS, get_enabled_networks
from core.blockchain.derivation import DERIVATION_PATHS
from core.blockchain.handler import BlockchainHandler
from core.ai.recovery_engine import AIRecoveryEngine
from core.translations import t


class ScanThread(QThread):
    """Background-Thread für Blockchain-Scanning"""
    
    progress_updated = pyqtSignal(int)
    result_found = pyqtSignal(dict)
    scan_completed = pyqtSignal(dict)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, scan_config: Dict[str, Any]):
        super().__init__()
        self.scan_config = scan_config
        self.is_cancelled = False
    
    def run(self):
        """Führt den Scan im Hintergrund aus"""
        try:
            asyncio.run(self._async_scan())
        except Exception as e:
            self.error_occurred.emit(str(e))
    
    async def _async_scan(self):
        """Async Scan-Logik"""
        scan_type = self.scan_config.get('scan_type', 'blockchain_scan')
        results = {"total_found": 0, "networks_scanned": 0, "addresses": [], "files_scanned": 0}
        
        if scan_type == 'file_scan':
            # File Scanning
            files = self.scan_config.get('scan_files', [])
            total_files = len(files)
            
            for i, file_path in enumerate(files):
                if self.is_cancelled:
                    break
                
                progress = int((i + 1) / total_files * 100)
                self.progress_updated.emit(progress)
                
                # Simuliere File-Analyse
                file_result = self._scan_file(file_path)
                if file_result:
                    self.result_found.emit(file_result)
                    results["addresses"].append(file_result)
                    results["total_found"] += 1
                
                results["files_scanned"] += 1
                await asyncio.sleep(0.3)  # Simuliere Scan-Zeit
        
        else:
            # Blockchain Scanning (wie vorher)
            networks = self.scan_config.get('networks', [])
            total_networks = len(networks)
            
            for i, network in enumerate(networks):
                if self.is_cancelled:
                    break
                    
                # Simuliere Scanning pro Netzwerk
                progress = int((i + 1) / total_networks * 100)
                self.progress_updated.emit(progress)
                
                # Simuliere gefundene Adresse (Placeholder)
                if i < 3:  # Simuliere ein paar Funde
                    result = {
                        "type": "blockchain",
                        "network": network,
                        "address": f"0x{''.join(['a'] * 40)}",
                        "balance": f"{0.001 * (i+1):.6f}",
                        "transactions": i + 1
                    }
                    self.result_found.emit(result)
                    results["addresses"].append(result)
                    results["total_found"] += 1
                
                results["networks_scanned"] += 1
                await asyncio.sleep(0.5)  # Simuliere Netzwerk-Latenz
        
        self.scan_completed.emit(results)
    
    def _scan_file(self, file_path):
        """Scannt eine einzelne Datei nach Wallet-Artefakten"""
        from pathlib import Path
        import re
        
        try:
            path = Path(file_path)
            
            # Grundlegende Datei-Info
            if path.is_file():
                # Lese Datei-Anfang für Pattern-Matching
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(1000)  # Erste 1000 Zeichen
                except:
                    with open(path, 'rb') as f:
                        content = f.read(1000).decode('utf-8', errors='ignore')
                
                # Suche nach Wallet-Mustern
                patterns = {
                    'seed_words': r'\b(?:abandon|ability|able|about|above|absent|absorb|abstract|absurd|abuse)\b',
                    'private_key': r'[0-9a-fA-F]{64}',
                    'address_eth': r'0x[a-fA-F0-9]{40}',
                    'address_btc': r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}'
                }
                
                found_patterns = []
                for pattern_name, pattern in patterns.items():
                    if re.search(pattern, content):
                        found_patterns.append(pattern_name)
                
                if found_patterns:
                    return {
                        "type": "file",
                        "network": "File System",
                        "address": str(path),
                        "balance": f"Patterns: {', '.join(found_patterns)}",
                        "transactions": len(found_patterns)
                    }
            
            elif path.is_dir():
                # Verzeichnis-Scan
                file_count = len(list(path.iterdir()))
                return {
                    "type": "directory",
                    "network": "File System", 
                    "address": str(path),
                    "balance": f"{file_count} Dateien",
                    "transactions": file_count
                }
        
        except Exception as e:
            # Fehler ignorieren und None zurückgeben
            pass
        
        return None
    
    def cancel(self):
        """Bricht den Scan ab"""
        self.is_cancelled = True


class WalletScannerWidget(QWidget):
    """
    Wallet Scanner Widget - Hauptfunktionalität der App
    
    Features:
    - Seed Phrase / Private Key Input
    - Netzwerk-Auswahl (12+ Blockchains)
    - Derivation Path Konfiguration  
    - Async Scanning mit Progress
    - Ergebnis-Tabelle mit Live-Updates
    - AI-Recovery Integration
    """
    
    scan_started = pyqtSignal()
    scan_completed = pyqtSignal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Core Components
        self.blockchain_handler = None
        self.ai_engine = AIRecoveryEngine()
        self.scan_thread = None
        
        # State
        self.is_scanning = False
        self.scan_results = []
        self.selected_scan_files = []  # Für File Scanner
        
        self.setup_ui()
        self.setup_connections()
        self.load_networks()
    
    def setup_ui(self):
        """Initialisiert die Benutzeroberfläche"""
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        # Header
        header = QLabel("🔍 Wallet Scanner")
        header_font = QFont()
        header_font.setPointSize(16)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)
        
        # Splitter für besseres Layout
        splitter = QSplitter(Qt.Orientation.Horizontal)
        main_layout.addWidget(splitter)
        
        # Linke Seite: Input & Konfiguration
        input_widget = self.create_input_panel()
        splitter.addWidget(input_widget)
        
        # Rechte Seite: Ergebnisse
        results_widget = self.create_results_panel()
        splitter.addWidget(results_widget)
        
        # Splitter-Verhältnis
        splitter.setSizes([400, 600])
        
        # Status & Control Panel
        control_panel = self.create_control_panel()
        main_layout.addWidget(control_panel)
    
    def create_input_panel(self) -> QWidget:
        """Erstellt das Input-Panel"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        # Input Tabs
        input_tabs = QTabWidget()
        layout.addWidget(input_tabs)
        
        # Tab 1: Seed Phrase
        seed_tab = QWidget()
        seed_layout = QVBoxLayout()
        seed_tab.setLayout(seed_layout)
        
        seed_layout.addWidget(QLabel("🌱 Seed Phrase:"))
        self.seed_input = QTextEdit()
        self.seed_input.setPlaceholderText("abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about")
        self.seed_input.setMaximumHeight(100)
        seed_layout.addWidget(self.seed_input)
        
        # Passphrase
        seed_layout.addWidget(QLabel("🔐 Passphrase (optional):"))
        self.passphrase_input = QLineEdit()
        self.passphrase_input.setEchoMode(QLineEdit.EchoMode.Password)
        seed_layout.addWidget(self.passphrase_input)
        
        # Sprache
        lang_layout = QHBoxLayout()
        lang_layout.addWidget(QLabel("🌐 Sprache:"))
        self.language_combo = QComboBox()
        self.language_combo.addItems(["english", "japanese", "french", "spanish", "italian"])
        lang_layout.addWidget(self.language_combo)
        lang_layout.addStretch()
        seed_layout.addLayout(lang_layout)
        
        input_tabs.addTab(seed_tab, "🌱 Seed")
        
        # Tab 2: Private Key
        privkey_tab = QWidget()
        privkey_layout = QVBoxLayout()
        privkey_tab.setLayout(privkey_layout)
        
        privkey_layout.addWidget(QLabel("🔑 Private Key:"))
        self.privkey_input = QTextEdit()
        self.privkey_input.setPlaceholderText("Fügen Sie Ihren Private Key hier ein...")
        self.privkey_input.setMaximumHeight(100)
        privkey_layout.addWidget(self.privkey_input)
        
        input_tabs.addTab(privkey_tab, "🔑 Private Key")
        
        # Tab 3: AI Recovery
        ai_tab = QWidget()
        ai_layout = QVBoxLayout()
        ai_tab.setLayout(ai_layout)
        
        ai_layout.addWidget(QLabel("🧠 Beschädigte Seed (? für fehlende Wörter):"))
        self.ai_input = QTextEdit()
        self.ai_input.setPlaceholderText("abandon ? abandon ? abandon abandon ? abandon abandon abandon abandon about")
        self.ai_input.setMaximumHeight(100)
        ai_layout.addWidget(self.ai_input)
        
        ai_recover_btn = QPushButton("🔧 KI Rekonstruieren")
        ai_recover_btn.clicked.connect(self.start_ai_recovery)
        ai_layout.addWidget(ai_recover_btn)
        
        input_tabs.addTab(ai_tab, "🧠 KI Recovery")
        
        # Tab 4: File Scanner
        file_tab = QWidget()
        file_layout = QVBoxLayout()
        file_tab.setLayout(file_layout)
        
        file_layout.addWidget(QLabel("📁 Dateien & Ordner scannen:"))
        
        file_button_layout = QHBoxLayout()
        
        self.select_files_btn = QPushButton("📁 Dateien auswählen")
        self.select_files_btn.clicked.connect(self.open_file_manager)
        file_button_layout.addWidget(self.select_files_btn)
        
        self.scan_home_btn = QPushButton("🏠 Home-Ordner scannen")
        self.scan_home_btn.clicked.connect(self.scan_home_directory)
        file_button_layout.addWidget(self.scan_home_btn)
        
        file_layout.addLayout(file_button_layout)
        
        self.selected_files_display = QTextEdit()
        self.selected_files_display.setMaximumHeight(80)
        self.selected_files_display.setPlaceholderText("Keine Dateien ausgewählt...")
        file_layout.addWidget(self.selected_files_display)
        
        input_tabs.addTab(file_tab, "📁 File Scanner")
        
        # Netzwerk-Auswahl
        network_group = self.create_network_selection()
        layout.addWidget(network_group)
        
        # Derivation-Konfiguration
        derivation_group = self.create_derivation_config()
        layout.addWidget(derivation_group)
        
        layout.addStretch()
        return widget
    
    def create_network_selection(self) -> QGroupBox:
        """Erstellt die Netzwerk-Auswahl"""
        group = QGroupBox("🌐 Blockchain-Netzwerke")
        layout = QGridLayout()
        group.setLayout(layout)
        
        self.network_checkboxes = {}
        row, col = 0, 0
        
        for network in NETWORKS:
            checkbox = QCheckBox(f"{network.symbol} - {network.name}")
            checkbox.setChecked(network.enabled)
            self.network_checkboxes[network.symbol] = checkbox
            
            layout.addWidget(checkbox, row, col)
            col += 1
            if col >= 2:  # 2 Spalten
                col = 0
                row += 1
        
        # Alle auswählen/abwählen
        button_layout = QHBoxLayout()
        select_all_btn = QPushButton("Alle auswählen")
        select_all_btn.clicked.connect(self.select_all_networks)
        select_none_btn = QPushButton("Keine auswählen")
        select_none_btn.clicked.connect(self.select_no_networks)
        
        button_layout.addWidget(select_all_btn)
        button_layout.addWidget(select_none_btn)
        layout.addLayout(button_layout, row + 1, 0, 1, 2)
        
        return group
    
    def create_derivation_config(self) -> QGroupBox:
        """Erstellt die Derivation-Konfiguration"""
        group = QGroupBox("⚙️ Derivation-Pfade")
        layout = QVBoxLayout()
        group.setLayout(layout)
        
        # Derivation Mode
        mode_layout = QHBoxLayout()
        mode_layout.addWidget(QLabel("Modus:"))
        self.derivation_combo = QComboBox()
        self.derivation_combo.addItems([
            "Standard (BIP44)",
            "Bitcoin Legacy (BIP44)",
            "Bitcoin SegWit (BIP49)", 
            "Bitcoin Native SegWit (BIP84)",
            "Bitcoin Taproot (BIP86)",
            "Erweitert (Custom)"
        ])
        mode_layout.addWidget(self.derivation_combo)
        layout.addLayout(mode_layout)
        
        # Anzahl Adressen
        addr_layout = QHBoxLayout()
        addr_layout.addWidget(QLabel("Adressen pro Netzwerk:"))
        self.address_count = QSpinBox()
        self.address_count.setRange(1, 100)
        self.address_count.setValue(5)
        addr_layout.addWidget(self.address_count)
        addr_layout.addStretch()
        layout.addLayout(addr_layout)
        
        return group
    
    def create_results_panel(self) -> QWidget:
        """Erstellt das Ergebnis-Panel"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        # Header
        header = QLabel("📊 Scan-Ergebnisse")
        header_font = QFont()
        header_font.setPointSize(12)
        header_font.setBold(True)
        header.setFont(header_font)
        layout.addWidget(header)
        
        # Ergebnis-Tabelle
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(5)
        self.results_table.setHorizontalHeaderLabels([
            "Netzwerk", "Adresse", "Balance", "Transaktionen", "Status"
        ])
        
        # Auto-resize Spalten
        header = self.results_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        
        layout.addWidget(self.results_table)
        
        # Statistiken
        stats_group = QGroupBox("📈 Statistiken")
        stats_layout = QGridLayout()
        stats_group.setLayout(stats_layout)
        
        self.stats_labels = {
            'scanned': QLabel("Gescannt: 0"),
            'found': QLabel("Gefunden: 0"),
            'total_balance': QLabel("Gesamt-Wert: 0.00 CHF"),
            'networks': QLabel("Netzwerke: 0/0")
        }
        
        row = 0
        for key, label in self.stats_labels.items():
            stats_layout.addWidget(label, row // 2, row % 2)
            row += 1
        
        layout.addWidget(stats_group)
        
        return widget
    
    def create_control_panel(self) -> QWidget:
        """Erstellt das Control-Panel"""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)
        
        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        self.scan_button = QPushButton("🚀 SCAN STARTEN")
        self.scan_button.setMinimumHeight(50)
        self.scan_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
            QPushButton:pressed {
                background-color: #1e8449;
            }
        """)
        self.scan_button.clicked.connect(self.start_scan)
        button_layout.addWidget(self.scan_button)
        
        self.stop_button = QPushButton("⏹️ Stopp")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_scan)
        button_layout.addWidget(self.stop_button)
        
        self.clear_button = QPushButton("🗑️ Löschen")
        self.clear_button.clicked.connect(self.clear_results)
        button_layout.addWidget(self.clear_button)
        
        self.export_button = QPushButton("💾 Exportieren")
        self.export_button.clicked.connect(self.export_results)
        button_layout.addWidget(self.export_button)
        
        layout.addLayout(button_layout)
        
        # Status Label
        self.status_label = QLabel("Bereit zum Scannen")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)
        
        return widget
    
    def setup_connections(self):
        """Richtet Signal-Verbindungen ein"""
        pass
    
    def load_networks(self):
        """Lädt verfügbare Netzwerke"""
        # Bereits in create_network_selection() implementiert
        pass
    
    def get_selected_networks(self) -> List[str]:
        """Gibt ausgewählte Netzwerke zurück"""
        selected = []
        for symbol, checkbox in self.network_checkboxes.items():
            if checkbox.isChecked():
                selected.append(symbol)
        return selected
    
    def select_all_networks(self):
        """Wählt alle Netzwerke aus"""
        for checkbox in self.network_checkboxes.values():
            checkbox.setChecked(True)
    
    def select_no_networks(self):
        """Wählt keine Netzwerke aus"""
        for checkbox in self.network_checkboxes.values():
            checkbox.setChecked(False)
    
    def start_scan(self):
        """Startet den Wallet-Scan"""
        if self.is_scanning:
            return
        
        # Bestimme Scan-Typ
        seed_text = self.seed_input.toPlainText().strip()
        privkey_text = self.privkey_input.toPlainText().strip()
        has_files = bool(self.selected_scan_files)
        
        # Validierung
        if not seed_text and not privkey_text and not has_files:
            QMessageBox.warning(
                self, "Warnung", 
                "Bitte geben Sie eine der folgenden Optionen ein:\n"
                "• Seed Phrase\n"
                "• Private Key\n"
                "• Dateien zum Scannen auswählen"
            )
            return
        
        # Netzwerk-Validierung nur bei Seed/PrivKey
        if (seed_text or privkey_text):
            selected_networks = self.get_selected_networks()
            if not selected_networks:
                QMessageBox.warning(self, "Warnung", "Bitte wählen Sie mindestens ein Netzwerk aus.")
                return
        
        # UI Update
        self.is_scanning = True
        self.scan_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        # Scan-Typ bestimmen
        if has_files:
            self.status_label.setText("🔍 File Scanning läuft...")
            scan_type = "file_scan"
            selected_networks = []  # Keine Netzwerke bei File Scan
        else:
            self.status_label.setText("🔍 Blockchain Scanning läuft...")
            scan_type = "blockchain_scan"
            selected_networks = self.get_selected_networks()
        
        # Scan-Konfiguration
        scan_config = {
            'scan_type': scan_type,
            'seed_phrase': seed_text,
            'private_key': privkey_text,
            'passphrase': self.passphrase_input.text(),
            'language': self.language_combo.currentText(),
            'networks': selected_networks,
            'derivation_mode': self.derivation_combo.currentText(),
            'address_count': self.address_count.value(),
            'scan_files': self.selected_scan_files
        }
        
        # Thread starten
        self.scan_thread = ScanThread(scan_config)
        self.scan_thread.progress_updated.connect(self.update_progress)
        self.scan_thread.result_found.connect(self.add_result)
        self.scan_thread.scan_completed.connect(self.scan_finished)
        self.scan_thread.error_occurred.connect(self.handle_error)
        self.scan_thread.start()
        
        self.scan_started.emit()
    
    def stop_scan(self):
        """Stoppt den aktuellen Scan"""
        if self.scan_thread and self.scan_thread.isRunning():
            self.scan_thread.cancel()
            self.scan_thread.wait()
        
        self.scan_finished({"cancelled": True})
    
    def update_progress(self, value: int):
        """Aktualisiert den Fortschrittsbalken"""
        self.progress_bar.setValue(value)
        self.status_label.setText(f"Scanning... {value}%")
    
    def add_result(self, result: Dict[str, Any]):
        """Fügt ein Scan-Ergebnis zur Tabelle hinzu"""
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        
        # Daten einfügen
        self.results_table.setItem(row, 0, QTableWidgetItem(result['network']))
        self.results_table.setItem(row, 1, QTableWidgetItem(result['address']))
        self.results_table.setItem(row, 2, QTableWidgetItem(f"{result['balance']} ETH"))
        self.results_table.setItem(row, 3, QTableWidgetItem(str(result['transactions'])))
        self.results_table.setItem(row, 4, QTableWidgetItem("✅ Aktiv"))
        
        # Statistiken aktualisieren
        self.update_statistics()
    
    def scan_finished(self, summary: Dict[str, Any]):
        """Wird aufgerufen wenn der Scan beendet ist"""
        self.is_scanning = False
        self.scan_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.progress_bar.setVisible(False)
        
        if summary.get('cancelled'):
            self.status_label.setText("Scan abgebrochen")
        else:
            total_found = summary.get('total_found', 0)
            networks_scanned = summary.get('networks_scanned', 0)
            self.status_label.setText(f"Scan beendet: {total_found} Ergebnisse in {networks_scanned} Netzwerken")
        
        self.scan_completed.emit(summary)
    
    def handle_error(self, error_message: str):
        """Behandelt Scan-Fehler"""
        self.scan_finished({"error": error_message})
        QMessageBox.critical(self, "Scan-Fehler", f"Ein Fehler ist aufgetreten:\n{error_message}")
    
    def update_statistics(self):
        """Aktualisiert die Statistik-Anzeige"""
        row_count = self.results_table.rowCount()
        selected_networks = len(self.get_selected_networks())
        
        self.stats_labels['scanned'].setText(f"Gescannt: {row_count}")
        self.stats_labels['found'].setText(f"Gefunden: {row_count}")
        self.stats_labels['networks'].setText(f"Netzwerke: {row_count}/{selected_networks}")
        
        # TODO: Echte Balance-Berechnung
        self.stats_labels['total_balance'].setText("Gesamt-Wert: 0.00 CHF")
    
    def clear_results(self):
        """Löscht alle Scan-Ergebnisse"""
        reply = QMessageBox.question(
            self, "Bestätigung", 
            "Möchten Sie alle Scan-Ergebnisse löschen?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.results_table.setRowCount(0)
            self.update_statistics()
            self.status_label.setText("Ergebnisse gelöscht")
    
    def export_results(self):
        """Exportiert die Scan-Ergebnisse"""
        QMessageBox.information(self, "Export", "CSV-Export wird implementiert...")
    
    def start_ai_recovery(self):
        """Startet die KI-basierte Seed-Wiederherstellung"""
        ai_input = self.ai_input.toPlainText().strip()
        if not ai_input:
            QMessageBox.warning(self, "Warnung", "Bitte geben Sie eine beschädigte Seed Phrase ein.")
            return
        
        # Einfache KI-Recovery Simulation
        words = ai_input.split()
        missing_count = words.count('?')
        
        if missing_count == 0:
            QMessageBox.information(self, "KI Recovery", "Keine fehlenden Wörter gefunden. Die Seed scheint vollständig zu sein.")
            return
        
        # Setze die "rekonstruierte" Seed in das normale Seed-Feld
        suggested_seed = ai_input.replace('?', 'abandon')  # Einfache Ersetzung
        self.seed_input.setPlainText(suggested_seed)
        
        QMessageBox.information(
            self, "KI Recovery", 
            f"KI-Rekonstruktion abgeschlossen!\n\n"
            f"Fehlende Wörter: {missing_count}\n"
            f"Vorschlag wurde in das Seed-Feld eingefügt.\n\n"
            f"⚠️ Hinweis: Dies ist eine Simulation. In der echten Version würde hier\n"
            f"ein fortgeschrittener Algorithmus verwendet werden."
        )
    
    def open_file_manager(self):
        """Öffnet den File Manager für die Dateiauswahl"""
        from .file_manager_dialog import FileManagerDialog
        
        dialog = FileManagerDialog(self)
        dialog.files_selected.connect(self.set_selected_files)
        dialog.exec()
    
    def set_selected_files(self, file_list):
        """Setzt die ausgewählten Dateien"""
        self.selected_scan_files = file_list
        self.update_file_display()
    
    def scan_home_directory(self):
        """Scannt das Home-Verzeichnis"""
        from pathlib import Path
        home_path = str(Path.home())
        self.selected_scan_files = [home_path]
        self.update_file_display()
        
        QMessageBox.information(
            self, "Home-Scan", 
            f"Home-Verzeichnis zum Scannen ausgewählt:\n{home_path}\n\n"
            f"Klicken Sie auf 'SCAN STARTEN' um zu beginnen."
        )
    
    def update_file_display(self):
        """Aktualisiert die Anzeige der ausgewählten Dateien"""
        if self.selected_scan_files:
            display_text = "\n".join([
                f"📄 {path}" if Path(path).is_file() else f"📁 {path}" 
                for path in self.selected_scan_files
            ])
        else:
            display_text = "Keine Dateien ausgewählt..."
        
        self.selected_files_display.setPlainText(display_text)


def main():
    """Test-Funktion für das Widget"""
    from PyQt6.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    
    widget = WalletScannerWidget()
    widget.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()