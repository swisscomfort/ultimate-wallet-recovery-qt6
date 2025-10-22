# Glossar - Begriffserklärungen

## A

**Adresse (Address)**  
Eine eindeutige Zeichenfolge, die ein Kryptowährungs-Wallet identifiziert. Ähnlich wie eine Kontonummer.

**Ableitungspfad (Derivation Path)**  
Ein Pfad-Schema (z.B. m/44'/60'/0'/0/0), das bestimmt, wie aus einer Seed Phrase spezifische Private Keys generiert werden.

**API-Key**  
Authentifizierungsschlüssel für Blockchain-Explorer-APIs (z.B. Etherscan). Ermöglicht Zugriff auf Blockchain-Daten.

## B

**BIP32**  
Bitcoin Improvement Proposal 32 - Standard für hierarchische deterministische Wallets (HD Wallets).

**BIP39**  
Standard für mnemonische Seed Phrases. Definiert die 2048 offiziellen Wörter.

**BIP44**  
Standard-Ableitungspfad: m/44'/coin_type'/account'/change/address_index

**BIP49**  
Ableitungspfad für Bitcoin SegWit (P2SH-P2WPKH): m/49'/0'/0'/0/x

**BIP84**  
Ableitungspfad für Bitcoin Native SegWit (P2WPKH): m/84'/0'/0'/0/x

**BIP86**  
Ableitungspfad für Bitcoin Taproot (P2TR): m/86'/0'/0'/0/x

**Blockchain Explorer**  
Website/Service zur Ansicht von Blockchain-Daten (z.B. Etherscan.io, Blockchain.com).

## C

**CHF**  
Schweizer Franken - Standardwährung für Wertanzeigen in dieser Anwendung.

**Coin Type**  
Nummer in Derivation Path, die Kryptowährung identifiziert (z.B. 0=BTC, 60=ETH).

## D

**Derivation (Ableitung)**  
Prozess der Generierung von Private Keys und Adressen aus einer Master Seed.

**Deterministic Wallet**  
Wallet, bei dem alle Keys aus einer einzigen Seed deterministisch abgeleitet werden.

## E

**Encryption (Verschlüsselung)**  
Schutz sensibler Daten durch kryptographische Verfahren (z.B. AES-256).

**EVM (Ethereum Virtual Machine)**  
Laufzeitumgebung für Smart Contracts auf Ethereum und kompatiblen Chains.

**Explorer API**  
Programmierschnittstelle von Blockchain-Explorern für automatisierte Abfragen.

## F

**Faucet**  
Service, der kostenlos kleine Mengen Kryptowährung verteilt (meist für Testnetzwerke).

**Forensische Analyse**  
Systematisches Durchsuchen von Datenträgern nach Wallet-Artefakten.

## G

**Gas**  
Gebühr für Transaktionen auf Ethereum und EVM-kompatiblen Blockchains.

**Guthaben (Balance)**  
Aktueller Coin/Token-Bestand einer Wallet-Adresse.

## H

**HD Wallet (Hierarchical Deterministic)**  
Wallet-System, das strukturiert Keys aus einer Master-Seed ableitet.

**HEX (Hexadezimal)**  
Zahlensystem mit Basis 16 (0-9, A-F). Private Keys werden oft in HEX dargestellt.

**Hot Wallet**  
Mit Internet verbundenes Wallet (Gegenteil: Cold Wallet).

## I

**Index**  
Position in Derivation Path (z.B. /0/5 → Adresse #5).

**Import**  
Einlesen von Wallet-Daten (Seed, Private Key) in eine Anwendung.

## K

**KI-Wiederherstellung**  
AI-gestützte Funktion zur Rekonstruktion beschädigter/unvollständiger Seeds.

**Key Derivation**  
Siehe "Derivation (Ableitung)".

## L

**Legacy Address**  
Älteres Bitcoin-Adressformat (beginnt mit 1).

**Layer 2 (L2)**  
Skalierungslösung auf bestehenden Blockchains (z.B. Arbitrum, Optimism).

## M

**Master Seed**  
Haupt-Seed aus der alle Keys abgeleitet werden.

**Mnemonic**  
Synonym für Seed Phrase - Wortliste zur Wiederherstellung.

**Mainnet**  
Haupt-Blockchain-Netzwerk (Gegenteil: Testnet).

## N

**Native SegWit**  
Bitcoin-Adressformat (bech32, beginnt mit bc1).

**Netzwerk (Network)**  
Blockchain-System (z.B. Ethereum, Bitcoin, BSC).

**Non-custodial**  
Wallet-Typ, bei dem nur der Nutzer Zugriff auf Private Keys hat.

## P

**P2PKH (Pay to Public Key Hash)**  
Bitcoin Legacy-Adressformat.

**P2SH (Pay to Script Hash)**  
Bitcoin-Adressformat für Multi-Sig und SegWit.

**P2WPKH (Pay to Witness Public Key Hash)**  
Bitcoin Native SegWit-Format.

**P2TR (Pay to Taproot)**  
Neuestes Bitcoin-Adressformat (Taproot).

**Passphrase (BIP39)**  
Optionales zusätzliches Passwort zur Seed Phrase (erhöht Sicherheit).

**Private Key**  
Geheimer Schlüssel, der Zugriff auf Wallet ermöglicht. **NIEMALS teilen!**

**Public Key**  
Aus Private Key abgeleiteter öffentlicher Schlüssel.

## Q

**QR Code**  
2D-Barcode zur Darstellung von Wallet-Adressen oder Private Keys.

## R

**Rate Limit**  
Maximale Anzahl API-Anfragen pro Zeiteinheit.

**Recovery**  
Wiederherstellung von Wallet-Zugriff durch Seed/Private Key.

## S

**Scan**  
Prozess der Überprüfung von Adressen auf Guthaben/Transaktionen.

**Seed Phrase**  
12, 15, 18 oder 24 Wörter zur Wallet-Wiederherstellung.

**SegWit (Segregated Witness)**  
Bitcoin-Upgrade für bessere Skalierung und niedrigere Gebühren.

**Signature Detection**  
Forensische Methode zum Erkennen von Wallet-Mustern in Dateien.

## T

**Taproot**  
Bitcoin-Upgrade für mehr Privatsphäre und Effizienz.

**Testnet**  
Test-Blockchain für Entwicklung (verwendet wertlose Test-Coins).

**Transaction (TX)**  
Blockchain-Transaktion (Überweisung, Smart Contract-Interaktion).

## U

**UTF-8**  
Zeichenkodierung (wichtig für internationale Seed Phrases).

## V

**Validator**  
Prüfprogramm für Seed Phrases (prüft auf BIP39-Konformität).

## W

**Wallet**  
Software oder Hardware zur Verwaltung von Kryptowährungen.

**WIF (Wallet Import Format)**  
Kompaktes Format für Bitcoin Private Keys (beginnt mit K, L oder 5).

**Whitepaper**  
Technisches Dokument, das Kryptowährung/Projekt beschreibt.

## Z

**Zero Balance**  
Wallet ohne Guthaben (Transactions = 0, Balance = 0).

---

## Häufig verwechselte Begriffe

### Seed vs. Private Key

```
Seed Phrase (BIP39):
✅ 12/15/18/24 Wörter
✅ Generiert MEHRERE Private Keys
✅ Menschenlesbar

Private Key:
✅ 64 HEX-Zeichen (oder WIF)
✅ Nur EINE Adresse
✅ Maschinenformat
```

### Address vs. Public Key

```
Public Key:
- Lange Zeichenkette (130+ Zeichen)
- Wird aus Private Key abgeleitet
- Selten direkt verwendet

Address:
- Kurze Zeichenkette (40-60 Zeichen)
- Wird aus Public Key abgeleitet
- Das was Sie teilen zum Empfangen
```

### Mainnet vs. Testnet

```
Mainnet:
- Echte Blockchain
- Echte Werte
- Produktiv-Umgebung

Testnet:
- Test-Blockchain
- Wertlose Test-Coins
- Entwicklungs-Umgebung
```

---

## Abkürzungen

| Abkürzung | Bedeutung |
|-----------|-----------|
| BTC | Bitcoin |
| ETH | Ethereum |
| BNB | Binance Coin |
| MATIC | Polygon |
| AVAX | Avalanche |
| ARB | Arbitrum |
| OP | Optimism |
| TX | Transaction |
| GUI | Graphical User Interface |
| CLI | Command Line Interface |
| API | Application Programming Interface |
| HD | Hierarchical Deterministic |
| EVM | Ethereum Virtual Machine |

---

## Nützliche Ressourcen

**BIP39 Wortliste:**
- https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

**Derivation Path Standards:**
- https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki
- https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki
- https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki

**Blockchain Explorer:**
- Ethereum: https://etherscan.io
- Bitcoin: https://blockstream.info
- BSC: https://bscscan.com
- Polygon: https://polygonscan.com

---

## Weitere Hilfe

- ➡️ [Schnellstart](02_schnellstart.md)
- ➡️ [Häufige Probleme](13_haeufige_probleme.md)
- ➡️ [Derivation Paths erklärt](08_derivation_paths.md)
