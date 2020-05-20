import httpx
from time import sleep
from pydantic import BaseModel
from db.handler import DBPostgre
from db.models import BTC_USD

pg = DBPostgre()

class BTC(BaseModel):
    amount: float

async def printHandler(item: BTC):
    btc_obj = BTC(**item)
    gg = await pg.saveData(database=BTC_USD, data=btc_obj.dict())
    print('SAVED! Hoooooooooooooooooora')
    print(gg)
    
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
