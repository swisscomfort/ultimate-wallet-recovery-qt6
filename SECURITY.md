# Security Policy

## 🛡️ Security Overview

Ultimate Wallet Recovery Tool handles highly sensitive cryptographic data. We take security seriously and appreciate the community's help in identifying vulnerabilities.

## 🔒 Security Features

- **AES-256 Encryption**: Military-grade encryption for local data storage
- **Secure Memory Management**: Sensitive data is securely erased from memory
- **Environment Variables**: API keys and secrets are never hardcoded
- **No Network Transmission**: Seed phrases and private keys never leave your device
- **Open Source**: Full transparency for security auditing

## 🚨 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 4.x     | ✅ Active support  |
| 3.x     | ⚠️ Legacy support  |
| < 3.0   | ❌ Not supported   |

## 📢 Reporting a Vulnerability

**Please DO NOT report security vulnerabilities through public GitHub issues.**

### Preferred Reporting Method

1. **Email**: Send details to the repository owner
2. **Include**: 
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)
3. **Response Time**: We aim to respond within 48 hours

### What to Expect

- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 7 days
- **Fix Timeline**: Critical issues within 14 days, others within 30 days
- **Credit**: Security researchers will be credited (unless anonymity is requested)

## ⚠️ Security Best Practices for Users

### Critical Warnings

1. ⚠️ **NEVER share your seed phrases or private keys with anyone**
2. ⚠️ **NEVER use this tool on untrusted computers**
3. ⚠️ **ALWAYS verify you're running the official release**
4. ⚠️ **ALWAYS use the tool offline when possible**
5. ⚠️ **ALWAYS keep your system updated and secure**

### Recommended Setup

```bash
# Use a dedicated air-gapped machine
# Verify file checksums before running
sha256sum launcher.py

# Use a dedicated Python environment
python -m venv secure-env
source secure-env/bin/activate

# Keep API keys in .env file (never commit)
cp .env.example .env
# Edit .env with your keys
```

### Data Protection

- **Encryption**: Enable encryption in settings
- **Backups**: Store backups in encrypted containers
- **Logs**: Regularly review and clean log files
- **Database**: Encrypt the SQLite database with a strong password

## 🔐 Cryptographic Implementation

### Key Derivation
- **Algorithm**: PBKDF2-HMAC-SHA256
- **Iterations**: 100,000+
- **Salt**: Randomly generated per installation

### Encryption
- **Algorithm**: AES-256-GCM
- **Mode**: Authenticated encryption
- **Libraries**: PyCryptodome, Python Cryptography

### Seed Phrase Generation
- **Standard**: BIP39/BIP44/BIP49/BIP84/BIP86
- **Entropy**: System CSPRNG (Cryptographically Secure Pseudo-Random Number Generator)
- **Libraries**: bip-utils, bitcoinlib

## 🔍 Security Auditing

### Self-Audit Checklist

- [ ] API keys in `.env` file (not hardcoded)
- [ ] Database encryption enabled
- [ ] Secure deletion of sensitive variables
- [ ] No plain-text seed storage
- [ ] HTTPS for all external API calls
- [ ] Input validation on user data
- [ ] Rate limiting on API requests

### Third-Party Audits

We welcome security audits from the community. Please contact us if you're interested in conducting a formal security review.

## 🏆 Hall of Fame

We recognize security researchers who responsibly disclose vulnerabilities:

<!-- Security researchers will be listed here -->
*No vulnerabilities reported yet - help us keep it secure!*

## 📚 Additional Resources

- [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [BIP39 Specification](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
- [Python Cryptography Best Practices](https://cryptography.io/en/latest/)

## ⚖️ Legal Notice

This tool is designed for **legitimate wallet recovery only**. Any misuse for unauthorized access is strictly prohibited and illegal. See [DISCLAIMER.md](DISCLAIMER.md) for full legal terms.

---

**Last Updated**: October 2025
