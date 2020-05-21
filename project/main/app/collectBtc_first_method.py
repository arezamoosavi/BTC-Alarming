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

    try:
        item = r.json()['data']
        btc_obj = BTC(**item)
        return btc_obj
    except Exception as e:
        print('Error! {}'.format(e))
        return 0

async def getEURBTC():
    async with httpx.AsyncClient() as client:
        r = await client.get(eur_btc_url)
    try:
        item = r.json()['data']
        btc_obj = BTC(**item)
        return btc_obj
    except Exception as e:
        print('Error! {}'.format(e))
        return 0

class BTCValues:
    
    @staticmethod
    async def get_save_USD():
        value = await getUSDBTC()
        await BTCValues.make_noise(database=BTC_USD, currValue=value)
        saved = await pg.saveData(database=BTC_USD, data=value.dict())
        print(saved)
    
    @staticmethod
    async def get_save_EUR():
        value = await getEURBTC()
        await BTCValues.make_noise(database=BTC_EUR, currValue=value)
        saved = await pg.saveData(database=BTC_EUR, data=value.dict())
        print(saved)

    @staticmethod
    async def make_noise(database, currValue):
        prevValue = await pg.getLast(database=database)
        if prevValue.amount < currValue.amount:
            print('hoyyyyyyyyyyyyyyyyy')
            print('\n'*10, ' UPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
    