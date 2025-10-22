# 🚀 Ultimate Wallet Recovery Tool - Qt6 Edition

![Version](https://img.shields.io/badge/version-4.0.0--qt6-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![Qt](https://img.shields.io/badge/Qt-6.6+-success)
![Status](https://img.shields.io/badge/status-Active%20Development-yellow)

## ✨ Neue Qt6 Architektur

**Komplett neu aufgebaut** mit professioneller, modularer Architektur:
- 🏗️ **GUI-unabhängige Business Logic** - Vollständig testbar
- ⚡ **Async/Await Support** - Non-blocking API calls
- 🎨 **Moderne Qt6 UI** - Native Performance
- 🔧 **Modulares Design** - Einfach erweiterbar

---

## 🎯 Quick Start

### Installation

```bash
# 1. Virtual Environment aktivieren
source wallet-recovery-env/bin/activate

# 2. Qt6 Dependencies installieren
pip install -r requirements_qt6.txt

# 3. GUI starten
python launcher_qt6.py
```

### Alternativen

```bash
# Legacy Tkinter GUI (nicht empfohlen)
python launcher_qt6.py --mode legacy

# CLI Scanner
python scan_runner.py --path /path/to/scan
```

---

## 📁 Neue Projektstruktur

```
ultimate-wallet-recovery/
├── src/
│   ├── core/                    # ✅ GUI-unabhängige Business Logic
│   │   ├── blockchain/          # Blockchain Handler, Networks, Derivation
│   │   ├── ai/                  # AI Recovery Engine
│   │   ├── storage/             # Database Manager
│   │   ├── forensic/            # Forensic Analysis (existing)
│   │   └── config_manager.py   # Configuration Management
│   │
│   ├── gui/                     # 🎨 Qt6 GUI Layer
│   │   ├── main_window.py      # Haupt-Fenster mit Tab-System
│   │   ├── widgets/            # Wiederverwendbare Widgets
│   │   ├── dialogs/            # Dialog-Fenster
│   │   ├── components/         # UI-Komponenten
│   │   └── themes/             # Theme-System
│   │
│   └── legacy/                  # 📦 Alte Tkinter GUI (archiviert)
│       └── wallet_recovery_ultimate.py
│
├── launcher_qt6.py              # Neuer unified launcher
├── requirements_qt6.txt         # Qt6 Dependencies
├── MIGRATION_PLAN.md           # Detaillierter Migrationsplan
└── MIGRATION_STATUS.md         # Aktueller Status
```

---

## ✨ Features

### ✅ Bereits Implementiert (Core Logic)

#### 🔗 Blockchain Module
- **12+ Netzwerke**: Ethereum, Bitcoin, BSC, Polygon, Arbitrum, etc.
- **Async Handler**: Non-blocking API calls mit aiohttp
- **Multi-Path Support**: BIP44, BIP49, BIP84, BIP86
- **Auto-Derivation**: Automatische Adress-Generierung

```python
from core.blockchain import BlockchainHandler, NETWORKS

async with BlockchainHandler() as handler:
    results = await handler.scan_multiple_networks(
        seed_phrase, networks, derivation_config
    )
```

#### 🧠 AI Recovery Engine
- **Fuzzy Matching**: Intelligente Worterkennung
- **Seed Reconstruction**: Unvollständige Seeds wiederherstellen
- **Auto-Correction**: Tippfehler automatisch korrigieren
- **Checksum Repair**: Checksum-Validierung und Reparatur

```python
from core.ai import AIRecoveryEngine

ai_engine = AIRecoveryEngine(language="english")
is_valid, corrected, fixes = ai_engine.repair_seed(damaged_seed)
```

#### 💾 Database Manager
- **SQLite Storage**: Persistente Speicherung
- **Analytics**: Statistiken und Erfolgsraten
- **Export**: CSV, JSON, Excel (geplant)

```python
from core.storage import DatabaseManager

db = DatabaseManager()
stats = db.get_statistics()
print(f"Success Rate: {stats['success_rate']:.2f}%")
```

### 🔄 In Entwicklung

#### 🎨 Qt6 GUI
- [x] Main Window mit Tab-System
- [x] MenuBar & ToolBar
- [x] StatusBar mit Network Status
- [ ] Scanner Widget (nächste Woche)
- [ ] AI Recovery Widget
- [ ] Forensic Widget Integration
- [ ] Analytics Dashboard
- [ ] Settings Panel

---

## 🚀 Entwicklung

### Widget Erstellen

```python
# src/gui/widgets/scanner_widget.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from core.blockchain import BlockchainHandler

class WalletScannerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        # Add your UI components
        self.setLayout(layout)
    
    async def start_scan(self):
        async with BlockchainHandler() as handler:
            results = await handler.scan_multiple_networks(...)
```

### Tests Schreiben

```python
# tests/test_blockchain.py
import pytest
from src.core.blockchain import BlockchainHandler

@pytest.mark.asyncio
async def test_address_generation():
    async with BlockchainHandler() as handler:
        addresses = handler.generate_addresses_from_seed(
            "test seed phrase...", network, derivation_config
        )
        assert len(addresses) == 5
```

---

## 📊 Migration Status

| Komponente | Status | Fortschritt |
|-----------|--------|-------------|
| Core Logic | ✅ Fertig | 100% |
| Qt6 Main Window | ✅ Fertig | 100% |
| Scanner Widget | 🔄 In Arbeit | 0% |
| AI Widget | ⏸️ Wartend | 0% |
| Forensic Widget | ⏸️ Wartend | 0% |
| Analytics Widget | ⏸️ Wartend | 0% |
| Settings Widget | ⏸️ Wartend | 0% |

**Gesamt-Fortschritt**: ~30%

Siehe [MIGRATION_STATUS.md](MIGRATION_STATUS.md) für Details.

---

## 🎯 Roadmap

### Woche 1 (Diese Woche)
- [x] Core Logic Extraction ✅
- [x] Qt6 Main Window ✅
- [ ] Scanner Widget
- [ ] AI Recovery Widget

### Woche 2
- [ ] Forensic Widget Integration
- [ ] Analytics Dashboard
- [ ] Theme System

### Woche 3
- [ ] Advanced Features (QR, CSV)
- [ ] Testing & Bug Fixes
- [ ] Documentation

**Target Release**: Version 4.0.0 in 3 Wochen

---

## 🔧 Dependencies

### Minimal
```bash
pip install PyQt6 bip-utils cryptography aiohttp requests qrcode[pil]
```

### Full
```bash
pip install -r requirements_qt6.txt
```

### Development
```bash
pip install -r requirements_qt6.txt
pip install pytest pytest-qt pytest-asyncio black flake8
```

---

## 📝 Dokumentation

- **User Guide**: [USER_GUIDE_DE.md](USER_GUIDE_DE.md)
- **Migration Plan**: [MIGRATION_PLAN.md](MIGRATION_PLAN.md)
- **Migration Status**: [MIGRATION_STATUS.md](MIGRATION_STATUS.md)
- **Development**: [README_DEV.md](README_DEV.md)

---

## 🤝 Contributing

Da das Tool noch in aktiver Entwicklung ist, sind Contributions sehr willkommen!

### Priorities
1. **Widget Implementation** - Scanner, AI, Forensic
2. **Testing** - Unit Tests für Core Logic
3. **Documentation** - Inline Comments, Docstrings
4. **Bug Fixes** - Issues auf GitHub

---

## 📜 License

MIT License - Siehe [LICENSE](LICENSE)

---

## 🙏 Credits

- **Qt6 Framework**: Cross-platform GUI excellence
- **BIP Utils**: Blockchain derivation library
- **Python Community**: Awesome ecosystem

---

## ⚠️ Hinweis

**Diese Version ist in aktiver Entwicklung!**
- Core Logic ist stabil und getestet ✅
- GUI Widgets werden gerade implementiert 🔄
- Für Produktiv-Einsatz Legacy Version verwenden

**Feedback willkommen!** GitHub Issues oder Discussions.
