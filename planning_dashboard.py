#!/usr/bin/env python3
"""
Planning Dashboard - Web Interface für Migration Planning
Läuft in Codespaces und zeigt Migration Status + Planning Tools
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
from pathlib import Path
import markdown

app = Flask(__name__)
CORS(app)

# Pfade
BASE_DIR = Path(__file__).parent
MIGRATION_STATUS = BASE_DIR / "MIGRATION_STATUS.md"
MIGRATION_PLAN = BASE_DIR / "MIGRATION_PLAN.md"
COPILOT_INSTRUCTIONS = BASE_DIR / ".github" / "copilot-instructions.md"

@app.route('/')
def index():
    """Hauptseite - Planning Dashboard"""
    return render_template('planning_dashboard.html')

@app.route('/api/migration-status')
def get_migration_status():
    """Lade Migration Status"""
    if MIGRATION_STATUS.exists():
        content = MIGRATION_STATUS.read_text(encoding='utf-8')
        return jsonify({
            'content': content,
            'html': markdown.markdown(content, extensions=['extra', 'codehilite'])
        })
    return jsonify({'error': 'Migration status not found'}), 404

@app.route('/api/migration-plan')
def get_migration_plan():
    """Lade Migration Plan"""
    if MIGRATION_PLAN.exists():
        content = MIGRATION_PLAN.read_text(encoding='utf-8')
        return jsonify({
            'content': content,
            'html': markdown.markdown(content, extensions=['extra', 'codehilite'])
        })
    return jsonify({'error': 'Migration plan not found'}), 404

@app.route('/api/copilot-instructions')
def get_copilot_instructions():
    """Lade Copilot Instructions"""
    if COPILOT_INSTRUCTIONS.exists():
        content = COPILOT_INSTRUCTIONS.read_text(encoding='utf-8')
        return jsonify({
            'content': content,
            'html': markdown.markdown(content, extensions=['extra', 'codehilite'])
        })
    return jsonify({'error': 'Copilot instructions not found'}), 404

@app.route('/api/project-structure')
def get_project_structure():
    """Zeige Projekt-Struktur"""
    def scan_dir(path, max_depth=3, current_depth=0):
        if current_depth >= max_depth:
            return {}
        
        structure = {}
        try:
            for item in sorted(path.iterdir()):
                if item.name.startswith('.') and item.name not in ['.github', '.devcontainer']:
                    continue
                if item.name in ['__pycache__', 'node_modules', 'wallet-recovery-env', 'venv']:
                    continue
                
                if item.is_dir():
                    structure[item.name] = scan_dir(item, max_depth, current_depth + 1)
                else:
                    structure[item.name] = 'file'
        except PermissionError:
            pass
        return structure
    
    structure = scan_dir(BASE_DIR)
    return jsonify(structure)

@app.route('/api/update-status', methods=['POST'])
def update_status():
    """Update Migration Status"""
    data = request.json
    new_content = data.get('content', '')
    
    if MIGRATION_STATUS.exists():
        MIGRATION_STATUS.write_text(new_content, encoding='utf-8')
        return jsonify({'success': True, 'message': 'Status updated'})
    return jsonify({'error': 'Could not update status'}), 500

@app.route('/api/tasks')
def get_tasks():
    """Extrahiere Tasks aus Migration Status"""
    if MIGRATION_STATUS.exists():
        content = MIGRATION_STATUS.read_text(encoding='utf-8')
        tasks = []
        
        for line in content.split('\n'):
            if '- [ ]' in line or '- [x]' in line or '- [✅]' in line:
                done = '[x]' in line or '[✅]' in line
                task_text = line.split(']', 1)[1].strip() if ']' in line else line
                tasks.append({
                    'text': task_text,
                    'done': done
                })
        
        return jsonify({
            'total': len(tasks),
            'completed': sum(1 for t in tasks if t['done']),
            'pending': sum(1 for t in tasks if not t['done']),
            'tasks': tasks
        })
    return jsonify({'error': 'No tasks found'}), 404

if __name__ == '__main__':
    print("""
    
    ╔══════════════════════════════════════════════════════════════╗
    ║  🚀 Ultimate Wallet Recovery - Planning Dashboard           ║
    ║                                                              ║
    ║  Dashboard läuft auf: http://localhost:8080                 ║
    ║                                                              ║
    ║  Features:                                                   ║
    ║  • Migration Status Tracking                                ║
    ║  • Task Overview                                             ║
    ║  • Project Structure Explorer                                ║
    ║  • Documentation Viewer                                      ║
    ║                                                              ║
    ║  Codespaces wird Port 8080 automatisch forwarden!           ║
    ╚══════════════════════════════════════════════════════════════╝
    
    """)
    app.run(host='0.0.0.0', port=8080, debug=True)
