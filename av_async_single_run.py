import aiohttp
import asyncio
import os

API_KEY = os.getenv('ALPHAVANTAGE_API_KEY')
URL = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
SYMBOL = 'AAPL'
results = []

async def run_tasks():
    session = aiohttp.ClientSession()
    responses = await session.get(URL.format(SYMBOL, API_KEY), ssl=False)
    await session.close()

asyncio.run(run_tasks())

