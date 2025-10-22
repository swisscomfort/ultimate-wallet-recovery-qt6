# Häufige Probleme & Lösungen (FAQ)

## 🔍 Scan-Probleme

### Problem: "Scan läuft bereits!"

**Symptom:** Button bleibt inaktiv, Warnung erscheint

**Ursache:** Ein Scan ist bereits im Gange

**Lösung:**
1. Warten bis aktueller Scan fertig ist
2. Oder: Button "⏹️ Stopp" klicken
3. Dann neuen Scan starten

### Problem: "Bitte Seed Phrase, Private Key oder KI-Wiederherstellung angeben!"

**Symptom:** Scan startet nicht

**Ursache:** Keine Eingabe in einem der Felder

**Lösung:**
1. **Entweder** Seed Phrase eingeben (Tab 1)
2. **Oder** Private Key eingeben (Tab 2)
3. **Oder** KI-Wiederherstellung nutzen (Tab 3)

### Problem: "Bitte mindestens ein Netzwerk auswählen!"

**Symptom:** Scan startet nicht trotz Eingabe

**Ursache:** Keine Netzwerk-Checkbox aktiviert

**Lösung:**
1. Mindestens **eine** Checkbox aktivieren (z.B. ETH)
2. Oder: "Alle auswählen" Button klicken (falls vorhanden)

### Problem: Scan dauert ewig

**Symptom:** Fortschrittsbalken bewegt sich kaum

**Ursache:** 
- Zu viele Netzwerke ausgewählt
- Langsame Internet-Verbindung
- API-Rate-Limits erreicht

**Lösung:**
```
✅ Kurzfristig:
- Reduzieren Sie Netzwerk-Auswahl auf 2-3
- Verringern Sie Adress-Index-Bereich (0-20 statt 0-100)
- Prüfen Sie Internet-Verbindung

✅ Langfristig:
- Premium API-Keys besorgen (höhere Rate-Limits)
- Nur relevante Netzwerke scannen
- Scans zeitlich verteilen
```

## 🔑 Seed Phrase Probleme

### Problem: "Ungültige Seed Phrase!"

**Symptom:** Fehlermeldung bei Scan-Start

**Häufigste Ursachen:**

#### 1. Falsche Wortanzahl
```
❌ Falsch: 13 Wörter
✅ Richtig: 12, 15, 18 oder 24 Wörter
```

#### 2. Ungültige Wörter
```
❌ Falsch: abandonn (Tippfehler)
✅ Richtig: abandon
```
**Lösung:** Nutzen Sie nur offizielle BIP39-Wörter

#### 3. Falsche Trennung
```
❌ Falsch: abandon,abandon,abandon (Kommas)
✅ Richtig: abandon abandon abandon (Leerzeichen)
```

#### 4. Groß-/Kleinschreibung
```
❌ Falsch: Abandon Abandon Abandon
✅ Richtig: abandon abandon abandon
```

### Problem: Seed gültig, aber keine Wallets gefunden

**Symptom:** Scan erfolgreich, aber alle Guthaben = 0

**Mögliche Ursachen:**

1. **Falscher Derivation Path**
   ```
   ✅ Versuchen Sie:
   - Standard (BIP44)
   - Bitcoin SegWit (BIP49)
   - Bitcoin Native SegWit (BIP84)
   - Bitcoin Taproot (BIP86)
   ```

2. **BIP39 Passphrase vergessen**
   ```
   Seed ohne Passphrase ≠ Seed mit Passphrase
   
   Wenn Sie eine Passphrase verwendet haben:
   - Geben Sie sie im Passphrase-Feld ein
   - Auch leere Passphrase versuchen ("")
   ```

3. **Falsche Netzwerke**
   ```
   Ihre Wallets könnten auf anderen Chains sein:
   - Aktivieren Sie mehr Netzwerke
   - Oder: "Alle Netzwerke" scannen
   ```

4. **Höherer Adress-Index**
   ```
   Standard: Adressen 0-20
   
   Wenn Sie viele Adressen generiert haben:
   - Erhöhen Sie Index-Bereich (z.B. 0-100)
   ```

## 💻 API & Verbindungs-Probleme

### Problem: "API-Request fehlgeschlagen"

**Symptom:** Fehler während Scan, einzelne Netzwerke übersprungen

**Ursache 1: Fehlende API-Keys**
```bash
✅ Lösung:
1. Öffnen Sie .env Datei
2. Fügen Sie API-Keys hinzu:
   ETHERSCAN_API_KEY=IHR_KEY_HIER
   BSCSCAN_API_KEY=IHR_KEY_HIER
3. Anwendung neu starten
```

**Ursache 2: Rate-Limit überschritten**
```
❌ Fehler: "Max rate limit reached"

✅ Lösung:
- 1-2 Minuten warten
- Premium API-Key besorgen (5 Anfragen/Sek statt 1)
- Scan mit weniger Netzwerken wiederholen
```

**Ursache 3: Ungültiger API-Key**
```
❌ Fehler: "Invalid API Key"

✅ Lösung:
1. API-Key auf Explorer-Website prüfen
2. Korrekt in .env kopieren (keine Leerzeichen!)
3. Anwendung neu starten
```

### Problem: "No internet connection"

**Symptom:** Alle Netzwerk-Scans schlagen fehl

**Lösung:**
```
1. Internet-Verbindung prüfen:
   ping google.com

2. Firewall-Einstellungen prüfen

3. VPN deaktivieren (falls aktiviert)

4. Proxy-Einstellungen prüfen

5. Offline-Modus verwenden:
   - Nur Adress-Generierung
   - Forensische Analyse
```

## 🧠 KI-Wiederherstellungs-Probleme

### Problem: "Keine Vorschläge gefunden"

**Symptom:** KI findet keine passenden Wörter

**Ursache:** Zu viele fehlende Wörter

**Lösung:**
```
❌ Zu schwer: ? ? ? abandon ? ? ? abandon ? ? ? ?

✅ Machbar: abandon ? abandon abandon ? abandon abandon abandon ? abandon abandon about

Regel: Maximal 30% fehlende Wörter
- 12 Wörter: max 3-4 fehlen
- 24 Wörter: max 7-8 fehlen
```

### Problem: KI-Rekonstruktion dauert sehr lange

**Symptom:** "KI rekonstruiert..." läuft minutenlang

**Ursache:** Zu viele Kombinationen zu prüfen

**Lösung:**
```
Reduzieren Sie Komplexität:

1. Geben Sie mehr bekannte Wörter an
2. Nutzen Sie Position-Hints (wenn Sie wissen, wo Wörter stehen)
3. Begrenzen Sie Wortvorschläge:
   Einstellungen → KI → Max Suggestions: 5 (statt 10)
```

## 💾 Datenbank-Probleme

### Problem: "Database locked"

**Symptom:** Kann Ergebnisse nicht speichern

**Ursache:** Mehrere Instanzen greifen auf DB zu

**Lösung:**
```bash
1. Alle Instanzen schließen
2. Prozesse prüfen:
   ps aux | grep wallet_recovery
   
3. Ggf. beenden:
   kill -9 <PID>
   
4. DB-Datei prüfen:
   ls -la wallet_recovery.db
   
5. Neu starten
```

### Problem: "Corrupted database"

**Symptom:** App startet nicht, DB-Fehler

**Lösung:**
```bash
1. Backup erstellen:
   cp wallet_recovery.db wallet_recovery.db.backup

2. DB reparieren:
   sqlite3 wallet_recovery.db "PRAGMA integrity_check;"

3. Wenn irreparabel, neu erstellen:
   rm wallet_recovery.db
   python launcher.py --mode standard
   # DB wird automatisch neu angelegt
```

## 🖥️ GUI-Probleme

### Problem: GUI startet nicht

**Symptom:** Fehlermeldung beim Start

**Ursache 1: Tkinter nicht installiert**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (via Homebrew)
brew install python-tk

# Dann neu starten
python launcher.py --mode standard
```

**Ursache 2: Display-Problem (Linux)**
```bash
# DISPLAY Variable setzen
export DISPLAY=:0

# Oder X11 Forwarding aktivieren
ssh -X user@host
```

**Ursache 3: Qt6 Probleme**
```bash
# Fallback auf Tkinter-GUI
python src/wallet_recovery_ultimate.py

# Oder Qt6 reparieren
pip install --upgrade PyQt6
```

### Problem: GUI friert ein

**Symptom:** Fenster reagiert nicht mehr

**Lösung:**
```
1. Nicht schließen! Scan läuft möglicherweise
2. Warten Sie 1-2 Minuten
3. Prüfen Sie Prozess-Last:
   - Task Manager (Windows)
   - Activity Monitor (macOS)
   - top/htop (Linux)
   
4. Wenn wirklich eingefroren:
   - Force-Close
   - Datenbank-Lock entfernen (siehe oben)
   - Neu starten
```

## 📂 Forensische Analyse-Probleme

### Problem: "Permission denied" beim Scannen

**Symptom:** Kann Ordner/Laufwerk nicht scannen

**Lösung:**
```bash
# Linux/macOS: Mit sudo ausführen
sudo python scan_runner.py --path /media/disk

# Windows: Als Administrator ausführen
# Rechtsklick → Als Administrator ausführen

# ODER: Berechtigungen ändern
sudo chmod -R 755 /pfad/zum/ordner
```

### Problem: Forensik-Scan findet nichts

**Symptom:** Scan abgeschlossen, 0 Ergebnisse

**Ursachen:**

1. **Falscher Scan-Modus**
   ```bash
   # Zu oberflächlich
   ❌ python scan_runner.py --mode quick
   
   # Besser
   ✅ python scan_runner.py --mode deep
   ```

2. **Dateityp-Filter zu streng**
   ```bash
   # Alle Dateitypen scannen
   python scan_runner.py --path /pfad --extensions all
   ```

3. **Verschlüsselte Container**
   ```
   Verschlüsselte Dateien können nicht gescannt werden
   
   ✅ Zuerst entschlüsseln:
   - BitLocker
   - VeraCrypt
   - LUKS
   
   Dann scannen
   ```

## ⚙️ Performance-Probleme

### Problem: Hohe CPU-Auslastung

**Symptom:** Lüfter laut, System langsam

**Lösung:**
```
1. Reduzieren Sie Parallelität:
   Einstellungen → Performance → Threads: 2 (statt 4)

2. Adress-Bereich verkleinern:
   0-20 statt 0-100

3. Weniger Netzwerke gleichzeitig

4. Background-Prozesse schließen
```

### Problem: Hoher RAM-Verbrauch

**Symptom:** 4+ GB RAM-Nutzung

**Lösung:**
```
1. Cache leeren:
   Einstellungen → Erweitert → Cache leeren

2. Scan-Historie begrenzen:
   Einstellungen → DB → Max Einträge: 1000

3. Forensik-Puffer reduzieren:
   --buffer-size 512 (statt 2048)
```

## 🔐 Sicherheits-Probleme

### Problem: "Warning: Unencrypted database"

**Symptom:** Warnung beim Start

**Lösung:**
```
1. Verschlüsselung aktivieren:
   Einstellungen → Sicherheit → Datenbank verschlüsseln

2. Master-Passwort setzen

3. DB wird neu verschlüsselt

⚠️ Wichtig: Passwort nicht vergessen!
```

### Problem: Seed wird in Logs gespeichert

**Symptom:** Seed in Textdateien sichtbar

**Lösung:**
```
1. Debug-Modus deaktivieren:
   python launcher.py  # OHNE --debug

2. Logs löschen:
   rm *.log
   rm debug_*.txt

3. Secure-Mode aktivieren:
   python launcher.py --debug-mode safe
   # Keine echten Daten in Logs
```

## 📱 Platform-spezifische Probleme

### Windows

**Problem:** "MSVCP140.dll fehlt"
```
Lösung: Visual C++ Redistributable installieren
https://aka.ms/vs/17/release/vc_redist.x64.exe
```

**Problem:** PowerShell Execution Policy
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### macOS

**Problem:** "App von unidentifiziertem Entwickler"
```bash
# Sicherheitseinstellungen umgehen
xattr -cr /pfad/zu/ultimate-wallet-recovery-main
```

**Problem:** Python nicht gefunden
```bash
# Python 3 explizit verwenden
python3 launcher.py --mode standard
```

### Linux

**Problem:** "libQt6Core.so.6 not found"
```bash
# Qt6 Bibliotheken installieren
sudo apt-get install libqt6core6 libqt6widgets6

# Fedora
sudo dnf install qt6-qtbase
```

## 🆘 Wenn nichts funktioniert

### Nuclear Option: Kompletter Reset

```bash
1. Backup erstellen:
   cp -r ultimate-wallet-recovery-main backup_recovery

2. Datenbank sichern:
   cp wallet_recovery.db wallet_recovery.db.backup

3. Komplette Neuinstallation:
   rm -rf wallet-recovery-env
   python3 -m venv wallet-recovery-env
   source wallet-recovery-env/bin/activate
   pip install -r requirements_integrated.txt

4. .env neu konfigurieren:
   cp .env.example .env
   # API-Keys einfügen

5. Neu starten:
   python launcher.py --mode standard

6. Alte DB importieren (falls nötig):
   cp wallet_recovery.db.backup wallet_recovery.db
```

## 📞 Support erhalten

Wenn alle Lösungen fehlschlagen:

1. **Logs sammeln:**
   ```bash
   # Debug-Infos generieren
   python launcher.py --debug-mode trace
   # Erzeugt debug_trace.jsonl
   ```

2. **Issue erstellen:**
   - GitHub: [Repository Issues](https://github.com/...)
   - Logs anhängen
   - Fehlermeldung kopieren
   - System-Info angeben (OS, Python-Version)

3. **Community fragen:**
   - Discord/Forum
   - Keine sensiblen Daten teilen!

## Nächste Schritte

- ➡️ [Fehlermeldungen erklärt](14_fehlermeldungen.md)
- ➡️ [Debug-Modi nutzen](15_debug_modi.md)
- ➡️ [Sicherheits-Best-Practices](10_sicherheit.md)
