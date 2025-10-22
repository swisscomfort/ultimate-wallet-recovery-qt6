"""
Blockchain Handler
Zentrale Business Logic für alle Blockchain-Operationen
GUI-unabhängig, vollständig testbar, async-fähig
"""

import asyncio
import aiohttp
import requests
import time
import hashlib
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from datetime import datetime
import logging

from bip_utils import (
    Bip39MnemonicValidator, Bip39SeedGenerator, 
    Bip44, Bip49, Bip84, Bip86, Bip44Changes
)

from .networks import NetworkConfig, NetworkType, NETWORKS, COINGECKO_API
from .derivation import (
    DerivationConfig, DerivationType, 
    get_derivation_path, DERIVATION_PATHS
)
from ..config_manager import ConfigManager

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AddressInfo:
    """Informationen über eine generierte Adresse"""
    address: str
    private_key: str
    public_key: str
    derivation_path: str
    index: int


@dataclass
class ScanResult:
    """Ergebnis eines Blockchain-Scans"""
    timestamp: datetime
    network: str
    address: str
    found: bool
    transactions: int = 0
    balance: float = 0.0
    current_price: float = 0.0
    usd_value: float = 0.0
    derivation_path: str = ""
    error: Optional[str] = None


class BlockchainHandler:
    """
    Zentrale Klasse für alle Blockchain-Operationen
    - Address Generation (BIP39/44/49/84/86)
    - Balance Checking (async)
    - Transaction History
    - Price Data (CoinGecko)
    """
    
    def __init__(self, config_manager: Optional[ConfigManager] = None):
        """
        Args:
            config_manager: Optional ConfigManager für API-Keys
        """
        self.config_manager = config_manager or ConfigManager()
        self.session: Optional[aiohttp.ClientSession] = None
        self.rate_limits: Dict[str, float] = {}  # Network -> Last Request Time
        
    async def __aenter__(self):
        """Async Context Manager Entry"""
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async Context Manager Exit"""
        if self.session:
            await self.session.close()
    
    def generate_addresses_from_seed(
        self,
        seed_phrase: str,
        network: NetworkConfig,
        derivation_config: DerivationConfig,
        passphrase: str = ""
    ) -> List[AddressInfo]:
        """
        Generiert Adressen aus einer Seed Phrase
        
        Args:
            seed_phrase: BIP39 Seed Phrase
            network: Network Configuration
            derivation_config: Derivation Configuration
            passphrase: Optionale BIP39 Passphrase
            
        Returns:
            Liste von AddressInfo Objekten
        """
        addresses = []
        
        try:
            # Validate Seed
            if not Bip39MnemonicValidator().IsValid(seed_phrase):
                raise ValueError("Ungültige BIP39 Seed Phrase")
            
            # Generate Seed
            seed_bytes = Bip39SeedGenerator(seed_phrase).Generate(passphrase)
            
            # Coin Type aus Network
            coin = network.coin
            
            # Multi-Account Scan
            if derivation_config.derivation_type == DerivationType.MULTI:
                for account in range(derivation_config.account + 1):
                    for change in range(derivation_config.change + 1):
                        for index in range(derivation_config.count):
                            addr_info = self._derive_address(
                                seed_bytes, coin, 
                                derivation_config.derivation_type,
                                account, change, index
                            )
                            addresses.append(addr_info)
            else:
                # Standard Derivation
                for index in range(derivation_config.count):
                    addr_info = self._derive_address(
                        seed_bytes, coin,
                        derivation_config.derivation_type,
                        derivation_config.account,
                        derivation_config.change,
                        index
                    )
                    addresses.append(addr_info)
                    
        except Exception as e:
            logger.error(f"Fehler bei Address Generation: {e}")
            raise
            
        return addresses
    
    def _derive_address(
        self,
        seed_bytes: bytes,
        coin: Any,
        derivation_type: DerivationType,
        account: int,
        change: int,
        index: int
    ) -> AddressInfo:
        """Leitet eine einzelne Adresse ab"""
        
        # Wähle Derivation Methode
        if derivation_type == DerivationType.BIP49:
            bip_ctx = Bip49.FromSeed(seed_bytes, coin)
        elif derivation_type == DerivationType.BIP84:
            bip_ctx = Bip84.FromSeed(seed_bytes, coin)
        elif derivation_type == DerivationType.BIP86:
            bip_ctx = Bip86.FromSeed(seed_bytes, coin)
        else:  # BIP44 Default
            bip_ctx = Bip44.FromSeed(seed_bytes, coin)
        
        # Derive Path: m/purpose'/coin_type'/account'/change/index
        bip_ctx = bip_ctx.Purpose()
        bip_ctx = bip_ctx.Coin()
        bip_ctx = bip_ctx.Account(account)
        bip_ctx = bip_ctx.Change(Bip44Changes.CHAIN_EXT if change == 0 else Bip44Changes.CHAIN_INT)
        bip_ctx = bip_ctx.AddressIndex(index)
        
        # Extract Info
        address = bip_ctx.PublicKey().ToAddress()
        private_key = bip_ctx.PrivateKey().Raw().ToHex()
        public_key = bip_ctx.PublicKey().RawCompressed().ToHex()
        
        # Derivation Path
        coin_type = coin.CoinNames()[0].split("_")[0] if hasattr(coin, 'CoinNames') else "0"
        path = get_derivation_path(derivation_type, int(coin_type), account, change, index)
        
        return AddressInfo(
            address=address,
            private_key=private_key,
            public_key=public_key,
            derivation_path=path,
            index=index
        )
    
    async def check_address_balance(
        self,
        address: str,
        network: NetworkConfig
    ) -> Tuple[int, float]:
        """
        Prüft Balance einer Adresse (async)
        
        Args:
            address: Blockchain Adresse
            network: Network Configuration
            
        Returns:
            (transaction_count, balance)
        """
        # Rate Limiting
        await self._rate_limit(network.name)
        
        try:
            if network.network_type == NetworkType.EVM:
                return await self._check_evm_balance(address, network)
            elif network.network_type == NetworkType.BITCOIN:
                return await self._check_bitcoin_balance(address, network)
            else:
                logger.warning(f"Network Type {network.network_type} nicht unterstützt")
                return (0, 0.0)
                
        except Exception as e:
            logger.error(f"Fehler beim Balance Check für {address}: {e}")
            return (0, 0.0)
    
    async def _check_evm_balance(
        self,
        address: str,
        network: NetworkConfig
    ) -> Tuple[int, float]:
        """Prüft EVM-Balance"""
        if not self.session:
            raise RuntimeError("Session nicht initialisiert. Verwende async with BlockchainHandler()")
        
        # API Key
        api_key = ""
        if network.api_key_name:
            api_key = self.config_manager.get_api_key(network.api_key_name.lower().replace("_api_key", ""))
        
        # Transaction Count
        params = {
            **network.explorer_params,
            "address": address,
            "apikey": api_key,
            "sort": "desc"
        }
        
        try:
            async with self.session.get(network.explorer_api, params=params, timeout=15) as response:
                data = await response.json()
                
                if data.get("status") == "1":
                    tx_list = data.get("result", [])
                    tx_count = len(tx_list)
                    
                    # Balance berechnen (letzte TX)
                    balance = 0.0
                    if tx_list:
                        # Wei -> Ether
                        latest_balance = int(tx_list[0].get("value", 0))
                        balance = latest_balance / (10 ** network.decimals)
                    
                    return (tx_count, balance)
                else:
                    return (0, 0.0)
                    
        except Exception as e:
            logger.error(f"EVM Balance Check Fehler: {e}")
            return (0, 0.0)
    
    async def _check_bitcoin_balance(
        self,
        address: str,
        network: NetworkConfig
    ) -> Tuple[int, float]:
        """Prüft Bitcoin-Balance"""
        if not self.session:
            raise RuntimeError("Session nicht initialisiert")
        
        try:
            # Blockstream API für Bitcoin
            url = f"{network.explorer_api}/address/{address}"
            
            async with self.session.get(url, timeout=15) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    tx_count = data.get("chain_stats", {}).get("tx_count", 0)
                    balance_sat = data.get("chain_stats", {}).get("funded_txo_sum", 0)
                    balance = balance_sat / (10 ** network.decimals)
                    
                    return (tx_count, balance)
                else:
                    return (0, 0.0)
                    
        except Exception as e:
            logger.error(f"Bitcoin Balance Check Fehler: {e}")
            return (0, 0.0)
    
    async def get_current_price(self, coingecko_id: str) -> float:
        """
        Holt aktuellen Preis von CoinGecko
        
        Args:
            coingecko_id: CoinGecko ID (z.B. "ethereum")
            
        Returns:
            Preis in USD
        """
        if not self.session:
            raise RuntimeError("Session nicht initialisiert")
        
        try:
            params = {
                "ids": coingecko_id,
                "vs_currencies": "usd"
            }
            
            async with self.session.get(COINGECKO_API, params=params, timeout=10) as response:
                data = await response.json()
                return data.get(coingecko_id, {}).get("usd", 0.0)
                
        except Exception as e:
            logger.error(f"CoinGecko Price Fetch Fehler: {e}")
            return 0.0
    
    async def scan_address(
        self,
        address_info: AddressInfo,
        network: NetworkConfig
    ) -> ScanResult:
        """
        Scannt eine einzelne Adresse
        
        Args:
            address_info: Address Information
            network: Network Configuration
            
        Returns:
            ScanResult
        """
        try:
            # Balance Check
            tx_count, balance = await self.check_address_balance(
                address_info.address, network
            )
            
            # Price
            current_price = await self.get_current_price(network.coingecko_id)
            usd_value = balance * current_price
            
            found = tx_count > 0 or balance > 0
            
            return ScanResult(
                timestamp=datetime.now(),
                network=network.name,
                address=address_info.address,
                found=found,
                transactions=tx_count,
                balance=balance,
                current_price=current_price,
                usd_value=usd_value,
                derivation_path=address_info.derivation_path
            )
            
        except Exception as e:
            logger.error(f"Scan Fehler für {address_info.address}: {e}")
            return ScanResult(
                timestamp=datetime.now(),
                network=network.name,
                address=address_info.address,
                found=False,
                error=str(e)
            )
    
    async def scan_multiple_networks(
        self,
        seed_phrase: str,
        networks: List[NetworkConfig],
        derivation_config: DerivationConfig,
        passphrase: str = "",
        progress_callback: Optional[callable] = None
    ) -> List[ScanResult]:
        """
        Scannt mehrere Netzwerke parallel
        
        Args:
            seed_phrase: BIP39 Seed Phrase
            networks: Liste von Networks
            derivation_config: Derivation Config
            passphrase: Optionale Passphrase
            progress_callback: Optional callback(current, total, result)
            
        Returns:
            Liste von ScanResults
        """
        all_results = []
        total_tasks = len(networks) * derivation_config.count
        current = 0
        
        for network in networks:
            # Generate Addresses
            addresses = self.generate_addresses_from_seed(
                seed_phrase, network, derivation_config, passphrase
            )
            
            # Scan parallel
            tasks = [self.scan_address(addr, network) for addr in addresses]
            results = await asyncio.gather(*tasks)
            
            for result in results:
                current += 1
                all_results.append(result)
                
                if progress_callback:
                    progress_callback(current, total_tasks, result)
        
        return all_results
    
    async def _rate_limit(self, network_name: str, min_interval: float = 1.0):
        """Rate Limiting für API Calls"""
        last_request = self.rate_limits.get(network_name, 0)
        current_time = time.time()
        
        time_since_last = current_time - last_request
        
        if time_since_last < min_interval:
            await asyncio.sleep(min_interval - time_since_last)
        
        self.rate_limits[network_name] = time.time()


# Synchrone Wrapper-Funktionen für Kompatibilität
def generate_addresses_sync(
    seed_phrase: str,
    network: NetworkConfig,
    derivation_config: DerivationConfig,
    passphrase: str = ""
) -> List[AddressInfo]:
    """Synchroner Wrapper für generate_addresses_from_seed"""
    handler = BlockchainHandler()
    return handler.generate_addresses_from_seed(
        seed_phrase, network, derivation_config, passphrase
    )


def scan_address_sync(
    address_info: AddressInfo,
    network: NetworkConfig,
    config_manager: Optional[ConfigManager] = None
) -> ScanResult:
    """Synchroner Wrapper für scan_address"""
    async def _scan():
        async with BlockchainHandler(config_manager) as handler:
            return await handler.scan_address(address_info, network)
    
    return asyncio.run(_scan())
