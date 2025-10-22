"""
Network Configuration Module
Zentrale Konfiguration für alle unterstützten Blockchain-Netzwerke
"""

from bip_utils import Bip44Coins
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum


class NetworkType(Enum):
    """Typ des Blockchain-Netzwerks"""
    EVM = "evm"
    BITCOIN = "bitcoin"
    SOLANA = "solana"
    CARDANO = "cardano"


@dataclass
class NetworkConfig:
    """Konfiguration für ein Blockchain-Netzwerk"""
    name: str
    symbol: str
    network_type: NetworkType
    coin: Bip44Coins
    explorer_api: str
    explorer_params: Dict[str, str]
    coingecko_id: str
    decimals: int
    enabled: bool = True
    api_key_name: str = None  # Name des API-Keys in .env (z.B. "ETHERSCAN_API_KEY")


# Alle unterstützten Netzwerke
NETWORKS: List[NetworkConfig] = [
    # EVM-Compatible Chains
    NetworkConfig(
        name="Ethereum",
        symbol="ETH",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.ETHEREUM,
        explorer_api="https://api.etherscan.io/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="ethereum",
        decimals=18,
        api_key_name="ETHERSCAN_API_KEY"
    ),
    NetworkConfig(
        name="BNB Smart Chain",
        symbol="BNB",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.BINANCE_SMART_CHAIN,
        explorer_api="https://api.bscscan.com/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="binancecoin",
        decimals=18,
        api_key_name="BSCSCAN_API_KEY"
    ),
    NetworkConfig(
        name="Polygon",
        symbol="MATIC",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.POLYGON,
        explorer_api="https://api.polygonscan.com/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="matic-network",
        decimals=18,
        api_key_name="POLYGONSCAN_API_KEY"
    ),
    NetworkConfig(
        name="Arbitrum",
        symbol="ARB",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.ARBITRUM,
        explorer_api="https://api.arbiscan.io/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="arbitrum",
        decimals=18,
        api_key_name="ARBISCAN_API_KEY"
    ),
    NetworkConfig(
        name="Optimism",
        symbol="OP",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.OPTIMISM,
        explorer_api="https://api-optimistic.etherscan.io/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="optimism",
        decimals=18,
        api_key_name="OPTIMISM_API_KEY"
    ),
    NetworkConfig(
        name="Avalanche C-Chain",
        symbol="AVAX",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.AVAX_C_CHAIN,
        explorer_api="https://api.snowtrace.io/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="avalanche-2",
        decimals=18,
        api_key_name="SNOWTRACE_API_KEY"
    ),
    NetworkConfig(
        name="Fantom",
        symbol="FTM",
        network_type=NetworkType.EVM,
        coin=Bip44Coins.FANTOM_OPERA,
        explorer_api="https://api.ftmscan.com/api",
        explorer_params={"module": "account", "action": "txlist"},
        coingecko_id="fantom",
        decimals=18,
        api_key_name="FTMSCAN_API_KEY"
    ),
    # Bitcoin Networks
    NetworkConfig(
        name="Bitcoin",
        symbol="BTC",
        network_type=NetworkType.BITCOIN,
        coin=Bip44Coins.BITCOIN,
        explorer_api="https://blockstream.info/api",
        explorer_params={},
        coingecko_id="bitcoin",
        decimals=8
    ),
    NetworkConfig(
        name="Litecoin",
        symbol="LTC",
        network_type=NetworkType.BITCOIN,
        coin=Bip44Coins.LITECOIN,
        explorer_api="https://litecoinspace.org/api",
        explorer_params={},
        coingecko_id="litecoin",
        decimals=8
    ),
    NetworkConfig(
        name="Dogecoin",
        symbol="DOGE",
        network_type=NetworkType.BITCOIN,
        coin=Bip44Coins.DOGECOIN,
        explorer_api="https://dogechain.info/api",
        explorer_params={},
        coingecko_id="dogecoin",
        decimals=8
    ),
    NetworkConfig(
        name="Bitcoin Cash",
        symbol="BCH",
        network_type=NetworkType.BITCOIN,
        coin=Bip44Coins.BITCOIN_CASH,
        explorer_api="https://api.blockchair.com/bitcoin-cash",
        explorer_params={},
        coingecko_id="bitcoin-cash",
        decimals=8
    ),
]


# Helper Funktionen
def get_network_by_name(name: str) -> NetworkConfig:
    """Gibt Network Config nach Namen zurück"""
    for network in NETWORKS:
        if network.name.lower() == name.lower():
            return network
    raise ValueError(f"Network '{name}' nicht gefunden")


def get_network_by_symbol(symbol: str) -> NetworkConfig:
    """Gibt Network Config nach Symbol zurück"""
    for network in NETWORKS:
        if network.symbol.upper() == symbol.upper():
            return network
    raise ValueError(f"Network mit Symbol '{symbol}' nicht gefunden")


def get_networks_by_type(network_type: NetworkType) -> List[NetworkConfig]:
    """Gibt alle Netzwerke eines Typs zurück"""
    return [n for n in NETWORKS if n.network_type == network_type]


def get_enabled_networks() -> List[NetworkConfig]:
    """Gibt alle aktivierten Netzwerke zurück"""
    return [n for n in NETWORKS if n.enabled]


# CoinGecko API
COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"
