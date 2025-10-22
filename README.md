# 🚀 Ultimate Wallet Recovery Tool

<div align="center">

![Version](https://img.shields.io/badge/version-4.0.0--qt6-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![Qt](https://img.shields.io/badge/Qt-6.6+-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-Active%20Development-yellow)

**Professional cryptocurrency wallet recovery tool with AI-powered seed reconstruction**

[Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Security](#-security) • [Contributing](#-contributing)

</div>

---

## ⚠️ CRITICAL WARNINGS

> **READ BEFORE USE**: This is a powerful cryptographic tool. Misuse can result in permanent loss of funds.

- 🔴 **ONLY use for legitimate wallet recovery** - See [DISCLAIMER.md](DISCLAIMER.md)
- 🔴 **NEVER share your seed phrases or private keys**
- 🔴 **USE ON TRUSTED, OFFLINE SYSTEMS ONLY**
- 🔴 **ALWAYS test with small amounts first**
- 🔴 **READ [SECURITY.md](SECURITY.md) before using**

---

## ✨ Features

### 🧠 AI-Powered Recovery
- **Smart Seed Reconstruction**: Industry-first AI-based partial seed recovery
- **Fuzzy Matching**: Intelligent correction of incomplete or damaged seeds
- **Pattern Learning**: Self-learning algorithms for higher success rates
- **Multi-Language BIP39**: Support for 8 languages (EN, JP, FR, ES, IT, KR, CN, PT)

### 🌐 Multi-Blockchain Support
- **12+ Networks**: Ethereum, Bitcoin, BSC, Polygon, Arbitrum, Optimism, Avalanche, Fantom, Litecoin, Dogecoin, Bitcoin Cash, Cardano
- **Multiple Address Types**: Legacy (P2PKH), SegWit (P2SH), Native SegWit (P2WPKH), Taproot (P2TR)
- **EVM + Bitcoin Ecosystems**: Full support for both major blockchain families
- **Real-time APIs**: Live balance checking via blockchain explorers

### 🎨 Modern Qt6 Interface
- **Professional GUI**: Native Qt6 widgets with smooth animations
- **Tab-based Navigation**: Scanner, AI Recovery, Forensics, Analytics, Settings
- **Multiple Themes**: Dark, Light, Ocean Blue, Matrix Green, Royal Purple
- **Responsive Design**: Optimized for various screen sizes
- **Real-time Progress**: Live updates and status indicators

### 🛡️ Enterprise Security
- **AES-256 Encryption**: Military-grade protection for local data
- **Secure Memory**: Automatic clearing of sensitive data
- **Environment Variables**: No hardcoded API keys
- **Offline Capable**: All core features work without internet
- **Audit Logging**: Complete action tracking (optional)

### 📊 Advanced Analytics
- **SQLite Database**: Persistent storage of scan results
- **Historical Tracking**: Long-term success metrics
- **Performance Metrics**: Detailed statistics and reports
- **Export Functions**: CSV, Excel, PDF report generation

### 🔬 Forensic Analysis
- **File Scanner**: Deep scanning of files and directories
- **Pattern Matching**: Advanced regex-based seed detection
- **Signature Recognition**: Identify wallet files by signature
- **Kali Tools Integration**: Binwalk, Foremost, Strings (optional)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Qt6 libraries (installed automatically)
- Linux, macOS, or Windows

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/swisscomfort/ultimate-wallet-recovery-qt6.git
cd ultimate-wallet-recovery-qt6

# 2. Create virtual environment
python -m venv wallet-recovery-env
source wallet-recovery-env/bin/activate  # Linux/Mac
# wallet-recovery-env\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements_qt6.txt

# 4. Configure API keys (optional, for balance checking)
cp .env.example .env
nano .env  # Add your API keys
```

### Launch GUI

```bash
# Start the Qt6 GUI
python launcher.py
```

### Alternative: CLI Scanner

```bash
# Scan files/directories from command line
python scan_runner.py --path /path/to/scan --mode deep
```

---

## 📖 Documentation

### User Guides (German)
- **[Installation](hilfe/01_installation.md)** - Detailed setup instructions
- **[Quick Start](hilfe/02_schnellstart.md)** - Get started in 5 minutes
- **[User Interface](hilfe/03_benutzeroberflaeche.md)** - GUI navigation guide
- **[Troubleshooting](hilfe/13_haeufige_probleme.md)** - Common issues and solutions
- **[Glossary](hilfe/18_glossar.md)** - Technical terms explained

### Technical Documentation
- **[Architecture](docs/ultimate_roadmap.md)** - System design and roadmap
- **[API Reference](docs/user_guide.md)** - Developer documentation
- **[Security Guide](SECURITY.md)** - Security best practices
- **[Legal Disclaimer](DISCLAIMER.md)** - Terms of use and warnings

---

## 🏗️ Project Structure

```
ultimate-wallet-recovery-qt6/
├── src/
│   ├── core/                    # Core business logic (GUI-independent)
│   │   ├── blockchain/          # Blockchain handlers, networks, derivation
│   │   ├── ai/                  # AI recovery engine
│   │   ├── storage/             # Database management
│   │   ├── config_manager.py   # Configuration & API keys
│   │   └── translations.py     # Localization system
│   │
│   ├── gui/                     # Qt6 GUI layer
│   │   ├── main_window.py      # Main application window
│   │   └── widgets/            # Modular UI widgets
│   │       ├── scanner_widget.py        # Wallet scanner
│   │       └── file_manager_dialog.py   # File selection
│   │
│   └── legacy/                  # Archived Tkinter GUI
│
├── hilfe/                       # German documentation
├── docs/                        # Technical documentation
├── templates/                   # HTML templates
│
├── launcher.py                  # Main launcher
├── scan_runner.py              # CLI scanner
├── config.json                 # Network configurations
├── requirements_qt6.txt        # Python dependencies
│
├── LICENSE                     # MIT License
├── SECURITY.md                 # Security policy
├── DISCLAIMER.md               # Legal warnings
└── README.md                   # This file
```

---

## 🔐 Security

### Security Features

- ✅ **Local Processing**: Seed phrases never leave your device
- ✅ **Encrypted Storage**: AES-256 encryption for database
- ✅ **Secure Memory**: Sensitive data cleared after use
- ✅ **Open Source**: Full transparency for auditing
- ✅ **No Telemetry**: No data collection or tracking

### Best Practices

```bash
# Recommended: Use on air-gapped system
# 1. Install dependencies on connected system
# 2. Transfer to offline system
# 3. Run recovery offline
# 4. Export results via USB

# Verify file integrity
sha256sum launcher.py

# Use strong encryption password
# Set in config.json or .env file
```

### Reporting Vulnerabilities

Please report security issues responsibly:
- **DO NOT** open public GitHub issues
- Email repository maintainer directly
- See [SECURITY.md](SECURITY.md) for full policy

---

## 🛠️ Configuration

### API Keys (Optional)

For real-time balance checking, add API keys to `.env`:

```bash
# Blockchain Explorers
ETHERSCAN_API_KEY=your_key_here
BSCSCAN_API_KEY=your_key_here
POLYGONSCAN_API_KEY=your_key_here
# ... see .env.example for full list
```

### Supported Networks

Configure networks in `config.json`:

| Network | Symbol | Type | Derivation Paths |
|---------|--------|------|------------------|
| Ethereum | ETH | EVM | BIP44 (m/44'/60'/0'/0) |
| Bitcoin | BTC | Bitcoin | BIP44/49/84/86 |
| BNB Chain | BNB | EVM | BIP44 (m/44'/714'/0'/0) |
| Polygon | MATIC | EVM | BIP44 (m/44'/966'/0'/0) |
| Arbitrum | ARB | EVM | BIP44 (m/44'/60'/0'/0) |
| Optimism | OP | EVM | BIP44 (m/44'/60'/0'/0) |
| Avalanche | AVAX | EVM | BIP44 (m/44'/9000'/0'/0) |
| Fantom | FTM | EVM | BIP44 (m/44'/60'/0'/0) |
| Litecoin | LTC | Bitcoin | BIP44/49/84 |
| Dogecoin | DOGE | Bitcoin | BIP44 |
| Bitcoin Cash | BCH | Bitcoin | BIP44 |
| Cardano | ADA | Cardano | BIP44 (m/44'/1815'/0'/0) |

---

## 🖼️ Screenshots

<div align="center">

### Main Scanner Interface
*Coming soon: 4 scanning modes - Seed Phrase, Private Key, AI Recovery, File Scanner*

### AI Recovery Engine
*Coming soon: Intelligent seed reconstruction with fuzzy matching*

### Analytics Dashboard
*Coming soon: Comprehensive statistics and historical data*

</div>

> **Note**: GUI is under active development (Qt6 migration in progress). Screenshots will be added upon completion.

---

## 🧪 Development Status

### ✅ Completed
- ✅ Core blockchain modules (async handlers, derivation)
- ✅ AI recovery engine (fuzzy matching, pattern recognition)
- ✅ Configuration management (encrypted, environment-based)
- ✅ Database storage (SQLite with encryption)
- ✅ Scanner widget (4 modes: seed, key, AI, file)
- ✅ German localization system

### 🔄 In Progress
- 🔄 Qt6 GUI widgets (40% complete)
- 🔄 Forensic analysis widget
- 🔄 Analytics dashboard widget
- 🔄 Settings & configuration widget

### 📋 Planned
- 📋 Unit tests & CI/CD pipeline
- 📋 Export formats (PDF, Excel)
- 📋 Multi-language UI (currently German)
- 📋 Hardware wallet support
- 📋 Batch processing improvements

See [docs/ultimate_roadmap.md](docs/ultimate_roadmap.md) for full roadmap.

---

## 🤝 Contributing

Contributions are welcome! This project needs help with:

- 🎨 Qt6 widget development
- 🧪 Unit testing
- 📚 Documentation improvements
- 🌍 Translations (English UI needed!)
- 🔒 Security auditing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone and setup
git clone https://github.com/swisscomfort/ultimate-wallet-recovery-qt6.git
cd ultimate-wallet-recovery-qt6
python -m venv dev-env
source dev-env/bin/activate

# Install dev dependencies
pip install -r requirements_qt6.txt

# Run tests (when available)
# pytest tests/

# Test individual widgets
python src/gui/widgets/scanner_widget.py
```

---

## 📜 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file.

**Important**: The MIT License provides the software "as is" without warranty. See [DISCLAIMER.md](DISCLAIMER.md) for full legal terms.

---

## 🙏 Acknowledgments

### Technologies
- **PyQt6**: Modern cross-platform GUI framework
- **bip-utils**: BIP39/44 implementation
- **bitcoinlib**: Bitcoin library for Python
- **cryptography**: Cryptographic recipes and primitives

### Inspiration
- BIP39/44/49/84/86 specifications
- Open-source crypto community
- Security researchers and ethical hackers

### Warning
This tool is for **legitimate wallet recovery only**. Unauthorized access to cryptocurrency wallets is illegal. The developers assume no responsibility for misuse.

---

## 📞 Support

### Community
- **Issues**: [GitHub Issues](https://github.com/swisscomfort/ultimate-wallet-recovery-qt6/issues)
- **Discussions**: [GitHub Discussions](https://github.com/swisscomfort/ultimate-wallet-recovery-qt6/discussions)

### Important
- ❌ We **cannot** help recover wallets without proper seed phrases
- ❌ We **do not** provide financial or investment advice
- ❌ We **cannot** bypass security on locked wallets
- ✅ We **can** help with software bugs and feature requests

---

## ⭐ Star History

If this project helped you recover your wallet, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting features
- 🤝 Contributing code

---

<div align="center">

**Made with ❤️ by the crypto recovery community**

[Report Bug](https://github.com/swisscomfort/ultimate-wallet-recovery-qt6/issues) • [Request Feature](https://github.com/swisscomfort/ultimate-wallet-recovery-qt6/issues) • [Read Docs](docs/)

</div>
