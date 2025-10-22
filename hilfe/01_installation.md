# Installation & Setup

## Systemanforderungen

### Mindestanforderungen
- **Betriebssystem**: Linux, macOS, Windows 10/11
- **Python**: Version 3.8 oder höher
- **RAM**: Mindestens 4 GB
- **Festplatte**: 500 MB freier Speicherplatz
- **Internet**: Für Blockchain-API-Zugriff (optional für Offline-Analyse)

### Empfohlene Konfiguration
- **Betriebssystem**: Ubuntu 20.04+ / Debian 11+ / macOS 12+
- **Python**: Version 3.10 oder höher
- **RAM**: 8 GB oder mehr
- **Festplatte**: 2 GB freier Speicherplatz (für Datenbank)
- **Internet**: Stabile Breitbandverbindung

## Installation

### Schritt 1: Repository klonen

```bash
git clone https://github.com/your-repo/ultimate-wallet-recovery.git
cd ultimate-wallet-recovery-main
```

### Schritt 2: Virtual Environment erstellen

**Linux/macOS:**
```bash
python3 -m venv wallet-recovery-env
source wallet-recovery-env/bin/activate
```

**Windows:**
```bash
python -m venv wallet-recovery-env
wallet-recovery-env\Scripts\activate
```

### Schritt 3: Abhängigkeiten installieren

**Vollständige Installation (empfohlen):**
```bash
pip install -r requirements_integrated.txt
```

**Nur GUI (ohne Forensik):**
```bash
pip install -r requirements.txt
```

**Qt6 GUI (experimentell):**
```bash
pip install -r requirements_qt6.txt
```

### Schritt 4: Umgebungsvariablen konfigurieren

1. Kopieren Sie die Beispiel-Konfiguration:
```bash
cp .env.example .env
```

2. Bearbeiten Sie `.env` und fügen Sie Ihre API-Keys ein:
```bash
nano .env  # oder verwenden Sie einen anderen Editor
```

3. Fügen Sie mindestens diese Keys hinzu:
```
# Blockchain Explorer APIs
ETHERSCAN_API_KEY=IHR_ETHERSCAN_KEY
BSCSCAN_API_KEY=IHR_BSCSCAN_KEY
POLYGONSCAN_API_KEY=IHR_POLYGONSCAN_KEY

# Optional
ARBISCAN_API_KEY=IHR_ARBISCAN_KEY
OPTIMISTIC_ETHERSCAN_API_KEY=IHR_OP_KEY
```

### Schritt 5: Installation überprüfen

```bash
# Test der Übersetzungen
python test_translations.py

# GUI-Demo starten
python demo_german_gui.py

# Hauptanwendung starten
python launcher.py --mode standard
```

## API-Keys erhalten

### Etherscan (Ethereum)
1. Besuchen Sie https://etherscan.io/
2. Registrieren Sie ein kostenloses Konto
3. Navigieren Sie zu "API-KEYs"
4. Erstellen Sie einen neuen API-Key
5. Fügen Sie ihn in `.env` ein

### BSCScan (Binance Smart Chain)
1. Besuchen Sie https://bscscan.com/
2. Gleicher Prozess wie Etherscan
3. API-Key in `.env` einfügen

### PolygonScan (Polygon/Matic)
1. Besuchen Sie https://polygonscan.com/
2. Registrieren und API-Key erstellen
3. In `.env` einfügen

### Weitere Explorer
- **Arbiscan**: https://arbiscan.io/
- **Optimistic Etherscan**: https://optimistic.etherscan.io/
- **Snowtrace** (Avalanche): https://snowtrace.io/
- **FTMScan** (Fantom): https://ftmscan.com/

## Fehlerbehebung bei Installation

### Problem: Python-Version zu alt

**Fehler**: `ERROR: Python 3.7 or later is required`

**Lösung**:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3.10 python3.10-venv

# macOS (mit Homebrew)
brew install python@3.10

# Dann erneut Virtual Environment erstellen
python3.10 -m venv wallet-recovery-env
```

### Problem: Pip-Pakete können nicht installiert werden

**Fehler**: `ERROR: Could not find a version that satisfies...`

**Lösung**:
```bash
# Pip aktualisieren
pip install --upgrade pip setuptools wheel

# Erneut versuchen
pip install -r requirements_integrated.txt
```

### Problem: bitcoinlib Installation schlägt fehl

**Fehler**: `ERROR: Failed building wheel for bitcoinlib`

**Lösung**:
```bash
# Abhängigkeiten installieren (Ubuntu/Debian)
sudo apt-get install build-essential python3-dev libssl-dev

# macOS
xcode-select --install

# Dann erneut versuchen
pip install bitcoinlib==0.7.4
```

### Problem: PyQt6 Installation auf Linux

**Fehler**: `ImportError: libQt6...`

**Lösung**:
```bash
# Ubuntu/Debian
sudo apt install python3-pyqt6 libqt6widgets6

# Fedora
sudo dnf install python3-qt6

# Oder pip neu installieren
pip install --upgrade PyQt6
```

### Problem: Keine Berechtigung zum Installieren

**Fehler**: `PermissionError: [Errno 13]...`

**Lösung**:
```bash
# NICHT sudo verwenden! Stattdessen:
# Sicherstellen, dass Virtual Environment aktiviert ist
source wallet-recovery-env/bin/activate

# Dann ohne sudo installieren
pip install -r requirements_integrated.txt
```

## Erste Schritte nach Installation

1. **Testen Sie die Installation**:
   ```bash
   python test_translations.py
   ```

2. **Starten Sie die GUI**:
   ```bash
   python launcher.py --mode standard
   ```

3. **Erkunden Sie die Hilfe**:
   - Lesen Sie die [Schnellstart-Anleitung](02_schnellstart.md)
   - Lernen Sie die [Benutzeroberfläche](03_benutzeroberflaeche.md) kennen

4. **Konfigurieren Sie API-Keys**:
   - Siehe [API-Konfiguration](12_api_konfiguration.md)

## Deinstallation

So entfernen Sie die Anwendung vollständig:

```bash
# Virtual Environment deaktivieren
deactivate

# Verzeichnis löschen
cd ..
rm -rf ultimate-wallet-recovery-main

# Optional: Datenbank löschen
rm wallet_recovery.db
```

## Updates

So aktualisieren Sie auf die neueste Version:

```bash
# Im Projektverzeichnis
git pull origin main

# Virtual Environment aktivieren
source wallet-recovery-env/bin/activate

# Abhängigkeiten aktualisieren
pip install --upgrade -r requirements_integrated.txt
```

## Nächste Schritte

- ➡️ [Schnellstart-Anleitung](02_schnellstart.md)
- ➡️ [Benutzeroberfläche](03_benutzeroberflaeche.md)
- ➡️ [API-Konfiguration](12_api_konfiguration.md)
