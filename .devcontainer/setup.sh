#!/bin/bash
# Codespaces Setup Script - Automatische Initialisierung

echo "🚀 Starting Ultimate Wallet Recovery - Qt6 Setup..."

# Python Virtual Environment erstellen
echo "📦 Creating virtual environment..."
python3 -m venv wallet-recovery-env

# Aktivieren
source wallet-recovery-env/bin/activate

# Pip upgraden
echo "⬆️ Upgrading pip..."
pip install --upgrade pip setuptools wheel

# Dependencies installieren
echo "📥 Installing dependencies..."
pip install -r requirements_qt6.txt

# .env Datei erstellen falls nicht vorhanden
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️ WICHTIG: Bitte API Keys in .env eintragen!"
fi

# SQLite Database initialisieren
echo "💾 Initializing database..."
python3 -c "from src.core.storage.database import DatabaseManager; db = DatabaseManager(); print('✅ Database initialized')"

# Git Config
echo "🔧 Configuring git..."
git config pull.rebase false

# Erfolgsmeldung
echo "
✅ Setup abgeschlossen!

📋 Nächste Schritte:
1. API Keys in .env eintragen: code .env
2. Migration Status prüfen: code MIGRATION_STATUS.md
3. Entwicklung starten: code src/gui/main_window.py

🎯 Quick Commands:
- source wallet-recovery-env/bin/activate  # Virtual env aktivieren
- python launcher_qt6.py                   # GUI starten (offscreen)
- pytest tests/ -v                         # Tests ausführen
- code MIGRATION_STATUS.md                 # Status checken

📚 Dokumentation:
- .github/CODESPACES_GUIDE.md              # Vollständige Anleitung
- .github/copilot-instructions.md          # Copilot Guidelines
- MIGRATION_PLAN.md                        # 10-Wochen Roadmap

🚀 Viel Erfolg!
"
