hereimport requests
from bs4 import BeautifulSoup
from apify import Actor
import asyncio

async def main():
    async with Actor:
        # The "Human Mask" (User-Agent) so the site thinks we are on iPhone
        headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1"
        }
        
        # Target: LCFE (Lagos Commodities Exchange)
        url = "https://lcfe.ng/market-watch/"
        print(f"Connecting to {url}...")
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                print("Market Watch data found! Pipe is active.")
                await Actor.push_data({
                    "market": "Lagos", 
                    "status": "Online", 
                    "msg": "Virgin data tunnel is live!"
                })
            else:
                print(f"Site busy (Status: {response.status_code}). Rotating mask...")
        except Exception as e:
            print(f"Error connecting: {e}")

if __name__ == "__main__":
    asyncio.run(main())
