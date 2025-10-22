# Contributing to Ultimate Wallet Recovery Tool

First off, thank you for considering contributing to Ultimate Wallet Recovery Tool! 🎉

This project aims to help people recover their cryptocurrency wallets legitimately. Your contributions can make a real difference.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## 🤝 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title** and description
- **Steps to reproduce** the problem
- **Expected behavior** vs actual behavior
- **Environment details** (OS, Python version, Qt version)
- **Screenshots** if applicable
- **Error messages** and stack traces

**Use the bug report template** when creating issues.

### 💡 Suggesting Features

Feature suggestions are tracked as GitHub issues. When suggesting a feature:

- **Use a clear title** and detailed description
- **Explain the use case** - why is this feature needed?
- **Provide examples** of how it would work
- **Consider alternatives** you've thought about

**Use the feature request template** when creating issues.

### 🔒 Security Issues

**DO NOT** report security vulnerabilities in public issues. See [SECURITY.md](SECURITY.md) for responsible disclosure process.

### 🎨 Contributing Code

We welcome code contributions! Areas needing help:

- **Qt6 Widgets**: Complete the GUI migration
- **Unit Tests**: Improve test coverage
- **Documentation**: API docs, user guides, translations
- **Bug Fixes**: Check open issues
- **Performance**: Optimize slow operations

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.11+
- Git
- Virtual environment tool
- Qt6 development libraries

### Setup Steps

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/ultimate-wallet-recovery-qt6.git
cd ultimate-wallet-recovery-qt6

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL-OWNER/ultimate-wallet-recovery-qt6.git

# 4. Create virtual environment
python -m venv dev-env
source dev-env/bin/activate  # Linux/Mac
# dev-env\Scripts\activate  # Windows

# 5. Install dependencies
pip install -r requirements_qt6.txt

# 6. Install development tools (optional)
pip install pytest black flake8 mypy

# 7. Create .env file
cp .env.example .env
# Edit .env with test API keys (optional)

# 8. Test the installation
python launcher.py
```

### Project Structure

```
src/
├── core/           # Business logic (GUI-independent)
│   ├── blockchain/ # Blockchain handlers
│   ├── ai/         # AI recovery engine
│   └── storage/    # Database management
│
├── gui/            # Qt6 interface
│   ├── widgets/    # Reusable widgets
│   └── dialogs/    # Dialog windows
│
└── legacy/         # Archived code (do not modify)
```

---

## 💻 Coding Standards

### Python Style Guide

We follow **PEP 8** with some exceptions:

```python
# ✅ Good
def scan_wallet(seed_phrase: str, networks: List[NetworkConfig]) -> List[ScanResult]:
    """
    Scan multiple blockchain networks for wallet activity.
    
    Args:
        seed_phrase: BIP39 seed phrase
        networks: List of network configurations
        
    Returns:
        List of scan results with balances and transactions
    """
    results = []
    for network in networks:
        result = _scan_single_network(seed_phrase, network)
        results.append(result)
    return results

# ❌ Bad - no type hints, no docstring
def scan_wallet(seed, nets):
    r = []
    for n in nets:
        r.append(_scan_single_network(seed, n))
    return r
```

### Key Principles

1. **Type Hints**: Always use type hints
2. **Docstrings**: All public functions/classes need docstrings
3. **Comments**: Explain "why", not "what"
4. **Naming**: Descriptive names (no single letters except loops)
5. **Line Length**: Max 100 characters (not strict 79)

### Code Formatting

```bash
# Format code with black
black src/

# Check style with flake8
flake8 src/ --max-line-length=100

# Type checking with mypy
mypy src/
```

### Qt6 Widget Guidelines

```python
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal

class MyWidget(QWidget):
    """Widget description."""
    
    # Define signals at class level
    data_changed = pyqtSignal(dict)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize UI components."""
        # Build UI here
        pass
        
    def on_action(self):
        """Handle user action."""
        # Emit signals for main window
        self.data_changed.emit({"status": "success"})
```

---

## 📝 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic change)
- `refactor`: Code restructuring
- `test`: Adding/modifying tests
- `chore`: Maintenance tasks

**Examples**:

```
feat(scanner): add Bitcoin Taproot support

Implement BIP86 derivation for Taproot addresses.
Includes both key-path and script-path spending.

Closes #123
```

```
fix(ai): correct fuzzy matching threshold

Previous threshold was too strict, causing valid
matches to be rejected. Adjusted to 0.85.

Fixes #456
```

### Commit Best Practices

- ✅ One logical change per commit
- ✅ Write clear, concise messages
- ✅ Reference issues with `#123`
- ✅ Use present tense ("add" not "added")
- ❌ Don't mix unrelated changes
- ❌ Don't commit commented-out code

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update from upstream**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Test your changes**:
   ```bash
   # Run tests (if available)
   pytest tests/
   
   # Test GUI manually
   python launcher.py
   ```

3. **Format code**:
   ```bash
   black src/
   flake8 src/ --max-line-length=100
   ```

4. **Update documentation**:
   - Add docstrings to new functions
   - Update README if needed
   - Add comments for complex logic

### Creating Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/my-feature
   ```

2. **Open PR on GitHub** with:
   - Clear title and description
   - Reference related issues
   - Screenshots if UI changes
   - Checklist of changes

3. **Use PR template** (auto-loaded)

### PR Template Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated (if applicable)
- [ ] Tested on local machine

### Review Process

1. Maintainers will review within 7 days
2. Address review comments
3. Push updates to same branch
4. Request re-review when ready
5. Maintainer will merge when approved

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_core.py

# Run with coverage
pytest --cov=src tests/
```

### Writing Tests

```python
import pytest
from src.core.blockchain.handler import BlockchainHandler

def test_seed_validation():
    """Test seed phrase validation."""
    handler = BlockchainHandler()
    
    # Valid seed
    assert handler.validate_seed("abandon abandon ... art")
    
    # Invalid seed
    assert not handler.validate_seed("invalid words here")
    
def test_address_derivation():
    """Test BIP44 address derivation."""
    handler = BlockchainHandler()
    seed = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    
    address = handler.derive_address(seed, path="m/44'/60'/0'/0/0")
    assert address.startswith("0x")
```

### Test Guidelines

- Test both success and failure cases
- Use descriptive test names
- One assertion per test (when possible)
- Mock external API calls
- Don't test GUI directly (test logic)

---

## 📚 Documentation

### Code Documentation

```python
def derive_address(seed: str, path: str, network: NetworkConfig) -> str:
    """
    Derive blockchain address from seed phrase.
    
    Implements BIP44/49/84/86 standards for address derivation.
    Supports both EVM and Bitcoin-style networks.
    
    Args:
        seed: Valid BIP39 mnemonic seed phrase (12-24 words)
        path: Derivation path (e.g., "m/44'/60'/0'/0/0")
        network: Network configuration object
        
    Returns:
        Derived address as string (format depends on network)
        
    Raises:
        ValueError: If seed is invalid or path malformed
        NetworkError: If network configuration is incomplete
        
    Example:
        >>> seed = "abandon abandon ... about"
        >>> path = "m/44'/60'/0'/0/0"
        >>> address = derive_address(seed, path, ETH_CONFIG)
        >>> print(address)
        '0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb'
    """
    pass
```

### User Documentation

- German docs in `hilfe/`
- English docs in `docs/`
- Update both when adding features
- Include examples and screenshots

---

## 🌍 Translations

We need help translating the UI to English and other languages!

### Translation System

```python
from core.translations import t, set_language

# In Python code
button_text = t('btn_start_scan')  # Returns "🚀 SCAN STARTEN" in German

# To add English:
# Edit src/core/translations.py
# Add 'en' translations alongside 'de'
```

### Translation Guidelines

- Keep technical terms consistent
- Preserve placeholders like `{network}`
- Match emoji usage
- Test in actual GUI

---

## ❓ Questions?

- **General**: Open a GitHub Discussion
- **Bugs**: Create an issue with bug template
- **Security**: See [SECURITY.md](SECURITY.md)
- **Chat**: (Add Discord/Telegram if available)

---

## 🎉 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Mentioned in annual acknowledgments

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing!** 🚀

Every contribution, no matter how small, helps make wallet recovery more accessible and secure.
