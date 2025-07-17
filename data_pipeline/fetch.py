# pipeline/fetch.py

import aiohttp
import asyncio
import os
from datetime import datetime
from pathlib import Path
import orjson

import ssl
import certifi


RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {"accept": "application/json"}
BASE_URL = "https://api.coingecko.com/api/v3"

async def fetch(session, url):
    async with session.get(url, headers=HEADERS) as response:
        response.raise_for_status()
        return await response.json()

async def save_json(data, name):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filepath = RAW_DIR / f"{name}_{timestamp}.json"
    with open(filepath, "wb") as f:
        f.write(orjson.dumps(data))
    print(f"[Saved] {name} → {filepath.name}")

async def fetch_trending(session):
    url = f"{BASE_URL}/search/trending"
    data = await fetch(session, url)
    await save_json(data, "trending")

async def fetch_market_data(session):
    url = f"{BASE_URL}/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    data = await fetch(session, url)
    await save_json(data, "market_data")

async def main():
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    
    connector = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(connector=connector) as session:
        await asyncio.gather(
            fetch_trending(session),
            fetch_market_data(session)
        )

if __name__ == "__main__":
    asyncio.run(main())
