#!/usr/bin/env python3
"""
File Manager Dialog für Ultimate Wallet Recovery
Erlaubt das Durchsuchen und Auswählen von Dateien/Ordnern für Scanning
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTreeView, QFileSystemModel,
    QPushButton, QLabel, QLineEdit, QGroupBox, QCheckBox,
    QMessageBox, QProgressBar, QTextEdit
)
from PyQt6.QtCore import Qt, QDir, pyqtSignal, QThread
from PyQt6.QtGui import QFont
from pathlib import Path
import os


class FileManagerDialog(QDialog):
    """
    File Manager Dialog für das Auswählen von Scan-Zielen
    """
    
    files_selected = pyqtSignal(list)  # Liste von Dateipfaden
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.selected_files = []
        self.setup_ui()
        self.setup_file_tree()
    
    def setup_ui(self):
        """Initialisiert die UI"""
        self.setWindowTitle("📁 Datei-Manager - Scan-Ziele auswählen")
        self.setModal(True)
        self.resize(800, 600)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Header
        header = QLabel("📁 Wählen Sie Dateien oder Ordner zum Scannen")
        header_font = QFont()
        header_font.setPointSize(12)
        header_font.setBold(True)
        header.setFont(header_font)
        layout.addWidget(header)
        
        # File Tree
        self.file_tree = QTreeView()
        layout.addWidget(self.file_tree)
        
        # Scan-Optionen
        options_group = QGroupBox("🔧 Scan-Optionen")
        options_layout = QVBoxLayout()
        options_group.setLayout(options_layout)
        
        self.recursive_checkbox = QCheckBox("Rekursiv in Unterordnern scannen")
        self.recursive_checkbox.setChecked(True)
        options_layout.addWidget(self.recursive_checkbox)
        
        self.hidden_files_checkbox = QCheckBox("Versteckte Dateien einschließen")
        options_layout.addWidget(self.hidden_files_checkbox)
        
        # Dateityp-Filter
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Dateityp-Filter:"))
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("*.dat, *.json, *.txt (leer = alle)")
        filter_layout.addWidget(self.filter_input)
        options_layout.addLayout(filter_layout)
        
        layout.addWidget(options_group)
        
        # Ausgewählte Dateien
        selected_group = QGroupBox("✅ Ausgewählte Scan-Ziele")
        selected_layout = QVBoxLayout()
        selected_group.setLayout(selected_layout)
        
        self.selected_list = QTextEdit()
        self.selected_list.setMaximumHeight(100)
        self.selected_list.setPlaceholderText("Klicken Sie auf Dateien/Ordner im Tree oben...")
        selected_layout.addWidget(self.selected_list)
        
        layout.addWidget(selected_group)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        add_file_btn = QPushButton("📄 Datei hinzufügen")
        add_file_btn.clicked.connect(self.add_selected_file)
        button_layout.addWidget(add_file_btn)
        
        add_folder_btn = QPushButton("📁 Ordner hinzufügen")
        add_folder_btn.clicked.connect(self.add_selected_folder)
        button_layout.addWidget(add_folder_btn)
        
        clear_btn = QPushButton("🗑️ Leeren")
        clear_btn.clicked.connect(self.clear_selection)
        button_layout.addWidget(clear_btn)
        
        button_layout.addStretch()
        
        start_btn = QPushButton("🚀 SCAN STARTEN")
        start_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-size: 12px;
                font-weight: bold;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        start_btn.clicked.connect(self.start_scan)
        button_layout.addWidget(start_btn)
        
        cancel_btn = QPushButton("❌ Abbrechen")
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)
        
        layout.addLayout(button_layout)
    
    def setup_file_tree(self):
        """Initialisiert den File Tree"""
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath(QDir.homePath())
        
        self.file_tree.setModel(self.file_model)
        self.file_tree.setRootIndex(self.file_model.index(QDir.homePath()))
        
        # Spalten-Breiten
        self.file_tree.setColumnWidth(0, 300)
        self.file_tree.setColumnWidth(1, 100)
        self.file_tree.setColumnWidth(2, 100)
        
        # Single Selection
        self.file_tree.setSelectionMode(QTreeView.SelectionMode.SingleSelection)
    
    def add_selected_file(self):
        """Fügt die ausgewählte Datei hinzu"""
        indexes = self.file_tree.selectedIndexes()
        if not indexes:
            QMessageBox.warning(self, "Warnung", "Bitte wählen Sie eine Datei aus.")
            return
        
        file_path = self.file_model.filePath(indexes[0])
        if os.path.isfile(file_path):
            if file_path not in self.selected_files:
                self.selected_files.append(file_path)
                self.update_selected_list()
        else:
            QMessageBox.information(self, "Info", "Bitte wählen Sie eine Datei (nicht Ordner) aus.")
    
    def add_selected_folder(self):
        """Fügt den ausgewählten Ordner hinzu"""
        indexes = self.file_tree.selectedIndexes()
        if not indexes:
            QMessageBox.warning(self, "Warnung", "Bitte wählen Sie einen Ordner aus.")
            return
        
        folder_path = self.file_model.filePath(indexes[0])
        if os.path.isdir(folder_path):
            if folder_path not in self.selected_files:
                self.selected_files.append(folder_path)
                self.update_selected_list()
        else:
            QMessageBox.information(self, "Info", "Bitte wählen Sie einen Ordner (nicht Datei) aus.")
    
    def clear_selection(self):
        """Leert die Auswahl"""
        self.selected_files.clear()
        self.update_selected_list()
    
    def update_selected_list(self):
        """Aktualisiert die Liste der ausgewählten Dateien"""
        if self.selected_files:
            text = "\n".join([f"📄 {path}" if os.path.isfile(path) else f"📁 {path}" 
                             for path in self.selected_files])
        else:
            text = "Keine Dateien/Ordner ausgewählt"
        
        self.selected_list.setPlainText(text)
    
    def start_scan(self):
        """Startet den Scan mit den ausgewählten Dateien"""
        if not self.selected_files:
            QMessageBox.warning(self, "Warnung", "Bitte wählen Sie mindestens eine Datei oder einen Ordner aus.")
            return
        
        # Scan-Konfiguration sammeln
        scan_config = {
            'paths': self.selected_files,
            'recursive': self.recursive_checkbox.isChecked(),
            'include_hidden': self.hidden_files_checkbox.isChecked(),
            'file_filter': self.filter_input.text().strip() or "*"
        }
        
        self.files_selected.emit(self.selected_files)
        self.accept()


def main():
    """Test-Funktion"""
    from PyQt6.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    
    dialog = FileManagerDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        print(f"Ausgewählte Dateien: {dialog.selected_files}")
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()