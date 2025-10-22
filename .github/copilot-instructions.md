# Copilot Instructions for Ultimate Wallet Recovery

## Project Scope

**Qt6-based unified wallet recovery system** - Cleaned up and focused:

- **🎯 Qt6 GUI (ONLY)** (`src/gui/main_window.py`): Modern Qt6 interface with comprehensive Scanner Widget
- **CLI Scanner** (`scan_runner.py`): Standalone file scanner for command-line use

**DELETED**: Legacy Tkinter GUI, Forensic GUI, Demo GUI, old launchers - all removed for focus.

Core architecture centers on `src/core/` containing blockchain handlers, configuration management, AI recovery engine, and SQLite storage.

## Key Patterns & Conventions

### Qt6 GUI Development Focus

- **Main Window** (`src/gui/main_window.py`): Tab-based interface with unified launcher
- **Widget System** (`src/gui/widgets/`): Modular widgets for different functions
  - `scanner_widget.py`: ✅ Full-featured scanner with 4 modes:
    - 🌱 Seed Phrase scanning (12+ blockchains)
    - 🔑 Private Key import and scanning
    - 🧠 AI Recovery for damaged seeds
    - 📁 File Scanner with pattern matching
  - `file_manager_dialog.py`: ✅ File/folder selection dialog
- **Signal/Slot Architecture**: Qt6 pattern for widget communication
  ```python
  # Widget to Main Window communication
  self.scanner_widget.scan_started.connect(self.on_scan_started)
  self.scanner_widget.scan_completed.connect(self.on_scan_completed)
  ```

### Configuration & Localization

- **ConfigManager** (`src/core/config_manager.py`): Encrypted configuration via `config.get_api_key('service')`, loads `.env` + `config.json`
- **Translation System** (`src/core/translations.py`): German-first localization with `t('key')` function, default language 'de'
  ```python
  from core.translations import t, set_language
  button_text = t('btn_start_scan')  # "🚀 SCAN STARTEN"
  ```

### Blockchain Architecture

- **Networks** (`src/core/blockchain/networks.py`): Import `NETWORKS` as List[NetworkConfig], use `get_enabled_networks()`
- **Network Objects**: Use `network.symbol`, `network.name`, `network.enabled` (not dictionary access)
- **Derivation** (`src/core/blockchain/derivation.py`): BIP44/49/84/86 path standards per blockchain
- **AI Recovery** (`src/core/ai/recovery_engine.py`): Fuzzy matching, pattern recognition, checksum repair

### Storage & Security

- **Database** (`src/core/storage/database.py`): SQLite with auto-table creation, use `save_scan_result()` methods
- **Encryption**: AES-256 for sensitive data, secure memory deletion patterns, TPM 2.0 support

## Essential Commands

```bash
# Activate environment (ALWAYS required)
source wallet-recovery-env/bin/activate

# 🎯 ONLY: Qt6 GUI (simplified launcher)
python launcher.py

# CLI file scanner
python scan_runner.py --path ./target --mode deep --db results.db

# Test German translations
python test_translations.py
```

## Development Priorities

### 🎯 Current Focus: Qt6 GUI Enhancement

1. **Scanner Widget**: ✅ Complete with 4 scanning modes, progress tracking, results table
2. **AI Recovery Widget**: 🔄 Next priority - integrate fuzzy matching and seed reconstruction
3. **Analytics Widget**: 📋 Dashboard for scan statistics and historical data
4. **Settings Widget**: ⚙️ Configuration panel for API keys and preferences

### Widget Development Pattern

```python
# Create new widget in src/gui/widgets/
class NewWidget(QWidget):
    # Define signals for main window communication
    action_completed = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        # Use core modules for business logic
        from core.blockchain import NETWORKS
        # Build Qt6 interface

# Integrate in main_window.py
self.new_widget = NewWidget(self)
self.new_widget.action_completed.connect(self.handle_action)
self.tab_widget.addTab(self.new_widget, "🔧 New Feature")
```

## Development Notes

### Current Status

- ✅ **Qt6 Main Window**: Functional with tab system, menu, toolbar
- ✅ **Scanner Widget**: Complete 4-mode scanner with real-time progress
- ✅ **File Manager**: Functional file/folder selection dialog
- ✅ **Cleanup Complete**: All legacy GUIs removed for focus
- 🔄 **Core Integration**: All blockchain/AI/storage modules GUI-independent

### Testing & Database

- Translation tests: `python test_translations.py`
- Database inspection: `sqlite3 wallet_recovery.db "SELECT * FROM scan_results;"`
- Widget testing: `python src/gui/widgets/scanner_widget.py` (standalone)

### Dependencies

- **Production**: `pip install -r requirements_qt6.txt`
- **CLI Tools**: Optional external tools (binwalk, foremost, strings) auto-detected

---

_Single Qt6 GUI focus. All new features should be implemented as Qt6 widgets._

```

## Debug System (`--debug-mode`)

Five distinct debug modes in `launcher.py` DEBUG_CONFIG:

- **basic**: Default with stacktrace + rotating logs
- **trace**: Function tracing with JSONL logging
- **safe**: Read-only mode with mocked database/API calls
- **perf**: CPU profiling with pstats output
- **io**: Detailed I/O operation logging

## Development Notes

### Active Migration Status

- Qt6 GUI incomplete: Core modules done, widgets 40% complete (see `MIGRATION_STATUS.md`)
- German localization complete for Tkinter GUI
- Forensic module fully functional with Kali Linux integration

### Testing & Database

- Translation tests: `python test_translations.py`
- Database inspection: `sqlite3 wallet_recovery.db "SELECT * FROM scan_results;"`
- Demo GUI: `python demo_german_gui.py`

### Dependencies

- **Production**: `pip install -r requirements_integrated.txt`
- **Qt6 Migration**: `pip install -r requirements_qt6.txt`
- **Kali Tools**: Optional external tools (binwalk, foremost, strings) auto-detected

---

_Multi-mode architecture requires understanding operational context - forensic vs recovery vs GUI migration workflows are distinct codepaths._
```
