#!/usr/bin/env python3
"""
Ultimate Wallet Recovery Tool - Launcher
Qt6-basierte moderne GUI für Wallet Recovery
"""

import sys
import argparse
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))


def main():
    parser = argparse.ArgumentParser(
        description="Ultimate Wallet Recovery Tool"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Debug-Modus aktivieren"
    )
    
    args = parser.parse_args()
    
    # Qt6 GUI starten
    print("🚀 Starte Ultimate Wallet Recovery Tool...")
    from gui.main_window import main as qt6_main
    qt6_main()


if __name__ == "__main__":
    main()
