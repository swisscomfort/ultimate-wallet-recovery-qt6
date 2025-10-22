# Benutzeroberfläche - Komplette Übersicht

## Hauptfenster

Die GUI ist in mehrere Bereiche unterteilt:

```
┌─────────────────────────────────────────────────────────────┐
│  🚀 Ultimate Wallet Recovery Tool - Enterprise Edition      │
├─────────────────────────────────────────────────────────────┤
│  [Datei] [Tools] [Ansicht] [Hilfe]                    Menü  │
├─────────────────────────────────────────────────────────────┤
│  [🔍 Quick Scan] [🧠 KI] [📊 Analytics] | Theme: [Dark ▼]   │ Toolbar
├──────────────────────────┬──────────────────────────────────┤
│                          │                                  │
│   Eingabe-Panel          │     Ergebnis-Panel              │
│                          │                                  │
│   • Seed Phrase          │     • Live-Console              │
│   • Private Key          │     • Tabellen-Ansicht          │
│   • KI-Wiederherstellung │     • Statistiken               │
│   • Netzwerk-Auswahl     │     • Charts                    │
│   • Optionen             │                                  │
│                          │                                  │
├──────────────────────────┴──────────────────────────────────┤
│  Status: Bereit  |  Gescannt: 0  |  Gefunden: 0            │ Statusbar
└─────────────────────────────────────────────────────────────┘
```

## Menüleiste

### Datei-Menü

**Neuer Scan**
- Startet einen frischen Scan
- Löscht vorherige Ergebnisse
- Tastenkombination: `Ctrl+N`

**CSV Importieren**
- Import von früheren Scan-Ergebnissen
- Unterstützt Standard-CSV-Format
- Tastenkombination: `Ctrl+I`

**Ergebnisse Exportieren**
- Export als CSV-Datei
- Enthält alle Scan-Daten
- Tastenkombination: `Ctrl+E`

**Beenden**
- Schließt die Anwendung
- Speichert Einstellungen automatisch
- Tastenkombination: `Ctrl+Q`

### Tools-Menü

**KI Seed Rekonstruktion**
- Öffnet KI-Wiederherstellungs-Dialog
- Für beschädigte Seeds
- Tastenkombination: `Ctrl+K`

**Adressen Generator**
- Generiert Adressen aus Seed/Key
- Batch-Generierung möglich
- Tastenkombination: `Ctrl+G`

**QR Code Scanner**
- Scannt QR-Codes mit Webcam
- Erkennt Private Keys und Adressen
- Tastenkombination: `Ctrl+Q`

**Ableitungs-Rechner**
- Berechnet Derivation Paths
- Zeigt alle möglichen Adressen
- Tastenkombination: `Ctrl+D`

### Ansicht-Menü

**Themes**
- **Dark**: Dunkles Theme (Standard)
- **Light**: Helles Theme
- **Blue**: Blaues Theme
- **Hacker**: Grünes Terminal-Theme

**Vollbild**
- Aktiviert Vollbildmodus
- Tastenkombination: `F11`

**Layout Zurücksetzen**
- Setzt GUI auf Standardlayout
- Nützlich nach Änderungen

### Hilfe-Menü

**Benutzerhandbuch**
- Öffnet diese Hilfe
- Vollständige Dokumentation

**Tastenkombinationen**
- Liste aller Shortcuts
- Tastenkombination: `Ctrl+H`

**Über**
- Versions-Informationen
- Lizenz und Credits

## Eingabe-Panel (Links)

### Tab 1: 🌱 Seed Phrase

**Seed Phrase Textfeld**
- Eingabe der Seed (12/15/18/24 Wörter)
- Auto-Vervollständigung aktiviert
- Fehlerprüfung in Echtzeit

**Sprache Dropdown**
```
[english        ▼]
```
Verfügbare Sprachen:
- english
- spanish
- french
- italian
- portuguese
- czech
- japanese
- korean
- chinese_simplified
- chinese_traditional

**BIP39 Passphrase**
- Optional, nur wenn verwendet
- Wird als Passwort-Feld angezeigt (*****)
- Wichtig für erweiterte Sicherheit

### Tab 2: 🔑 Private Key

**Private Key Textfeld**
- HEX-Format (64 Zeichen)
- Automatische Formatierung
- Validierung in Echtzeit

**Beispiel:**
```
a1b2c3d4e5f6789012345678901234567890abcdefabcdefabcdefabcdefabcd
```

### Tab 3: 🧠 KI-Wiederherstellung

**Partial Seed Eingabe**
- Bekannte Wörter eingeben
- `?` für fehlende Wörter
- System schlägt Alternativen vor

**Beispiel:**
```
abandon ? abandon abandon ? abandon abandon ? abandon abandon abandon about
```

**Button: 🧠 KI Rekonstruieren**
- Startet AI-Analyse
- Generiert Vorschläge
- Zeigt Top-Kandidaten

## Erweiterte Optionen

### 🔧 Netzwerk-Auswahl

**Checkboxen für jedes Netzwerk:**
```
☑ ETH    ☑ BTC    ☑ BNB
☑ MATIC  ☐ ARB    ☐ OP
☐ AVAX   ☐ FTM    ☐ BASE
```

**Tipps:**
- Mehr Netzwerke = längere Scan-Zeit
- Starten Sie mit 2-3 wichtigsten
- Alle aktivieren für vollständigen Scan

### Ableitungsmodus

**Dropdown-Auswahl:**
```
[Standard (BIP44)           ▼]
```

**Verfügbare Modi:**
- **Standard (BIP44)**: m/44'/60'/0'/0/x (EVM-Chains)
- **Bitcoin Legacy**: m/44'/0'/0'/0/x (P2PKH)
- **Bitcoin SegWit**: m/49'/0'/0'/0/x (P2SH-P2WPKH)
- **Bitcoin Native SegWit**: m/84'/0'/0'/0/x (P2WPKH)
- **Bitcoin Taproot**: m/86'/0'/0'/0/x (P2TR)
- **Benutzerdefiniert**: Eigener Pfad

[Mehr über Derivation Paths →](08_derivation_paths.md)

### Scan-Optionen (erweitert)

**Adress-Index-Bereich:**
```
Von: [0    ] Bis: [20   ]
```
- Scannt Adressen im angegebenen Bereich
- Standard: 0-20 (erste 21 Adressen)
- Kann erhöht werden bei Bedarf

**Timeout-Einstellungen:**
```
API Timeout: [15   ] Sekunden
```
- Zeit bis API-Anfrage abbricht
- Bei langsamer Verbindung erhöhen

## Scan-Steuerung

### Hauptbutton

**🚀 SCAN STARTEN**
- Großer grüner Button
- Startet den Wiederherstellungs-Prozess
- Wird zu "🔄 SCAN LÄUFT..." während Ausführung

### Sekundäre Buttons

**⏹️ Stopp**
- Bricht laufenden Scan ab
- Behält bisherige Ergebnisse
- Tastenkombination: `Ctrl+S`

**🗑️ Löschen**
- Löscht alle Ergebnisse
- Setzt GUI zurück
- Bestätigung erforderlich
- Tastenkombination: `Ctrl+L`

**📤 Exportieren**
- Speichert Ergebnisse als CSV
- Öffnet Speichern-Dialog
- Tastenkombination: `Ctrl+E`

## Fortschrittsanzeige

### 📊 Scan-Fortschritt

**Status-Label:**
```
Bereit zum Scannen
```

Mögliche Status:
- ⏸️ Bereit zum Scannen
- 🔄 Wird gescannt...
- ✅ Scan abgeschlossen!
- ❌ Fehler aufgetreten

**Fortschrittsbalken:**
```
[████████████████░░░░░░░░] 65%
```

**Live-Statistiken:**
```
Gescannt: 156  |  Gefunden: 3  |  Wert: 12,450.00 CHF
```

## Ergebnis-Panel (Rechts)

### Tab 1: 📟 Console

**Live-Output während Scan:**
```
🌐 Ethereum: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
   ✅ Guthaben: 1.5 ETH | Transaktionen: 45 | Wert: 4,500.00 CHF

🌐 Bitcoin: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
   ✅ Guthaben: 0.025 BTC | Transaktionen: 12 | Wert: 1,875.00 CHF

🎉 WALLET GEFUNDEN!
💰 Gesamtwert: 6,375.00 CHF
```

**Features:**
- Auto-Scroll zu neuesten Einträgen
- Farbcodierte Ausgabe
- Copy-Funktion (Rechtsklick)

### Tab 2: 📊 Tabelle

**Strukturierte Ergebnisansicht:**

| Netzwerk | Adresse | Guthaben | TX | Wert (CHF) | Status |
|----------|---------|----------|-----|-----------|---------|
| Ethereum | 0x742d... | 1.5 ETH | 45 | 4,500.00 | ✅ Aktiv |
| Bitcoin | bc1qxy... | 0.025 BTC | 12 | 1,875.00 | ✅ Aktiv |

**Funktionen:**
- Sortierbar nach Spalten (Klick auf Header)
- Filter-Funktion (Rechtsklick)
- Export einzelner Zeilen

### Tab 3: 📈 Statistiken

**Scan-Übersicht:**
```
📊 Gesamt-Statistiken

Netzwerke gescannt:    8
Adressen geprüft:      160
Wallets gefunden:      3
Gesamtwert:            6,375.00 CHF

Durchschn. Scan-Zeit:  2.3 Sekunden
Erfolgsrate:           1.88%
```

**Netzwerk-Verteilung (Chart):**
```
ETH  ████████████████████ 70.6%
BTC  ██████████ 29.4%
BNB  ░░░░░░░░░░ 0.0%
```

### Tab 4: 📑 Historie

**Frühere Scans:**
```
2025-10-03 14:30:22  |  3 Wallets  |  6,375 CHF
2025-10-02 09:15:10  |  0 Wallets  |  0 CHF
2025-10-01 18:45:33  |  1 Wallet   |  2,100 CHF
```

**Funktionen:**
- Laden früherer Ergebnisse
- Vergleich zwischen Scans
- Export-Historie

## Statusleiste (Unten)

**Permanente Informationsanzeige:**
```
Status: Bereit  |  Gescannt: 0  |  Gefunden: 0  |  🌐 Online  |  💾 DB: OK
```

**Elemente:**
- **Status**: Aktueller Zustand
- **Gescannt**: Anzahl geprüfter Adressen
- **Gefunden**: Wallets mit Guthaben
- **🌐 Verbindung**: Online/Offline Status
- **💾 Datenbank**: DB-Status

## Tastenkombinationen Übersicht

### Navigation
- `Ctrl+1-4`: Wechsel zwischen Tabs
- `Tab`: Nächstes Feld
- `Shift+Tab`: Vorheriges Feld

### Aktionen
- `Ctrl+N`: Neuer Scan
- `Ctrl+S`: Scan stoppen
- `Ctrl+L`: Ergebnisse löschen
- `Ctrl+E`: Exportieren
- `Ctrl+I`: Importieren

### Tools
- `Ctrl+K`: KI-Wiederherstellung
- `Ctrl+G`: Adressen-Generator
- `Ctrl+D`: Derivation-Rechner

### Ansicht
- `F11`: Vollbild
- `Ctrl++`: Vergrößern
- `Ctrl+-`: Verkleinern
- `Ctrl+0`: Zoom zurücksetzen

### Allgemein
- `Ctrl+Q`: Beenden
- `Ctrl+H`: Hilfe
- `F1`: Schnellhilfe

[Vollständige Liste →](16_tastenkombinationen.md)

## Themes

### Dark Theme (Standard)
- Schwarzer Hintergrund
- Weiße Schrift
- Grüne Akzente
- Augenschonend

### Light Theme
- Weißer Hintergrund
- Schwarze Schrift
- Blaue Akzente
- Tagsüber geeignet

### Hacker Theme
- Schwarzer Hintergrund
- Grüne Schrift
- Matrix-Stil
- Retro-Look

## Tipps zur Bedienung

### 💡 Tipp 1: Drag & Drop
Sie können Dateien direkt ins Seed-Feld ziehen:
- TXT-Dateien mit Seeds
- JSON mit Wallet-Daten

### 💡 Tipp 2: Rechtsklick-Menü
Rechtsklick auf Ergebnisse für:
- Kopieren
- Details anzeigen
- QR-Code generieren
- An Blockchain-Explorer senden

### 💡 Tipp 3: Auto-Save
Einstellungen werden automatisch gespeichert:
- Ausgewählte Netzwerke
- Theme-Präferenzen
- Fenster-Position

### 💡 Tipp 4: Dunkelmodus-Planung
Dunkelmodus aktiviert sich automatisch:
- Nachts (20:00 - 06:00)
- Kann in Einstellungen deaktiviert werden

## Nächste Schritte

➡️ [Seed Phrase Recovery im Detail](04_seed_recovery.md)  
➡️ [KI-Wiederherstellung nutzen](06_ki_wiederherstellung.md)  
➡️ [Alle Tastenkombinationen](16_tastenkombinationen.md)
