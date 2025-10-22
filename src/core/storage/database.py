"""
Database Manager
SQLite Database für Scan-Ergebnisse und Analytics
"""

import sqlite3
import logging
from typing import List, Dict, Optional, Any
from datetime import datetime
from pathlib import Path
from dataclasses import asdict

from ..blockchain.handler import ScanResult

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseManager:
    """SQLite database für storing scan results and analytics"""
    
    def __init__(self, db_path: str = "wallet_recovery.db"):
        self.db_path = Path(db_path)
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Scan results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                network TEXT NOT NULL,
                address TEXT NOT NULL,
                found BOOLEAN NOT NULL,
                transactions INTEGER DEFAULT 0,
                balance REAL DEFAULT 0.0,
                current_price REAL DEFAULT 0.0,
                usd_value REAL DEFAULT 0.0,
                symbol TEXT,
                derivation_path TEXT,
                seed_hash TEXT,
                error TEXT
            )
        ''')
        
        # Analytics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                total_scans INTEGER DEFAULT 0,
                successful_recoveries INTEGER DEFAULT 0,
                total_value_found REAL DEFAULT 0.0,
                networks_scanned TEXT,
                avg_scan_time REAL DEFAULT 0.0
            )
        ''')
        
        # Settings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL,
                encrypted BOOLEAN DEFAULT FALSE
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info(f"Database initialisiert: {self.db_path}")
    
    def save_scan_result(self, result: ScanResult, seed_hash: Optional[str] = None):
        """Save scan result to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO scan_results 
            (timestamp, network, address, found, transactions, balance, 
             current_price, usd_value, derivation_path, seed_hash, error)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            result.timestamp.isoformat(),
            result.network,
            result.address,
            result.found,
            result.transactions,
            result.balance,
            result.current_price,
            result.usd_value,
            result.derivation_path,
            seed_hash,
            result.error
        ))
        
        conn.commit()
        conn.close()
    
    def get_all_results(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get all scan results"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM scan_results 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (limit,))
        
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return results
    
    def get_successful_scans(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get only successful scans (with balance or transactions)"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM scan_results 
            WHERE found = 1 
            ORDER BY usd_value DESC 
            LIMIT ?
        ''', (limit,))
        
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return results
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get overall statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Total scans
        cursor.execute('SELECT COUNT(*) FROM scan_results')
        total_scans = cursor.fetchone()[0]
        
        # Successful recoveries
        cursor.execute('SELECT COUNT(*) FROM scan_results WHERE found = 1')
        successful = cursor.fetchone()[0]
        
        # Total value found
        cursor.execute('SELECT SUM(usd_value) FROM scan_results WHERE found = 1')
        total_value = cursor.fetchone()[0] or 0.0
        
        # By network
        cursor.execute('''
            SELECT network, COUNT(*) as count, SUM(usd_value) as value 
            FROM scan_results 
            WHERE found = 1 
            GROUP BY network
        ''')
        by_network = {row[0]: {'count': row[1], 'value': row[2]} for row in cursor.fetchall()}
        
        conn.close()
        
        return {
            'total_scans': total_scans,
            'successful_recoveries': successful,
            'total_value_found': total_value,
            'success_rate': (successful / total_scans * 100) if total_scans > 0 else 0,
            'by_network': by_network
        }
    
    def clear_all_results(self):
        """Clear all scan results (DANGEROUS!)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM scan_results')
        conn.commit()
        conn.close()
        logger.warning("Alle Scan-Ergebnisse gelöscht!")
