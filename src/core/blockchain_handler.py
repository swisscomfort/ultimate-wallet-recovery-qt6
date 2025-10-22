"""
Ultimate Wallet Recovery Tool - Blockchain Handler
Handles all blockchain-related operations with improved architecture
"""

import asyncio
import aiohttp
import time
import logging
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
from concurrent.futures import ThreadPoolExecutor
import hashlib
from difflib import get_close_matches

from .config_manager import config

try:
    from bip_utils import (
        Bip39MnemonicValidator, Bip39MnemonicGenerator, Bip39WordsNum,
        Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes,
        Bip49, Bip84, Bip86
    )
    BIP_UTILS_AVAILABLE = True
except ImportError:
    BIP_UTILS_AVAILABLE = False

logger = logging.getLogger(__name__)


class NetworkType(Enum):
    """Supported network types"""
    EVM = "evm"
    BITCOIN = "bitcoin"
    UNKNOWN = "unknown"


class AddressType(Enum):
    """Bitcoin address types"""
    P2PKH = "p2pkh"  # Legacy
    P2SH = "p2sh"    # SegWit wrapped
    P2WPKH = "p2wpkh"  # Native SegWit
    P2TR = "p2tr"    # Taproot
    EVM = "evm"      # Ethereum-style


@dataclass
class AddressInfo:
    """Information about a derived address"""
    address: str
    address_type: AddressType
    derivation_path: str
    private_key: Optional[str] = None
    public_key: Optional[str] = None


@dataclass
class ScanResult:
    """Result of scanning an address"""
    address_info: AddressInfo
    network: str
    has_activity: bool
    transaction_count: int
    balance: float
    current_price: float
    total_value: float
    scan_time: float
    error: Optional[str] = None


class BlockchainHandler:
    """Handles all blockchain operations with async support"""
    
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
        self.performance_settings = config.get_performance_settings()
        self.rate_limiter = {}  # Per-network rate limiting
        
    async def __aenter__(self):
        """Async context manager entry"""
        connector = aiohttp.TCPConnector(
            limit=self.performance_settings['max_concurrent_requests']
        )
        timeout = aiohttp.ClientTimeout(
            total=self.performance_settings['request_timeout']
        )
        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    def validate_mnemonic(self, mnemonic: str) -> bool:
        """Validate BIP39 mnemonic phrase"""
        if not BIP_UTILS_AVAILABLE:
            logger.warning("BIP utils not available for mnemonic validation")
            return False
        
        try:
            return Bip39MnemonicValidator().IsValid(mnemonic)
        except Exception as e:
            logger.error(f"Mnemonic validation error: {e}")
            return False
    
    def suggest_mnemonic_corrections(self, words: List[str]) -> str:
        """Suggest corrections for invalid mnemonic words"""
        if not BIP_UTILS_AVAILABLE:
            return " ".join(words)
        
        try:
            generator = Bip39MnemonicGenerator()
            valid_words = generator.FromWordsNumber(Bip39WordsNum.WORDS_NUM_24).ToList()
            
            corrected = []
            for word in words:
                if word in valid_words:
                    corrected.append(word)
                else:
                    matches = get_close_matches(word, valid_words, 1, cutoff=0.6)
                    corrected.append(matches[0] if matches else word)
            
            return " ".join(corrected)
        except Exception as e:
            logger.error(f"Mnemonic correction error: {e}")
            return " ".join(words)
    
    def derive_addresses(self, 
                        seed: str, 
                        passphrase: str = "",
                        network_config: Dict[str, Any] = None,
                        derivation_config: Dict[str, Any] = None) -> List[AddressInfo]:
        """Derive addresses for a given seed and network"""
        if not BIP_UTILS_AVAILABLE:
            logger.error("BIP utils not available for address derivation")
            return []
        
        if not network_config or not derivation_config:
            return []
        
        try:
            seed_bytes = Bip39SeedGenerator(seed).Generate(passphrase)
            network_type = NetworkType(network_config.get('type', 'unknown'))
            
            if network_type == NetworkType.EVM:
                return self._derive_evm_addresses(seed_bytes, network_config, derivation_config)
            elif network_type == NetworkType.BITCOIN:
                return self._derive_bitcoin_addresses(seed_bytes, network_config, derivation_config)
            else:
                logger.warning(f"Unsupported network type: {network_type}")
                return []
                
        except Exception as e:
            logger.error(f"Address derivation error: {e}")
            return []
    
    def _derive_evm_addresses(self, 
                             seed_bytes: bytes,
                             network_config: Dict[str, Any],
                             derivation_config: Dict[str, Any]) -> List[AddressInfo]:
        """Derive EVM-compatible addresses"""
        addresses = []
        
        try:
            # Map coin_type to Bip44Coins enum
            coin_type = network_config.get('coin_type', 60)
            bip44_coin = self._get_bip44_coin(coin_type)
            
            if not bip44_coin:
                logger.warning(f"Unsupported coin type: {coin_type}")
                return []
            
            bip44_ctx = Bip44.FromSeed(seed_bytes, bip44_coin)
            
            for i in range(derivation_config.get('count', 5)):
                addr_ctx = bip44_ctx.Purpose().Coin().Account(
                    derivation_config.get('account', 0)
                ).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
                
                address_info = AddressInfo(
                    address=addr_ctx.PublicKey().ToAddress(),
                    address_type=AddressType.EVM,
                    derivation_path=f"m/44'/{coin_type}'/{derivation_config.get('account', 0)}'/0/{i}",
                    private_key=addr_ctx.PrivateKey().Raw().ToHex(),
                    public_key=addr_ctx.PublicKey().RawCompressed().ToHex()
                )
                addresses.append(address_info)
                
        except Exception as e:
            logger.error(f"EVM address derivation error: {e}")
        
        return addresses
    
    def _derive_bitcoin_addresses(self,
                                 seed_bytes: bytes,
                                 network_config: Dict[str, Any],
                                 derivation_config: Dict[str, Any]) -> List[AddressInfo]:
        """Derive Bitcoin addresses with multiple formats"""
        addresses = []
        
        try:
            coin_type = network_config.get('coin_type', 0)
            bip44_coin = self._get_bip44_coin(coin_type)
            
            if not bip44_coin:
                return []
            
            derivation_type = derivation_config.get('type', 'bip44')
            count = derivation_config.get('count', 5)
            account = derivation_config.get('account', 0)
            
            # BIP44 (Legacy P2PKH)
            if derivation_type in ['bip44', 'multi']:
                addresses.extend(self._derive_bip44_addresses(
                    seed_bytes, bip44_coin, account, count, coin_type
                ))
            
            # BIP49 (SegWit P2SH)
            if derivation_type in ['bip49', 'multi']:
                addresses.extend(self._derive_bip49_addresses(
                    seed_bytes, bip44_coin, account, count, coin_type
                ))
            
            # BIP84 (Native SegWit P2WPKH)
            if derivation_type in ['bip84', 'multi']:
                addresses.extend(self._derive_bip84_addresses(
                    seed_bytes, bip44_coin, account, count, coin_type
                ))
            
            # BIP86 (Taproot P2TR)
            if derivation_type in ['bip86', 'multi']:
                addresses.extend(self._derive_bip86_addresses(
                    seed_bytes, bip44_coin, account, count, coin_type
                ))
                
        except Exception as e:
            logger.error(f"Bitcoin address derivation error: {e}")
        
        return addresses
    
    def _derive_bip44_addresses(self, seed_bytes, coin, account, count, coin_type):
        """Derive BIP44 legacy addresses"""
        addresses = []
        try:
            bip44_ctx = Bip44.FromSeed(seed_bytes, coin)
            for i in range(count):
                addr_ctx = bip44_ctx.Purpose().Coin().Account(account).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
                addresses.append(AddressInfo(
                    address=addr_ctx.PublicKey().ToAddress(),
                    address_type=AddressType.P2PKH,
                    derivation_path=f"m/44'/{coin_type}'/{account}'/0/{i}",
                    private_key=addr_ctx.PrivateKey().Raw().ToHex()
                ))
        except Exception as e:
            logger.debug(f"BIP44 derivation error: {e}")
        return addresses
    
    def _derive_bip49_addresses(self, seed_bytes, coin, account, count, coin_type):
        """Derive BIP49 SegWit addresses"""
        addresses = []
        try:
            bip49_ctx = Bip49.FromSeed(seed_bytes, coin)
            for i in range(count):
                addr_ctx = bip49_ctx.Purpose().Coin().Account(account).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
                addresses.append(AddressInfo(
                    address=addr_ctx.PublicKey().ToAddress(),
                    address_type=AddressType.P2SH,
                    derivation_path=f"m/49'/{coin_type}'/{account}'/0/{i}",
                    private_key=addr_ctx.PrivateKey().Raw().ToHex()
                ))
        except Exception as e:
            logger.debug(f"BIP49 derivation error: {e}")
        return addresses
    
    def _derive_bip84_addresses(self, seed_bytes, coin, account, count, coin_type):
        """Derive BIP84 Native SegWit addresses"""
        addresses = []
        try:
            bip84_ctx = Bip84.FromSeed(seed_bytes, coin)
            for i in range(count):
                addr_ctx = bip84_ctx.Purpose().Coin().Account(account).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
                addresses.append(AddressInfo(
                    address=addr_ctx.PublicKey().ToAddress(),
                    address_type=AddressType.P2WPKH,
                    derivation_path=f"m/84'/{coin_type}'/{account}'/0/{i}",
                    private_key=addr_ctx.PrivateKey().Raw().ToHex()
                ))
        except Exception as e:
            logger.debug(f"BIP84 derivation error: {e}")
        return addresses
    
    def _derive_bip86_addresses(self, seed_bytes, coin, account, count, coin_type):
        """Derive BIP86 Taproot addresses"""
        addresses = []
        try:
            bip86_ctx = Bip86.FromSeed(seed_bytes, coin)
            for i in range(count):
                addr_ctx = bip86_ctx.Purpose().Coin().Account(account).Change(Bip44Changes.CHAIN_EXT).AddressIndex(i)
                addresses.append(AddressInfo(
                    address=addr_ctx.PublicKey().ToAddress(),
                    address_type=AddressType.P2TR,
                    derivation_path=f"m/86'/{coin_type}'/{account}'/0/{i}",
                    private_key=addr_ctx.PrivateKey().Raw().ToHex()
                ))
        except Exception as e:
            logger.debug(f"BIP86 derivation error: {e}")
        return addresses
    
    def _get_bip44_coin(self, coin_type: int):
        """Map coin type to Bip44Coins enum"""
        coin_mapping = {
            0: Bip44Coins.BITCOIN,
            2: Bip44Coins.LITECOIN,
            3: Bip44Coins.DOGECOIN,
            60: Bip44Coins.ETHEREUM,
            145: Bip44Coins.BITCOIN_CASH,
            714: Bip44Coins.BINANCE_SMART_CHAIN,
            966: Bip44Coins.POLYGON,
        }
        return coin_mapping.get(coin_type)
    
    async def scan_addresses(self, 
                           addresses: List[AddressInfo],
                           network_config: Dict[str, Any],
                           progress_callback: Optional[callable] = None) -> List[ScanResult]:
        """Scan multiple addresses for activity"""
        if not self.session:
            raise RuntimeError("Session not initialized. Use async context manager.")
        
        results = []
        network_name = network_config.get('name', 'Unknown')
        
        # Apply rate limiting
        await self._apply_rate_limit(network_name)
        
        # Create semaphore for concurrent requests
        semaphore = asyncio.Semaphore(self.performance_settings['max_concurrent_requests'])
        
        # Create tasks for all addresses
        tasks = []
        for i, address_info in enumerate(addresses):
            task = self._scan_single_address(
                semaphore, address_info, network_config, i, len(addresses)
            )
            tasks.append(task)
        
        # Execute tasks and collect results
        for i, task in enumerate(asyncio.as_completed(tasks)):
            try:
                result = await task
                results.append(result)
                
                if progress_callback:
                    progress = (i + 1) / len(addresses)
                    progress_callback(progress, result)
                    
            except Exception as e:
                logger.error(f"Error scanning address: {e}")
        
        return results
    
    async def _scan_single_address(self,
                                  semaphore: asyncio.Semaphore,
                                  address_info: AddressInfo,
                                  network_config: Dict[str, Any],
                                  index: int,
                                  total: int) -> ScanResult:
        """Scan a single address for activity"""
        async with semaphore:
            start_time = time.time()
            
            try:
                network_type = NetworkType(network_config.get('type', 'unknown'))
                
                if network_type == NetworkType.EVM:
                    has_activity, tx_count, balance = await self._check_evm_activity(
                        address_info.address, network_config
                    )
                elif network_type == NetworkType.BITCOIN:
                    has_activity, tx_count, balance = await self._check_bitcoin_activity(
                        address_info.address, network_config
                    )
                else:
                    has_activity, tx_count, balance = False, 0, 0.0
                
                # Get current price
                current_price = await self._get_coin_price(network_config.get('coingecko_id'))
                total_value = balance * current_price if current_price else 0.0
                
                scan_time = time.time() - start_time
                
                return ScanResult(
                    address_info=address_info,
                    network=network_config.get('name', 'Unknown'),
                    has_activity=has_activity,
                    transaction_count=tx_count,
                    balance=balance,
                    current_price=current_price,
                    total_value=total_value,
                    scan_time=scan_time
                )
                
            except Exception as e:
                scan_time = time.time() - start_time
                logger.error(f"Error scanning {address_info.address}: {e}")
                
                return ScanResult(
                    address_info=address_info,
                    network=network_config.get('name', 'Unknown'),
                    has_activity=False,
                    transaction_count=0,
                    balance=0.0,
                    current_price=0.0,
                    total_value=0.0,
                    scan_time=scan_time,
                    error=str(e)
                )
    
    async def _check_evm_activity(self, 
                                 address: str, 
                                 network_config: Dict[str, Any]) -> Tuple[bool, int, float]:
        """Check EVM address activity"""
        try:
            api_key = network_config.get('api_key')
            if not api_key:
                logger.warning(f"No API key for {network_config.get('name')}")
                return False, 0, 0.0
            
            # Check transactions
            params = {
                'module': 'account',
                'action': 'txlist',
                'address': address,
                'apikey': api_key,
                'page': 1,
                'offset': 10
            }
            
            async with self.session.get(network_config['explorer_api'], params=params) as response:
                data = await response.json()
                
                if data.get('status') == '1' and data.get('result'):
                    tx_count = len(data['result'])
                    
                    # Get balance
                    balance_params = {
                        'module': 'account',
                        'action': 'balance',
                        'address': address,
                        'tag': 'latest',
                        'apikey': api_key
                    }
                    
                    async with self.session.get(network_config['explorer_api'], params=balance_params) as balance_response:
                        balance_data = await balance_response.json()
                        
                        if balance_data.get('status') == '1':
                            balance_wei = int(balance_data.get('result', '0'))
                            balance = balance_wei / (10 ** network_config.get('decimals', 18))
                            return True, tx_count, balance
                
                return False, 0, 0.0
                
        except Exception as e:
            logger.error(f"EVM activity check error: {e}")
            return False, 0, 0.0
    
    async def _check_bitcoin_activity(self,
                                     address: str,
                                     network_config: Dict[str, Any]) -> Tuple[bool, int, float]:
        """Check Bitcoin address activity"""
        try:
            network_name = network_config.get('name', '').lower()
            
            if 'bitcoin' in network_name:
                api_url = f"https://blockstream.info/api/address/{address}/txs"
            elif 'litecoin' in network_name:
                api_url = f"https://litecoinspace.org/api/address/{address}/txs"
            else:
                return False, 0, 0.0
            
            async with self.session.get(api_url) as response:
                if response.status == 200:
                    txs = await response.json()
                    if txs:
                        # Get balance
                        balance_url = api_url.replace('/txs', '')
                        async with self.session.get(balance_url) as balance_response:
                            if balance_response.status == 200:
                                balance_data = await balance_response.json()
                                balance_satoshi = balance_data.get('chain_stats', {}).get('funded_txo_sum', 0) - \
                                                balance_data.get('chain_stats', {}).get('spent_txo_sum', 0)
                                balance = balance_satoshi / (10 ** network_config.get('decimals', 8))
                                return True, len(txs), balance
                        
                        return True, len(txs), 0.0
                
                return False, 0, 0.0
                
        except Exception as e:
            logger.error(f"Bitcoin activity check error: {e}")
            return False, 0, 0.0
    
    async def _get_coin_price(self, coingecko_id: str) -> float:
        """Get current coin price from CoinGecko"""
        if not coingecko_id:
            return 0.0
        
        try:
            url = "https://api.coingecko.com/api/v3/simple/price"
            params = {
                'ids': coingecko_id,
                'vs_currencies': 'usd'
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get(coingecko_id, {}).get('usd', 0.0)
                
        except Exception as e:
            logger.error(f"Price fetch error for {coingecko_id}: {e}")
        
        return 0.0
    
    async def _apply_rate_limit(self, network_name: str):
        """Apply rate limiting per network"""
        current_time = time.time()
        last_request = self.rate_limiter.get(network_name, 0)
        rate_limit_delay = self.performance_settings['rate_limit_delay']
        
        time_since_last = current_time - last_request
        if time_since_last < rate_limit_delay:
            await asyncio.sleep(rate_limit_delay - time_since_last)
        
        self.rate_limiter[network_name] = time.time()


# Convenience functions for backward compatibility
def validate_mnemonic(mnemonic: str) -> bool:
    """Validate mnemonic phrase"""
    handler = BlockchainHandler()
    return handler.validate_mnemonic(mnemonic)


def suggest_mnemonic_corrections(words: List[str]) -> str:
    """Suggest mnemonic corrections"""
    handler = BlockchainHandler()
    return handler.suggest_mnemonic_corrections(words)
