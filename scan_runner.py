#!/usr/bin/env python3
"""
Standalone Scan Runner für Ultimate Wallet Recovery Tool
Startet einen forensischen Scan unabhängig von der GUI und gibt alle Logs live auf stdout aus.
Ergebnisse werden wie gehabt in die Datenbank geschrieben.
"""
import sys
import os
import argparse
from datetime import datetime
from src.forensic.core.file_scanner import ForensicFileScanner, ScanMode


def main():
    parser = argparse.ArgumentParser(description="Standalone Forensic Scan Runner")
    parser.add_argument("--path", required=True, help="Verzeichnis zum Scannen")
    parser.add_argument("--mode", choices=["quick", "deep", "forensic"], default="deep", help="Scan-Modus")
    parser.add_argument("--db", default=None, help="Pfad zur Ergebnis-Datenbank (optional)")
    args = parser.parse_args()

    scan_mode_map = {
        "quick": ScanMode.QUICK_SCAN,
        "deep": ScanMode.DEEP_SCAN,
        "forensic": ScanMode.FORENSIC_MODE
    }
    scan_mode = scan_mode_map[args.mode]

    print(f"[INFO] Starte Scan: {args.path} | Modus: {scan_mode.value}")
    scanner = ForensicFileScanner(database_path=args.db)
    start_time = datetime.now()
    results = []
    for result in scanner.scan_directory(args.path, scan_mode, recursive=True, max_workers=4):
        print(f"[RESULT] Datei: {result.file_info.path}")
        print(f"         Größe: {result.file_info.size} Bytes")
        print(f"         Risiko: {result.risk_assessment['overall_risk']:.2f}")
        print(f"         Erkennungen: {len(result.detections)}")
        for detection in result.detections:
            print(f"         🔍 {detection.signature_type.value}: {detection.pattern_matched[:50]}...")
        if result.recommendations:
            print("         💡 Empfehlungen:")
            for rec in result.recommendations:
                print(f"            {rec}")
        sys.stdout.flush()
        results.append(result)
    print(f"[INFO] Scan abgeschlossen. {len(results)} Dateien analysiert.")
    print(f"[INFO] Ergebnisse wurden in die Datenbank geschrieben: {scanner.database_path}")
    print(f"[INFO] Dauer: {datetime.now() - start_time}")

if __name__ == "__main__":
    main()
