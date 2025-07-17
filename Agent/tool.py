import sqlite3
from pathlib import Path

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

DB_PATH = Path(__file__).resolve().parent.parent / "db_storage" / "crypto.db"
#print(f"DB_PATH = {DB_PATH}")

def get_top_crypto(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, symbol, current_price, market_cap 
        FROM crypto_market_data 
        ORDER BY market_cap DESC 
        LIMIT ?
    """, (limit,))
    results = cursor.fetchall()
    cursor.close()
    return results

def get_crypto_by_name(name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM crypto_market_data 
        WHERE LOWER(name) LIKE ?
        ORDER BY market_cap DESC
    """, (f"%{name.lower()}%",))
    results = cursor.fetchall()
    cursor.close()
    return results

def get_all_cryptos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, symbol, current_price, market_cap
        FROM crypto_market_data
    """)
    results = cursor.fetchall()
    cursor.close()
    return results

if __name__ == "__main__":
    top_cryptos = get_top_crypto(5)
    print("Top 5 Cryptos:")
    for crypto in top_cryptos:
        print(crypto)

    search_name = "Bitcoin"
    cryptos = get_crypto_by_name(search_name)
    print(f"\nSearch results for '{search_name}':")
    for crypto in cryptos:
        print(crypto)

if __name__ == "__main__":
    cryptos = get_all_cryptos()
    for c in cryptos[:5]:
        print(c)
