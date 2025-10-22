#!/usr/bin/env python3
"""
Mehrsprachige Übersetzungen für Ultimate Wallet Recovery Tool
Unterstützt: Deutsch (DE), Englisch (EN)
"""

TRANSLATIONS = {
    'de': {
        # Hauptfenster
        'window_title': '🚀 Ultimate Wallet Recovery Tool - Enterprise Edition',
        'main_header': '🚀 Ultimate Wallet Recovery Scanner',
        
        # Tabs
        'tab_seed': '🌱 Seed Phrase',
        'tab_privkey': '🔑 Private Key',
        'tab_ai': '🧠 KI-Wiederherstellung',
        
        # Input Labels
        'seed_label': 'Seed Phrase (12/15/18/24 Wörter):',
        'language_label': 'Sprache:',
        'passphrase_label': 'BIP39 Passphrase (optional):',
        'privkey_label': 'Private Key (HEX-Format):',
        'ai_seed_label': 'Teilweise/Beschädigte Seed (nutze ? für fehlende Wörter):',
        
        # Buttons
        'btn_ai_reconstruct': '🧠 KI Rekonstruieren',
        'btn_start_scan': '🚀 SCAN STARTEN',
        'btn_stop': '⏹️ Stopp',
        'btn_clear': '🗑️ Löschen',
        'btn_export': '📤 Exportieren',
        
        # Advanced Options
        'advanced_options': '🔧 Erweiterte Optionen',
        'networks_label': 'Zu scannende Netzwerke:',
        'derivation_mode': 'Ableitungsmodus:',
        
        # Progress
        'progress_title': '📊 Scan-Fortschritt',
        'ready_status': 'Bereit zum Scannen',
        'scanned_label': 'Gescannt:',
        'found_label': 'Gefunden:',
        'value_label': 'Wert:',
        
        # Results
        'results_title': '📊 Live-Scan-Ergebnisse',
        'auto_refresh': 'Auto-Aktualisierung',
        'refresh_interval': 'Intervall (s):',
        
        # Table Headers
        'col_network': 'Netzwerk',
        'col_address': 'Adresse',
        'col_balance': 'Guthaben',
        'col_transactions': 'Transaktionen',
        'col_value_chf': 'Wert (CHF)',
        'col_status': 'Status',
        'col_path': 'Ableitungspfad',
        
        # Analytics
        'analytics_title': '📈 Analytics Dashboard',
        'total_scans': 'Gesamt-Scans:',
        'total_found': 'Gefundene Wallets:',
        'total_value': 'Gesamtwert (CHF):',
        'best_network': 'Bestes Netzwerk:',
        'avg_scan_time': 'Ø Scan-Zeit:',
        'success_rate': 'Erfolgsrate:',
        
        # Messages
        'msg_scan_progress': 'Scan läuft...',
        'msg_scan_complete': 'Scan abgeschlossen!',
        'msg_no_results': 'Keine Ergebnisse gefunden',
        'msg_wallet_found': 'Wallet gefunden!',
        
        # Warnings
        'warn_scan_running': 'Scan läuft bereits!',
        'warn_provide_input': 'Bitte Seed Phrase, Private Key oder KI-Wiederherstellung angeben!',
        'warn_select_network': 'Bitte mindestens ein Netzwerk auswählen!',
        
        # Errors
        'error_scan_failed': 'Scan fehlgeschlagen:',
        'error_invalid_seed': 'Ungültige Seed Phrase!',
        'error_invalid_privkey': 'Ungültiger Private Key!',
        'error_database': 'Datenbankfehler:',
        
        # Success Messages
        'success_export': 'Erfolgreich nach {} exportiert',
        'success_clear': 'Ergebnisse gelöscht',
        
        # AI Recovery
        'ai_reconstructing': 'KI rekonstruiert Seed...',
        'ai_suggestions': 'KI-Vorschläge:',
        'ai_combinations': 'Mögliche Kombinationen:',
        
        # Derivation Paths
        'deriv_standard': 'Standard (BIP44)',
        'deriv_bitcoin_legacy': 'Bitcoin Legacy',
        'deriv_bitcoin_segwit': 'Bitcoin SegWit',
        'deriv_bitcoin_native': 'Bitcoin Native SegWit',
        'deriv_bitcoin_taproot': 'Bitcoin Taproot',
        'deriv_custom': 'Benutzerdefiniert',
        
        # QR Code
        'qr_title': 'QR-Code',
        'qr_save': 'QR speichern',
        
        # Security
        'security_title': '🔐 Sicherheit',
        'encrypt_results': 'Ergebnisse verschlüsseln',
        'password_prompt': 'Passwort eingeben:',
        
        # Forensic Mode
        'forensic_title': '🔍 Forensische Analyse',
        'scan_path': 'Scan-Pfad:',
        'scan_mode': 'Scan-Modus:',
        'scan_depth': 'Tiefe:',
        'signature_types': 'Signaturtypen:',
        'risk_assessment': 'Risikobewertung',
        
        # Database
        'db_results': 'Datenbank-Ergebnisse',
        'db_export': 'DB Exportieren',
        'db_import': 'DB Importieren',
        'db_clear': 'DB Löschen',
        
        # Settings
        'settings_title': '⚙️ Einstellungen',
        'api_keys': 'API-Schlüssel',
        'appearance': 'Erscheinungsbild',
        'theme': 'Theme:',
        'language_setting': 'Sprache:',
        
        # Menu Items
        'menu_file': 'Datei',
        'menu_edit': 'Bearbeiten',
        'menu_view': 'Ansicht',
        'menu_tools': 'Tools',
        'menu_help': 'Hilfe',
        'menu_exit': 'Beenden',
        'menu_about': 'Über',
        
        # Status Messages
        'status_ready': 'Bereit',
        'status_scanning': 'Wird gescannt...',
        'status_processing': 'Wird verarbeitet...',
        'status_done': 'Fertig',
        
        # Currency
        'currency_chf': 'CHF',
        'currency_usd': 'USD',
        'currency_eur': 'EUR',
    },
    
    'en': {
        # Main Window
        'window_title': '🚀 Ultimate Wallet Recovery Tool - Enterprise Edition',
        'main_header': '🚀 Ultimate Wallet Recovery Scanner',
        
        # Tabs
        'tab_seed': '🌱 Seed Phrase',
        'tab_privkey': '🔑 Private Key',
        'tab_ai': '🧠 AI Recovery',
        
        # Input Labels
        'seed_label': 'Seed Phrase (12/15/18/24 words):',
        'language_label': 'Language:',
        'passphrase_label': 'BIP39 Passphrase (optional):',
        'privkey_label': 'Private Key (HEX format):',
        'ai_seed_label': 'Partial/Damaged Seed (use ? for missing words):',
        
        # Buttons
        'btn_ai_reconstruct': '🧠 AI Reconstruct',
        'btn_start_scan': '🚀 START SCAN',
        'btn_stop': '⏹️ Stop',
        'btn_clear': '🗑️ Clear',
        'btn_export': '📤 Export',
        
        # Advanced Options
        'advanced_options': '🔧 Advanced Options',
        'networks_label': 'Networks to scan:',
        'derivation_mode': 'Derivation Mode:',
        
        # Progress
        'progress_title': '📊 Scan Progress',
        'ready_status': 'Ready to scan',
        'scanned_label': 'Scanned:',
        'found_label': 'Found:',
        'value_label': 'Value:',
        
        # Results
        'results_title': '📊 Live Scan Results',
        'auto_refresh': 'Auto-refresh',
        'refresh_interval': 'Interval (s):',
        
        # Table Headers
        'col_network': 'Network',
        'col_address': 'Address',
        'col_balance': 'Balance',
        'col_transactions': 'Transactions',
        'col_value_chf': 'Value (CHF)',
        'col_status': 'Status',
        'col_path': 'Derivation Path',
        
        # Analytics
        'analytics_title': '📈 Analytics Dashboard',
        'total_scans': 'Total Scans:',
        'total_found': 'Wallets Found:',
        'total_value': 'Total Value (CHF):',
        'best_network': 'Best Network:',
        'avg_scan_time': 'Avg Scan Time:',
        'success_rate': 'Success Rate:',
        
        # Messages
        'msg_scan_progress': 'Scanning in progress...',
        'msg_scan_complete': 'Scan completed!',
        'msg_no_results': 'No results found',
        'msg_wallet_found': 'Wallet found!',
        
        # Warnings
        'warn_scan_running': 'Scan already in progress!',
        'warn_provide_input': 'Please provide seed phrase, private key, or use AI recovery!',
        'warn_select_network': 'Please select at least one network!',
        
        # Errors
        'error_scan_failed': 'Scan failed:',
        'error_invalid_seed': 'Invalid seed phrase!',
        'error_invalid_privkey': 'Invalid private key!',
        'error_database': 'Database error:',
        
        # Success Messages
        'success_export': 'Successfully exported to {}',
        'success_clear': 'Results cleared',
        
        # AI Recovery
        'ai_reconstructing': 'AI reconstructing seed...',
        'ai_suggestions': 'AI Suggestions:',
        'ai_combinations': 'Possible Combinations:',
        
        # Derivation Paths
        'deriv_standard': 'Standard (BIP44)',
        'deriv_bitcoin_legacy': 'Bitcoin Legacy',
        'deriv_bitcoin_segwit': 'Bitcoin SegWit',
        'deriv_bitcoin_native': 'Bitcoin Native SegWit',
        'deriv_bitcoin_taproot': 'Bitcoin Taproot',
        'deriv_custom': 'Custom',
        
        # QR Code
        'qr_title': 'QR Code',
        'qr_save': 'Save QR',
        
        # Security
        'security_title': '🔐 Security',
        'encrypt_results': 'Encrypt results',
        'password_prompt': 'Enter password:',
        
        # Forensic Mode
        'forensic_title': '🔍 Forensic Analysis',
        'scan_path': 'Scan Path:',
        'scan_mode': 'Scan Mode:',
        'scan_depth': 'Depth:',
        'signature_types': 'Signature Types:',
        'risk_assessment': 'Risk Assessment',
        
        # Database
        'db_results': 'Database Results',
        'db_export': 'Export DB',
        'db_import': 'Import DB',
        'db_clear': 'Clear DB',
        
        # Settings
        'settings_title': '⚙️ Settings',
        'api_keys': 'API Keys',
        'appearance': 'Appearance',
        'theme': 'Theme:',
        'language_setting': 'Language:',
        
        # Menu Items
        'menu_file': 'File',
        'menu_edit': 'Edit',
        'menu_view': 'View',
        'menu_tools': 'Tools',
        'menu_help': 'Help',
        'menu_exit': 'Exit',
        'menu_about': 'About',
        
        # Status Messages
        'status_ready': 'Ready',
        'status_scanning': 'Scanning...',
        'status_processing': 'Processing...',
        'status_done': 'Done',
        
        # Currency
        'currency_chf': 'CHF',
        'currency_usd': 'USD',
        'currency_eur': 'EUR',
    }
}


class Translator:
    """Übersetzungsmanager für die Anwendung"""
    
    def __init__(self, language='de'):
        """
        Initialisiert den Übersetzer
        
        Args:
            language: Sprachcode ('de' oder 'en')
        """
        self.language = language
        self.translations = TRANSLATIONS.get(language, TRANSLATIONS['en'])
    
    def t(self, key: str, fallback: str = None) -> str:
        """
        Übersetzt einen Schlüssel
        
        Args:
            key: Übersetzungsschlüssel
            fallback: Fallback-Text wenn Schlüssel nicht gefunden
            
        Returns:
            Übersetzter Text oder Fallback
        """
        return self.translations.get(key, fallback or key)
    
    def set_language(self, language: str):
        """Setzt die aktuelle Sprache"""
        if language in TRANSLATIONS:
            self.language = language
            self.translations = TRANSLATIONS[language]
    
    def get_language(self) -> str:
        """Gibt die aktuelle Sprache zurück"""
        return self.language


# Globale Übersetzer-Instanz (Standard: Deutsch)
_translator = Translator('de')


def t(key: str, fallback: str = None) -> str:
    """Globale Übersetzungsfunktion"""
    return _translator.t(key, fallback)


def set_language(language: str):
    """Setzt die globale Sprache"""
    _translator.set_language(language)


def get_language() -> str:
    """Gibt die aktuelle Sprache zurück"""
    return _translator.get_language()
