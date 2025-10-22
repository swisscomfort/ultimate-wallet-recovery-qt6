"""
Blockchain Module
GUI-unabhängige Business Logic für alle Blockchain-Operationen
"""

from .networks import (
    NetworkConfig,
    NetworkType,
    NETWORKS,
    get_network_by_name,
    get_network_by_symbol,
    get_networks_by_type,
    get_enabled_networks,
    COINGECKO_API
)

from .derivation import (
    DerivationConfig,
    DerivationType,
    DERIVATION_PATHS,
    get_derivation_path,
    get_derivation_config,
    get_all_derivation_names
)

from .handler import (
    BlockchainHandler,
    AddressInfo,
    ScanResult,
    generate_addresses_sync,
    scan_address_sync
)

__all__ = [
    # Networks
    'NetworkConfig',
    'NetworkType',
    'NETWORKS',
    'get_network_by_name',
    'get_network_by_symbol',
    'get_networks_by_type',
    'get_enabled_networks',
    'COINGECKO_API',
    # Derivation
    'DerivationConfig',
    'DerivationType',
    'DERIVATION_PATHS',
    'get_derivation_path',
    'get_derivation_config',
    'get_all_derivation_names',
    # Handler
    'BlockchainHandler',
    'AddressInfo',
    'ScanResult',
    'generate_addresses_sync',
    'scan_address_sync',
]
