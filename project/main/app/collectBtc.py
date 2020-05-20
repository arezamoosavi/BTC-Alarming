import httpx
from time import sleep
from db.handler import DBPostgre
from db.models import BTC_EUR, BTC_USD
from pydantic import BaseModel

pg = DBPostgre()


class BTC(BaseModel):
    amount: float


usd_btc_url= "https://api.coinbase.com/v2/prices/spot?currency=USD"
eur_btc_url= "https://api.coinbase.com/v2/prices/spot?currency=EUR"

async def getUSDBTC():
    async with httpx.AsyncClient() as client:
        r = await client.get(usd_btc_url)

    item = r.json()['data']
    btc_obj = BTC(**item)
    return btc_obj

async def getEURBTC():
    async with httpx.AsyncClient() as client:
        r = await client.get(eur_btc_url)

    item = r.json()['data']
    btc_obj = BTC(**item)
    return btc_obj

class BTCValues:
    
    @staticmethod
    async def get_save_USD():
        value = await getUSDBTC()
        saved = await pg.saveData(database=BTC_USD, data=value.dict())
        print(saved)
    
    @staticmethod
    async def get_save_EUR():
        value = await getEURBTC()
        saved = await pg.saveData(database=BTC_EUR, data=value.dict())
        print(saved)