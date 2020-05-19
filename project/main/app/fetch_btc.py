import httpx
from time import sleep


btc_url= "https://api.coinbase.com/v2/prices/spot?currency=USD"

async def getBTC(times):
    while times>0:
        times += -1
        async with httpx.AsyncClient() as client:
            r = await client.get(btc_url)

        print(r.json())
        sleep(5)
