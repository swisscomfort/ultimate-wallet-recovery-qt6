"""
Ultimate Wallet Recovery Tool - Secure Configuration Manager
Handles environment variables, API keys, and secure settings
"""

import os
import json
import logging
from typing import Dict, Any, Optional, List
from pathlib import Path
import base64

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    CRYPTOGRAPHY_AVAILABLE = False

logger = logging.getLogger(__name__)


class ConfigManager:
    """Secure configuration manager for API keys and settings"""
    
    def __init__(self, config_file: str = "config.json", env_file: str = ".env"):
        self.config_file = Path(config_file)
        self.env_file = Path(env_file)
        self.config_data = {}
        self.env_data = {}
        self._encryption_key = None
        
        self.load_configuration()
    
    def load_configuration(self):
        """Load configuration from files and environment"""
        # Load .env file if exists
        self._load_env_file()
        
        # Load config.json
        self._load_config_file()
        
        # Override with environment variables
        self._load_environment_variables()
    
    def _load_env_file(self):
        """Load .env file"""
        if self.env_file.exists():
            try:
                with open(self.env_file, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            key, value = line.split('=', 1)
                            self.env_data[key.strip()] = value.strip()
                logger.info(f"Loaded {len(self.env_data)} environment variables from {self.env_file}")
            except Exception as e:
                logger.error(f"Error loading .env file: {e}")
    
    def _load_config_file(self):
        """Load configuration from JSON file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    self.config_data = json.load(f)
                logger.info(f"Loaded configuration from {self.config_file}")
            except Exception as e:
                logger.error(f"Error loading config file: {e}")
                self.config_data = {}
    
    def _load_environment_variables(self):
        """Load environment variables, prioritizing them over file configs"""
        env_vars = [
            'ETHERSCAN_API_KEY', 'BSCSCAN_API_KEY', 'POLYGONSCAN_API_KEY',
            'ARBISCAN_API_KEY', 'OPTIMISM_API_KEY', 'SNOWTRACE_API_KEY',
            'FTMSCAN_API_KEY', 'ENCRYPTION_PASSWORD', 'DATABASE_ENCRYPTION_KEY',
            'MAX_CONCURRENT_REQUESTS', 'REQUEST_TIMEOUT', 'RATE_LIMIT_DELAY',
            'LOG_LEVEL', 'LOG_FILE_PATH', 'BACKUP_ENABLED', 'BACKUP_LOCATION'
        ]
        
        for var in env_vars:
            # Check environment first, then .env file
            value = os.getenv(var) or self.env_data.get(var)
            if value:
                self.env_data[var] = value
    
    def get_api_key(self, service: str) -> Optional[str]:
        """Get API key for a specific service"""
        key_mapping = {
            'etherscan': 'ETHERSCAN_API_KEY',
            'bscscan': 'BSCSCAN_API_KEY',
            'polygonscan': 'POLYGONSCAN_API_KEY',
            'arbiscan': 'ARBISCAN_API_KEY',
            'optimism': 'OPTIMISM_API_KEY',
            'snowtrace': 'SNOWTRACE_API_KEY',
            'ftmscan': 'FTMSCAN_API_KEY'
        }
        
        env_key = key_mapping.get(service.lower())
        if not env_key:
            logger.warning(f"Unknown service: {service}")
            return None
        
        api_key = self.env_data.get(env_key)
        if not api_key or api_key.startswith('your_'):
            logger.warning(f"API key for {service} not configured or using placeholder")
            return None
        
        return api_key
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a setting value with fallback to default"""
        # Check environment variables first
        env_value = self.env_data.get(key.upper())
        if env_value is not None:
            return self._convert_type(env_value)
        
        # Check config file
        return self._get_nested_value(self.config_data, key, default)
    
    def _get_nested_value(self, data: Dict, key: str, default: Any) -> Any:
        """Get nested value from config using dot notation"""
        keys = key.split('.')
        current = data
        
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        
        return current
    
    def _convert_type(self, value: str) -> Any:
        """Convert string values to appropriate types"""
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value
    
    def get_network_config(self, network_name: str) -> Optional[Dict[str, Any]]:
        """Get configuration for a specific network"""
        networks = self.config_data.get('networks', [])
        for network in networks:
            if network.get('name', '').lower() == network_name.lower():
                # Add API key to network config
                api_key = self.get_api_key(network_name)
                if api_key:
                    network = network.copy()
                    network['api_key'] = api_key
                return network
        return None
    
    def get_all_networks(self) -> List[Dict[str, Any]]:
        """Get all network configurations with API keys"""
        networks = self.config_data.get('networks', [])
        result = []
        
        for network in networks:
            if network.get('enabled', True):
                network_copy = network.copy()
                api_key = self.get_api_key(network['name'])
                if api_key:
                    network_copy['api_key'] = api_key
                    result.append(network_copy)
                else:
                    logger.warning(f"No API key configured for {network['name']}")
        
        return result
    
    def get_derivation_paths(self) -> Dict[str, Any]:
        """Get derivation path configurations"""
        return self.config_data.get('derivation_paths', {})
    
    def get_themes(self) -> Dict[str, Any]:
        """Get theme configurations"""
        return self.config_data.get('themes', {})
    
    def get_security_settings(self) -> Dict[str, Any]:
        """Get security-related settings"""
        return {
            'encryption_enabled': self.get_setting('security.encryption_enabled', True),
            'encryption_algorithm': self.get_setting('security.encryption_algorithm', 'AES-256'),
            'key_derivation': self.get_setting('security.key_derivation', 'PBKDF2'),
            'iterations': self.get_setting('security.iterations', 100000),
            'secure_deletion': self.get_setting('security.secure_deletion', True),
            'memory_protection': self.get_setting('security.memory_protection', True),
            'audit_logging': self.get_setting('security.audit_logging', True),
            'session_timeout': self.get_setting('security.session_timeout', 3600)
        }
    
    def get_performance_settings(self) -> Dict[str, Any]:
        """Get performance-related settings"""
        return {
            'max_concurrent_requests': self.get_setting('MAX_CONCURRENT_REQUESTS', 5),
            'request_timeout': self.get_setting('REQUEST_TIMEOUT', 15),
            'retry_attempts': self.get_setting('performance.retry_attempts', 3),
            'rate_limit_delay': self.get_setting('RATE_LIMIT_DELAY', 1.2),
            'cache_enabled': self.get_setting('performance.cache_enabled', True),
            'cache_duration': self.get_setting('performance.cache_duration', 300),
            'batch_size': self.get_setting('performance.batch_size', 10),
            'thread_pool_size': self.get_setting('performance.thread_pool_size', 4)
        }
    
    def setup_encryption(self, password: Optional[str] = None) -> bool:
        """Setup encryption key from password or environment"""
        if not CRYPTOGRAPHY_AVAILABLE:
            logger.warning("Cryptography library not available")
            return False
            
        try:
            if not password:
                password = self.env_data.get('ENCRYPTION_PASSWORD')
            
            if not password:
                logger.warning("No encryption password provided")
                return False
            
            # Derive key from password
            salt = b'wallet_recovery_salt_2024'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
            self._encryption_key = key
            
            logger.info("Encryption key derived successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup encryption: {e}")
            return False
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data"""
        if not CRYPTOGRAPHY_AVAILABLE or not self._encryption_key:
            logger.warning("Encryption not available, returning plain data")
            return data
        
        try:
            f = Fernet(self._encryption_key)
            encrypted = f.encrypt(data.encode())
            return base64.urlsafe_b64encode(encrypted).decode()
        except Exception as e:
            logger.error(f"Encryption failed: {e}")
            return data
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        if not CRYPTOGRAPHY_AVAILABLE or not self._encryption_key:
            logger.warning("Decryption not available, returning data as-is")
            return encrypted_data
        
        try:
            f = Fernet(self._encryption_key)
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted = f.decrypt(encrypted_bytes)
            return decrypted.decode()
        except Exception as e:
            logger.error(f"Decryption failed: {e}")
            return encrypted_data
    
    def validate_configuration(self) -> Dict[str, Any]:
        """Validate configuration and return status"""
        validation_result = {
            'valid': True,
            'warnings': [],
            'errors': [],
            'api_keys_configured': 0,
            'total_api_keys': 7
        }
        
        # Check API keys
        services = ['etherscan', 'bscscan', 'polygonscan', 'arbiscan', 'optimism', 'snowtrace', 'ftmscan']
        for service in services:
            api_key = self.get_api_key(service)
            if api_key and not api_key.startswith('your_'):
                validation_result['api_keys_configured'] += 1
            else:
                validation_result['warnings'].append(f"API key for {service} not configured")
        
        # Check encryption setup
        if not self.env_data.get('ENCRYPTION_PASSWORD'):
            validation_result['warnings'].append("Encryption password not set")
        
        # Check required directories
        backup_location = self.get_setting('BACKUP_LOCATION', './backups/')
        if not Path(backup_location).exists():
            validation_result['warnings'].append(f"Backup directory does not exist: {backup_location}")
        
        log_file_path = self.get_setting('LOG_FILE_PATH', './logs/wallet_recovery.log')
        log_dir = Path(log_file_path).parent
        if not log_dir.exists():
            validation_result['warnings'].append(f"Log directory does not exist: {log_dir}")
        
        if validation_result['warnings'] or validation_result['errors']:
            validation_result['valid'] = False
        
        return validation_result
    
    def create_default_env_file(self):
        """Create a default .env file from .env.example"""
        example_file = Path('.env.example')
        if example_file.exists() and not self.env_file.exists():
            try:
                example_file.rename(self.env_file)
                logger.info(f"Created {self.env_file} from example file")
            except Exception as e:
                logger.error(f"Failed to create .env file: {e}")

# Global configuration instance
config = ConfigManager()
