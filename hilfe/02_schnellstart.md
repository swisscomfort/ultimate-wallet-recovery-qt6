# Schnellstart-Anleitung

## Willkommen! 🚀

Diese Anleitung führt Sie in 5 Minuten durch Ihre erste Wallet-Wiederherstellung.

## Voraussetzungen

✅ Installation abgeschlossen ([siehe Installation](01_installation.md))  
✅ Virtual Environment aktiviert  
✅ Mindestens ein API-Key konfiguriert (optional, aber empfohlen)

## Schnellstart: Wallet mit Seed Phrase wiederherstellen

### Schritt 1: GUI starten

```bash
# Terminal öffnen
cd /pfad/zum/ultimate-wallet-recovery-main

# Virtual Environment aktivieren
source wallet-recovery-env/bin/activate

# GUI starten
python launcher.py --mode standard
```

### Schritt 2: Seed Phrase eingeben

1. **Tab "🌱 Seed Phrase" auswählen** (sollte bereits aktiv sein)

2. **Seed Phrase eingeben** in das Textfeld:
   - 12, 15, 18 oder 24 Wörter
   - Durch Leerzeichen getrennt
   - Kleinbuchstaben verwenden

   **Beispiel:**
   ```
   abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about
   ```

3. **Sprache auswählen** (normalerweise "english")

4. **Optional: BIP39 Passphrase** eingeben (falls verwendet)

### Schritt 3: Netzwerke auswählen

Wählen Sie die Blockchain-Netzwerke aus, die gescannt werden sollen:

- ✅ **ETH** (Ethereum) - empfohlen
- ✅ **BTC** (Bitcoin) - empfohlen
- ✅ **BNB** (Binance Smart Chain)
- ✅ **MATIC** (Polygon)
- ⬜ **ARB** (Arbitrum)
- ⬜ **OP** (Optimism)

**Tipp:** Mehr Netzwerke = längere Scan-Zeit. Starten Sie mit 1-3 Netzwerken.

### Schritt 4: Scan starten

1. **Button "🚀 SCAN STARTEN"** klicken

2. **Warten Sie** während der Scan läuft:
   - Fortschrittsbalken beobachten
   - Live-Statistiken ansehen
   - Console-Output im rechten Bereich prüfen

3. **Ergebnisse werden automatisch angezeigt**:
   - Gefundene Adressen
   - Guthaben (falls vorhanden)
   - Transaktionsanzahl
   - Aktueller Wert in CHF

### Schritt 5: Ergebnisse prüfen

**Im Results-Bereich sehen Sie:**

```
📊 Live-Scan-Ergebnisse

Console:
🌐 Ethereum: 0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb
   ✅ Guthaben: 0.0 ETH | Transaktionen: 0

🌐 Bitcoin: bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh
   ✅ Guthaben: 0.0 BTC | Transaktionen: 0
```

**Wenn ein Guthaben gefunden wird:**
```
🎉 WALLET GEFUNDEN!
💰 Guthaben: 1.5 ETH
💵 Wert: 4,500.00 CHF
```

## Alternative: Private Key verwenden

### Schritt 1: Tab wechseln

Klicken Sie auf Tab **"🔑 Private Key"**

### Schritt 2: Private Key eingeben

Geben Sie Ihren Private Key im **HEX-Format** ein (64 Zeichen):

```
a1b2c3d4e5f6789012345678901234567890abcdefabcdefabcdefabcdefabcd
```

### Schritt 3: Scan starten

Button **"🚀 SCAN STARTEN"** klicken - der Rest funktioniert wie oben.

## KI-Wiederherstellung: Beschädigte Seed reparieren

### Wann verwenden?

- 🔸 Sie haben einige Wörter vergessen
- 🔸 Wörter sind unleserlich oder beschädigt
- 🔸 Reihenfolge teilweise unklar

### So funktioniert's:

1. **Tab "🧠 KI-Wiederherstellung"** öffnen

2. **Bekannte Wörter eingeben**, `?` für fehlende:
   ```
   abandon ? abandon abandon ? abandon abandon abandon ? abandon abandon about
   ```

3. **Button "🧠 KI Rekonstruieren"** klicken

4. **KI-Vorschläge prüfen**:
   - System schlägt mögliche Wörter vor
   - Kombinationen werden generiert
   - Top-Kandidaten werden getestet

5. **Ergebnisse prüfen** und beste Option wählen

**⚠️ Wichtig:** Je mehr Wörter fehlen, desto länger dauert die Rekonstruktion!

## Ergebnisse exportieren

### CSV-Export

1. Nach erfolgreichem Scan: **Button "📤 Exportieren"** klicken

2. **Speicherort wählen**

3. **Datei enthält:**
   - Alle gescannten Adressen
   - Guthaben und Werte
   - Netzwerk-Informationen
   - Zeitstempel

### Beispiel CSV:

```csv
Timestamp,Network,Address,Balance,Transactions,Value_CHF
2025-10-03 14:30:22,Ethereum,0x742d35...,0.5,12,1500.00
2025-10-03 14:30:25,Bitcoin,bc1qxy2k...,0.001,3,75.50
```

## Häufige Anfänger-Fehler

### ❌ Fehler 1: Seed Phrase mit Groß-/Kleinschreibung

**Falsch:**
```
Abandon Abandon Abandon...
```

**Richtig:**
```
abandon abandon abandon...
```

**Lösung:** Immer Kleinbuchstaben verwenden!

### ❌ Fehler 2: Wörter mit Komma getrennt

**Falsch:**
```
abandon,abandon,abandon...
```

**Richtig:**
```
abandon abandon abandon...
```

**Lösung:** Nur Leerzeichen als Trenner!

### ❌ Fehler 3: Falsche Wortanzahl

**Fehler:** 13 Wörter eingegeben (ungültig)

**Richtig:** Nur 12, 15, 18 oder 24 Wörter sind gültig!

**Lösung:** Prüfen Sie die Anzahl der Wörter!

### ❌ Fehler 4: Kein Netzwerk ausgewählt

**Fehler:** "Bitte mindestens ein Netzwerk auswählen!"

**Lösung:** Mindestens eine Checkbox aktivieren (z.B. ETH)

## Tipps für erfolgreiche Scans

### 🎯 Tipp 1: Starten Sie klein

Zuerst nur **1-2 Netzwerke** scannen, um die Funktion zu testen.

### 🎯 Tipp 2: API-Keys verwenden

Ohne API-Keys sind Funktionen eingeschränkt. Holen Sie sich kostenlose Keys:
- [Etherscan API](12_api_konfiguration.md)

### 🎯 Tipp 3: Derivation Paths verstehen

Verschiedene Wallets verwenden verschiedene Pfade:
- **Standard (BIP44)**: Die meisten Wallets
- **Bitcoin SegWit (BIP49)**: Moderne Bitcoin-Wallets
- **Bitcoin Native SegWit (BIP84)**: Neueste Bitcoin-Wallets

[Mehr über Derivation Paths](08_derivation_paths.md)

### 🎯 Tipp 4: Geduld haben

Ein vollständiger Multi-Blockchain-Scan kann 5-10 Minuten dauern.

### 🎯 Tipp 5: Ergebnisse sichern

Exportieren Sie wichtige Ergebnisse sofort als CSV!

## Was kommt als Nächstes?

### Grundlagen vertiefen:
- 📖 [Benutzeroberfläche](03_benutzeroberflaeche.md) - Alle Features erklärt
- 📖 [Seed Phrase Recovery](04_seed_recovery.md) - Detaillierte Anleitung
- 📖 [Multi-Blockchain Support](07_blockchain_support.md) - Alle Netzwerke

### Erweiterte Features:
- 🔧 [KI-Wiederherstellung](06_ki_wiederherstellung.md) - AI-Features nutzen
- 🔧 [Forensische Analyse](09_forensische_analyse.md) - Datenträger scannen
- 🔧 [Sicherheit](10_sicherheit.md) - Sichere Nutzung

### Probleme?
- 🆘 [Häufige Probleme](13_haeufige_probleme.md) - FAQ
- 🆘 [Fehlermeldungen](14_fehlermeldungen.md) - Fehler beheben

## Schnellreferenz: Wichtigste Befehle

```bash
# GUI starten
python launcher.py --mode standard

# Forensische Analyse
python launcher.py --mode forensic

# Qt6 GUI (experimentell)
python launcher_qt6.py --mode qt6

# CLI Scan
python scan_runner.py --path /pfad --mode deep

# Übersetzungen testen
python test_translations.py

# Demo GUI
python demo_german_gui.py
```

## Nächste Schritte

➡️ [Benutzeroberfläche im Detail](03_benutzeroberflaeche.md)  
➡️ [Seed Phrase Recovery](04_seed_recovery.md)  
➡️ [Alle Blockchain-Netzwerke](07_blockchain_support.md)
