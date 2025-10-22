# 🚀 GitHub Codespaces Setup Guide - Ultimate Wallet Recovery Tool

## 📋 Schnellstart für Codespaces

### 1. Codespace öffnen

Gehen Sie zu: https://github.com/swisscomfort/ultimate-wallet-recovery

Dann:
- Klicken Sie auf **Code** (grüner Button)
- Wählen Sie **Codespaces** Tab
- Klicken Sie **Create codespace on main**

**Oder direkt**: https://codespaces.new/swisscomfort/ultimate-wallet-recovery

---

## ⚙️ Initiale Setup (Automatisch)

Codespaces wird automatisch starten. Falls nicht, führen Sie manuell aus:

```bash
# Python Virtual Environment erstellen
python3 -m venv wallet-recovery-env

# Aktivieren
source wallet-recovery-env/bin/activate

# Dependencies installieren
pip install --upgrade pip
pip install -r requirements_qt6.txt
```

---

## 🏗️ Projekt-Struktur verstehen

```
ultimate-wallet-recovery/
├── src/
│   ├── core/                    # 🧠 Business Logic (GUI-unabhängig)
│   │   ├── blockchain/          # Blockchain-Operationen
│   │   │   ├── handler.py       # ⭐ API Calls, Balance Checks
│   │   │   ├── derivation.py   # BIP39/44/49/84/86 Paths
│   │   │   └── networks.py      # Network Configs (ETH, BTC, etc.)
│   │   ├── ai/                  # AI Recovery Engine
│   │   │   └── recovery_engine.py
│   │   ├── storage/             # Datenbank & Verschlüsselung
│   │   │   └── database.py
│   │   ├── forensic/            # Forensic Scanner
│   │   │   ├── signature_detection.py
│   │   │   └── file_scanner.py
│   │   └── config_manager.py    # Config & API Keys
│   │
│   ├── gui/                     # 🎨 Qt6 GUI Layer
│   │   ├── main_window.py       # ⭐ Main Window (Tab System)
│   │   ├── widgets/             # 📝 TODO: Widgets erstellen
│   │   ├── dialogs/             # 📝 TODO: Dialogs erstellen
│   │   └── themes/              # 📝 TODO: Theme System
│   │
│   └── legacy/                  # 🗄️ Alte Tkinter GUI (Reference)
│       └── wallet_recovery_ultimate.py
│
├── launcher_qt6.py              # ⭐ Qt6 GUI Starter
├── launcher.py                  # Legacy Launcher (für Referenz)
├── config.json                  # Konfiguration
├── .env                         # API Keys (erstellen!)
├── requirements_qt6.txt         # Qt6 Dependencies
└── MIGRATION_STATUS.md          # 📊 Fortschritt tracken
```

---

## 🎯 Entwicklungs-Workflow in Codespaces

### Phase 1: Environment Setup (Tag 1)

```bash
# 1. Virtual Environment aktivieren (falls nicht aktiv)
source wallet-recovery-env/bin/activate

# 2. Dependencies prüfen
pip list | grep -i pyqt6
pip list | grep -i bip

# 3. .env Datei erstellen (für API Keys)
cp .env.example .env
# Dann editieren und API Keys einfügen
nano .env
```

**Wichtig**: `.env` Datei mit Ihren API Keys:
```env
ETHERSCAN_API_KEY=your_key_here
BSCSCAN_API_KEY=your_key_here
POLYGONSCAN_API_KEY=your_key_here
ARBISCAN_API_KEY=your_key_here
```

### Phase 2: Core Module testen (Tag 1-2)

```bash
# Test: Blockchain Handler
python3 -c "
from src.core.blockchain.handler import BlockchainHandler
handler = BlockchainHandler()
print('✅ BlockchainHandler imported')
"

# Test: AI Engine
python3 -c "
from src.core.ai.recovery_engine import AIRecoveryEngine
engine = AIRecoveryEngine()
print('✅ AIRecoveryEngine imported')
"

# Test: Database
python3 -c "
from src.core.storage.database import DatabaseManager
db = DatabaseManager()
print('✅ Database initialized')
"
```

### Phase 3: GUI Development starten (Tag 2-5)

#### 3.1 Scanner Widget erstellen

```bash
# Erstelle Scanner Widget
mkdir -p src/gui/widgets
touch src/gui/widgets/__init__.py
code src/gui/widgets/scanner_widget.py
```

**Template für `scanner_widget.py`**:
```python
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QTextEdit, QPushButton, QProgressBar
)
from PyQt6.QtCore import pyqtSignal

class WalletScannerWidget(QWidget):
    """Wallet Scanner Tab - Seed/Key Input & Scanning"""
    
    scan_requested = pyqtSignal(str, str)  # (input_type, value)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("🔍 Wallet Scanner")
        header.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(header)
        
        # Seed Input
        seed_label = QLabel("Seed Phrase (12/24 words):")
        layout.addWidget(seed_label)
        
        self.seed_input = QTextEdit()
        self.seed_input.setPlaceholderText("Enter seed phrase here...")
        self.seed_input.setMaximumHeight(100)
        layout.addWidget(self.seed_input)
        
        # Scan Button
        scan_btn = QPushButton("🚀 Start Scan")
        scan_btn.clicked.connect(self.on_scan_clicked)
        layout.addWidget(scan_btn)
        
        # Progress
        self.progress = QProgressBar()
        layout.addWidget(self.progress)
        
        layout.addStretch()
        self.setLayout(layout)
    
    def on_scan_clicked(self):
        seed = self.seed_input.toPlainText().strip()
        if seed:
            self.scan_requested.emit("seed", seed)
```

#### 3.2 Widget ins Main Window integrieren

```bash
code src/gui/main_window.py
```

**In `main_window.py` ergänzen**:
```python
from src.gui.widgets.scanner_widget import WalletScannerWidget

# In setup_tabs():
scanner_widget = WalletScannerWidget()
scanner_widget.scan_requested.connect(self.on_scan_requested)
self.tabs.addTab(scanner_widget, "🔍 Scanner")
```

### Phase 4: Features migrieren (Tag 5-14)

#### Prioritätenliste:
1. ✅ **Scanner Widget** - Seed/Key Input
2. ⬜ **Network Selector** - Checkbox Grid für Netzwerke
3. ⬜ **Results Table** - Scan-Ergebnisse anzeigen
4. ⬜ **AI Recovery Widget** - Partial Seed Reconstruction
5. ⬜ **Forensic Widget** - Integration bestehendes Modul
6. ⬜ **Analytics Widget** - Dashboard mit Charts
7. ⬜ **QR Dialog** - QR Scanner/Generator
8. ⬜ **CSV Import/Export** - Bulk Operations

#### Migration-Workflow:

```bash
# 1. Feature aus Legacy identifizieren
code src/legacy/wallet_recovery_ultimate.py
# Suche: Ctrl+F "def setup_xxx"

# 2. Neues Widget erstellen
code src/gui/widgets/xxx_widget.py

# 3. Business Logic nach core/ extrahieren (falls nötig)
code src/core/xxx/handler.py

# 4. Im Main Window integrieren
code src/gui/main_window.py

# 5. Testen
python launcher_qt6.py

# 6. Status updaten
code MIGRATION_STATUS.md
```

---

## 🧪 Testing in Codespaces

### Unit Tests ausführen

```bash
# Erstelle test_xxx.py Dateien in tests/
mkdir -p tests
touch tests/__init__.py

# Test erstellen
cat > tests/test_blockchain.py << 'EOF'
import pytest
from src.core.blockchain.handler import BlockchainHandler

def test_blockchain_handler_init():
    handler = BlockchainHandler()
    assert handler is not None

def test_network_configs():
    from src.core.blockchain.networks import NETWORKS
    assert len(NETWORKS) > 0
    assert any(n['name'] == 'Ethereum' for n in NETWORKS)
EOF

# Tests ausführen
pytest tests/ -v
```

### GUI Testing (ohne Display)

Da Codespaces kein Display hat, können Sie:

1. **Headless Testing**:
```bash
# Qt6 mit offscreen platform
export QT_QPA_PLATFORM=offscreen
python launcher_qt6.py --test
```

2. **VNC Setup** (optional für visuelle Tests):
```bash
# VNC Server installieren
sudo apt-get update
sudo apt-get install -y x11vnc xvfb

# X Virtual Framebuffer starten
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99

# Jetzt GUI starten
python launcher_qt6.py
```

3. **Port Forwarding** für Web-Preview:
```bash
# Falls Flask Backend läuft
python backend/app.py  # Port 5000
# Codespaces forwarded automatisch
```

---

## 📊 Fortschritt tracken

### Migration Status updaten

```bash
# Nach jedem Feature-Abschluss
code MIGRATION_STATUS.md

# Status ändern von ⬜ auf ✅
# Notizen hinzufügen
```

### Git Workflow

```bash
# Feature Branch erstellen
git checkout -b feature/scanner-widget

# Änderungen committen
git add src/gui/widgets/scanner_widget.py
git commit -m "✅ Add Scanner Widget with seed input"

# Pushen
git push origin feature/scanner-widget

# Pull Request auf GitHub erstellen
```

---

## 🔧 Nützliche Codespaces Commands

### VS Code Shortcuts in Codespaces

- **Ctrl+Shift+P**: Command Palette
- **Ctrl+P**: Quick File Open
- **Ctrl+Shift+F**: Search in all files
- **Ctrl+`**: Toggle Terminal
- **F5**: Start Debugging

### Terminal Tricks

```bash
# Schnell zu wichtigen Dateien
alias main='code src/gui/main_window.py'
alias status='code MIGRATION_STATUS.md'
alias plan='code MIGRATION_PLAN.md'

# Environment aktivieren shortcut
alias venv='source wallet-recovery-env/bin/activate'

# Quick test
alias test='pytest tests/ -v'
```

### Python REPL für schnelle Tests

```bash
python3
>>> from src.core.blockchain.handler import BlockchainHandler
>>> handler = BlockchainHandler()
>>> handler.get_available_networks()
# Teste interaktiv
```

---

## 🐛 Troubleshooting in Codespaces

### Problem: PyQt6 Import Error

```bash
# Lösung: Reinstall
pip uninstall PyQt6 -y
pip install PyQt6==6.6.0
```

### Problem: Display nicht verfügbar

```bash
# Lösung: Offscreen Platform
export QT_QPA_PLATFORM=offscreen
# Oder für Tests:
export QT_QPA_PLATFORM=minimal
```

### Problem: API Keys nicht gefunden

```bash
# Prüfen ob .env existiert
ls -la .env

# Falls nicht, erstellen
cp .env.example .env
nano .env  # API Keys eintragen
```

### Problem: Module not found

```bash
# Prüfe Python Path
python3 -c "import sys; print('\n'.join(sys.path))"

# Stelle sicher, dass du im richtigen Dir bist
pwd  # sollte /workspaces/ultimate-wallet-recovery sein

# Virtual env aktivieren
source wallet-recovery-env/bin/activate
```

---

## 📚 Nützliche Ressourcen

### Dokumentation Links

- **Qt6 Docs**: https://doc.qt.io/qt-6/
- **PyQt6 Tutorial**: https://www.pythonguis.com/pyqt6-tutorial/
- **BIP39**: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
- **bip-utils Docs**: https://bip-utils.readthedocs.io/

### Codespaces Spezifisch

- **Codespaces Docs**: https://docs.github.com/en/codespaces
- **Port Forwarding**: https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace

### Projekt-spezifische Docs

```bash
# Alle READMEs durchlesen
cat README.md
cat README_QT6.md
cat MIGRATION_PLAN.md
cat .github/copilot-instructions.md
```

---

## 🎯 Täglicher Workflow (Empfohlen)

### Morgens (Start)

```bash
# 1. Codespace öffnen
# 2. Terminal öffnen
source wallet-recovery-env/bin/activate

# 3. Status prüfen
git status
cat MIGRATION_STATUS.md

# 4. Neueste Änderungen pullen
git pull origin main

# 5. Feature auswählen aus MIGRATION_STATUS.md
# 6. Feature Branch erstellen
git checkout -b feature/xxx
```

### Während der Arbeit

```bash
# Kontinuierlich testen
python launcher_qt6.py  # (mit offscreen if needed)

# Oder einzelne Module testen
python -m pytest tests/test_xxx.py -v

# Code formatieren
black src/gui/widgets/*.py

# Imports checken
isort src/gui/widgets/*.py
```

### Abends (Ende)

```bash
# Änderungen committen
git add .
git commit -m "✅ Feature XXX implemented"

# Pushen
git push origin feature/xxx

# Status updaten
code MIGRATION_STATUS.md
# ⬜ -> ✅ für erledigte Tasks

# Commit & Push Status
git add MIGRATION_STATUS.md
git commit -m "📊 Update migration status"
git push
```

---

## 🚀 Quick Start Checklist

Nach dem Öffnen von Codespaces:

- [ ] Virtual env aktivieren: `source wallet-recovery-env/bin/activate`
- [ ] Dependencies installieren: `pip install -r requirements_qt6.txt`
- [ ] .env Datei erstellen: `cp .env.example .env` + editieren
- [ ] Core Module testen: `python -c "from src.core.blockchain.handler import BlockchainHandler; print('OK')"`
- [ ] Main Window testen: `QT_QPA_PLATFORM=offscreen python launcher_qt6.py`
- [ ] Migration Status öffnen: `code MIGRATION_STATUS.md`
- [ ] Erste Task auswählen und starten! 🎊

---

## 💡 Produktivitäts-Tips

1. **Nutze GitHub Copilot** in Codespaces (meist schon aktiv)
2. **Split Editor**: Ctrl+\ für Side-by-Side Code
3. **Multi-Cursor**: Ctrl+Alt+Down für mehrere Cursors
4. **Snippet erstellen**: Für wiederholte PyQt6 Patterns
5. **Extensions**: Python, PyQt6, GitLens installieren

---

## 📞 Hilfe bekommen

Wenn Sie stuck sind:

1. **Copilot fragen**: In Codespaces verfügbar
2. **Issues erstellen**: https://github.com/swisscomfort/ultimate-wallet-recovery/issues
3. **Copilot Instructions lesen**: `.github/copilot-instructions.md`
4. **Legacy Code anschauen**: `src/legacy/` für Referenz

---

**Viel Erfolg! 🚀 Sie schaffen das!**
