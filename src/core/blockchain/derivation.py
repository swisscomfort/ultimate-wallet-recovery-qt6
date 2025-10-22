"""
Derivation Path Configuration
BIP39/BIP44/BIP49/BIP84/BIP86 Derivation Paths für verschiedene Wallet-Typen
"""

from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class DerivationType(Enum):
    """Typ der Derivation"""
    BIP44 = "bip44"  # Legacy/Standard
    BIP49 = "bip49"  # SegWit (P2SH-P2WPKH)
    BIP84 = "bip84"  # Native SegWit (P2WPKH)
    BIP86 = "bip86"  # Taproot (P2TR)
    CUSTOM = "custom"  # Benutzerdefiniert
    MULTI = "multi"  # Multi-Account Scan


@dataclass
class DerivationConfig:
    """Konfiguration für einen Derivation Path"""
    name: str
    derivation_type: DerivationType
    account: int = 0
    change: int = 0
    count: int = 5  # Anzahl der zu generierenden Adressen
    description: str = ""
    

# Vordefinierte Derivation Paths
DERIVATION_PATHS: Dict[str, DerivationConfig] = {
    "Standard (BIP44)": DerivationConfig(
        name="Standard (BIP44)",
        derivation_type=DerivationType.BIP44,
        account=0,
        change=0,
        count=5,
        description="Standard BIP44 Derivation für EVM und Bitcoin Legacy"
    ),
    "Extended (10 Addresses)": DerivationConfig(
        name="Extended (10 Addresses)",
        derivation_type=DerivationType.BIP44,
        account=0,
        change=0,
        count=10,
        description="Erweitert: 10 Adressen scannen"
    ),
    "Deep Scan (20 Addresses)": DerivationConfig(
        name="Deep Scan (20 Addresses)",
        derivation_type=DerivationType.BIP44,
        account=0,
        change=0,
        count=20,
        description="Tiefer Scan: 20 Adressen scannen"
    ),
    "Bitcoin Legacy (P2PKH)": DerivationConfig(
        name="Bitcoin Legacy (P2PKH)",
        derivation_type=DerivationType.BIP44,
        account=0,
        change=0,
        count=10,
        description="Bitcoin Legacy Adressen (1...)"
    ),
    "Bitcoin SegWit (P2SH)": DerivationConfig(
        name="Bitcoin SegWit (P2SH)",
        derivation_type=DerivationType.BIP49,
        account=0,
        change=0,
        count=10,
        description="Bitcoin SegWit Adressen (3...)"
    ),
    "Bitcoin Native SegWit (P2WPKH)": DerivationConfig(
        name="Bitcoin Native SegWit (P2WPKH)",
        derivation_type=DerivationType.BIP84,
        account=0,
        change=0,
        count=10,
        description="Bitcoin Native SegWit Adressen (bc1q...)"
    ),
    "Bitcoin Taproot (P2TR)": DerivationConfig(
        name="Bitcoin Taproot (P2TR)",
        derivation_type=DerivationType.BIP86,
        account=0,
        change=0,
        count=10,
        description="Bitcoin Taproot Adressen (bc1p...)"
    ),
    "Hardware Wallets": DerivationConfig(
        name="Hardware Wallets",
        derivation_type=DerivationType.BIP44,
        account=0,
        change=0,
        count=5,
        description="Standard für Hardware Wallets (Ledger, Trezor)"
    ),
    "Multi-Account Scan": DerivationConfig(
        name="Multi-Account Scan",
        derivation_type=DerivationType.MULTI,
        account=3,  # Bis Account 3
        change=2,   # Internal und External
        count=5,
        description="Scannt mehrere Accounts und Change Chains"
    ),
    "Custom Configuration": DerivationConfig(
        name="Custom Configuration",
        derivation_type=DerivationType.CUSTOM,
        account=0,
        change=0,
        count=5,
        description="Benutzerdefinierte Konfiguration"
    ),
}


def get_derivation_path(
    derivation_type: DerivationType,
    coin_type: int,
    account: int = 0,
    change: int = 0,
    index: int = 0
) -> str:
    """
    Generiert einen Derivation Path String
    
    Args:
        derivation_type: Typ der Derivation (BIP44/49/84/86)
        coin_type: BIP44 Coin Type (z.B. 60 für ETH, 0 für BTC)
        account: Account Index
        change: Change Chain (0 = external, 1 = internal)
        index: Address Index
        
    Returns:
        Derivation Path String (z.B. "m/44'/60'/0'/0/0")
    """
    if derivation_type == DerivationType.BIP44:
        purpose = 44
    elif derivation_type == DerivationType.BIP49:
        purpose = 49
    elif derivation_type == DerivationType.BIP84:
        purpose = 84
    elif derivation_type == DerivationType.BIP86:
        purpose = 86
    else:
        purpose = 44  # Default
    
    return f"m/{purpose}'/{coin_type}'/{account}'/{change}/{index}"


def get_derivation_config(name: str) -> DerivationConfig:
    """Gibt Derivation Config nach Namen zurück"""
    if name in DERIVATION_PATHS:
        return DERIVATION_PATHS[name]
    raise ValueError(f"Derivation Path '{name}' nicht gefunden")


def get_all_derivation_names() -> List[str]:
    """Gibt alle verfügbaren Derivation Path Namen zurück"""
    return list(DERIVATION_PATHS.keys())
