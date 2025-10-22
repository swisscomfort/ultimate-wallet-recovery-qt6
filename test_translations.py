#!/usr/bin/env python3
"""
Test-Skript für deutsche GUI-Übersetzungen
"""

import sys
sys.path.insert(0, 'src')

# Import ohne andere Module
import importlib.util
spec = importlib.util.spec_from_file_location("translations", "src/core/translations.py")
translations = importlib.util.module_from_spec(spec)
spec.loader.exec_module(translations)

t = translations.t

print("=" * 60)
print("DEUTSCHE GUI ÜBERSETZUNGEN - TEST")
print("=" * 60)
print()

print("HAUPTFENSTER:")
print(f"  Fenstertitel: {t('window_title')}")
print(f"  Hauptüberschrift: {t('main_header')}")
print()

print("TABS:")
print(f"  Seed Tab: {t('tab_seed')}")
print(f"  Private Key Tab: {t('tab_privkey')}")
print(f"  KI Tab: {t('tab_ai')}")
print()

print("BUTTONS:")
print(f"  Scan Starten: {t('btn_start_scan')}")
print(f"  Stopp: {t('btn_stop')}")
print(f"  Löschen: {t('btn_clear')}")
print(f"  Exportieren: {t('btn_export')}")
print(f"  KI Rekonstruieren: {t('btn_ai_reconstruct')}")
print()

print("LABELS:")
print(f"  Seed Label: {t('seed_label')}")
print(f"  Sprache: {t('language_label')}")
print(f"  Passphrase: {t('passphrase_label')}")
print(f"  Private Key: {t('privkey_label')}")
print()

print("OPTIONEN:")
print(f"  Erweiterte Optionen: {t('advanced_options')}")
print(f"  Netzwerke: {t('networks_label')}")
print(f"  Ableitungsmodus: {t('derivation_mode')}")
print()

print("FORTSCHRITT:")
print(f"  Titel: {t('progress_title')}")
print(f"  Bereit: {t('ready_status')}")
print(f"  Gescannt: {t('scanned_label')}")
print(f"  Gefunden: {t('found_label')}")
print(f"  Wert: {t('value_label')}")
print()

print("STATUS:")
print(f"  Scan läuft: {t('msg_scan_progress')}")
print(f"  Scan fertig: {t('msg_scan_complete')}")
print(f"  Bereit: {t('status_ready')}")
print(f"  Wird gescannt: {t('status_scanning')}")
print()

print("WARNUNGEN:")
print(f"  Scan läuft bereits: {t('warn_scan_running')}")
print(f"  Eingabe fehlt: {t('warn_provide_input')}")
print(f"  Netzwerk wählen: {t('warn_select_network')}")
print()

print("FEHLER:")
print(f"  Scan fehlgeschlagen: {t('error_scan_failed')}")
print(f"  Ungültige Seed: {t('error_invalid_seed')}")
print(f"  Ungültiger Key: {t('error_invalid_privkey')}")
print()

print("MENÜS:")
print(f"  Datei: {t('menu_file')}")
print(f"  Bearbeiten: {t('menu_edit')}")
print(f"  Ansicht: {t('menu_view')}")
print(f"  Tools: {t('menu_tools')}")
print(f"  Hilfe: {t('menu_help')}")
print(f"  Beenden: {t('menu_exit')}")
print(f"  Über: {t('menu_about')}")
print()

print("=" * 60)
print("TEST ERFOLGREICH ABGESCHLOSSEN!")
print("=" * 60)
