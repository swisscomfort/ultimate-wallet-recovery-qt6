# Ultimate Wallet Recovery Qt6

Experimental Qt6 desktop prototype for inspecting wallet-recovery workflows, BIP39 input, HD-wallet derivation settings, and local wallet-artifact scanning.

> [!CAUTION]
> This repository is not production-ready and has not been independently security-audited. Do not enter a real seed phrase or private key. Use public test vectors or disposable test wallets in an isolated environment. The software cannot bypass wallet security and must only be used on data and wallets you are authorized to inspect.

## Status

**Classification:** experimental product prototype.

The current checkout contains a launchable PyQt6 shell and several core modules, but important workflows are incomplete or simulated. It should be treated as a development and security-research project, not as a finished recovery product.

### Present in the repository

- a PyQt6 main window with scanner, AI recovery, forensic, analytics, and settings tabs;
- a functional scanner interface for seed, private-key, damaged-seed, and file inputs;
- configuration objects for 11 blockchain networks;
- BIP39 validation and BIP44/49/84/86 derivation modules based on `bip-utils`;
- asynchronous explorer/CoinGecko client code;
- basic local file-pattern detection in the GUI scanner;
- an SQLite schema for scan results and analytics;
- German UI translation data and project documentation.

### Important limitations

- The GUI blockchain scan currently emits synthetic placeholder addresses, balances, and transaction counts instead of executing the available derivation and explorer code end to end.
- AI recovery is deterministic fuzzy matching, not a trained AI model. Its word-list loader currently falls back to a small, incomplete English list.
- The dedicated AI recovery, forensic, analytics, and settings tabs are placeholders.
- `scan_runner.py` cannot run because the referenced `src.forensic` package is absent.
- CSV import/export, QR scanning, address generation, status checks, and several menu actions are stubs.
- The SQLite database is not encrypted by the current database layer. Secure-memory clearing and complete audit logging are not implemented.
- There is no automated unit-test suite or CI workflow. `test_translations.py` is an executable translation smoke script, not a test framework suite.
- No packaged release artifacts have been published.

## Verified development start

The following path was checked on Linux with Python 3.12 and the dependencies from `requirements_qt6.txt`:

```bash
git clone https://github.com/swisscomfort/ultimate-wallet-recovery-qt6.git
cd ultimate-wallet-recovery-qt6

python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements_qt6.txt
python launcher.py
```

The launcher creates `wallet_recovery.db` in the current working directory. Use only test data.

### Checks

```bash
python -m compileall -q src launcher.py scan_runner.py test_translations.py
python test_translations.py
```

The source compilation and translation smoke script pass in the verified environment. An off-screen launch remained running during a bounded smoke check. The standalone scanner is a known failure until `src.forensic` is implemented or `scan_runner.py` is changed.

## Architecture

```text
launcher.py                    Qt6 application entry point
src/gui/main_window.py         Main window and placeholder workspaces
src/gui/widgets/               Scanner and file-selection widgets
src/core/blockchain/           Network, derivation, and explorer logic
src/core/ai/recovery_engine.py Fuzzy seed-repair prototype
src/core/storage/database.py   Plain SQLite persistence
src/core/config_manager.py     JSON/environment configuration helpers
hilfe/                         German user documentation
docs/                          Additional project documentation and roadmap
```

`src/legacy/` contains the earlier Tkinter implementation. It is not the Qt6 launch path.

## Development priorities

1. Replace simulated scan results with tested integration of the derivation and explorer layers.
2. Add tests for known BIP39 vectors, derivation paths, API error handling, file scanning, and database behavior.
3. Remove or implement placeholder tabs and broken entry points.
4. Define and verify a security model for secret handling, persistence, logs, and offline operation.
5. Add CI, dependency locking, packaging, and signed release artifacts.

The longer-term ideas in [`docs/ultimate_roadmap.md`](docs/ultimate_roadmap.md) are plans, not implemented capabilities.

## Responsible use

- Work only with wallets and files you own or are explicitly authorized to recover.
- Prefer an offline, disposable test system.
- Never paste secrets into bug reports, screenshots, logs, or public issues.
- Review [`SECURITY.md`](SECURITY.md) and [`DISCLAIMER.md`](DISCLAIMER.md) before experimenting.

## License

MIT — see [`LICENSE`](LICENSE). The software is provided without warranty.
