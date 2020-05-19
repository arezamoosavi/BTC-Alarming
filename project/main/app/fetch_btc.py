import httpx
from time import sleep
from db.db_handler import BTC

async def printHandler(item: BTC):
    btc_obj = BTC(**item)
    print(btc_obj, '  from pydantic! \n')


btc_url= "https://api.coinbase.com/v2/prices/spot?currency=USD"

async def getBTC(times):
    while times>0:
        times += -1
        async with httpx.AsyncClient() as client:
            r = await client.get(btc_url)


        jr = r.json()
        print(jr, '\n\n')
        await printHandler(jr['data'])
        sleep(5)
