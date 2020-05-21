import httpx
from time import sleep
from pydantic import BaseModel
from db.dtQuery import pgQuery


pg = pgQuery()


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
        await BTCValues.make_noise(database='btc_usd', currValue=value)
        saved = await pg.saveData(database='btc_usd', record=value.amount)
        print(saved)
    
    @staticmethod
    async def get_save_EUR():
        value = await getEURBTC()
        await BTCValues.make_noise(database='btc_eur', currValue=value)
        saved = await pg.saveData(database='btc_eur', record=value.amount)
        print(saved)

    @staticmethod
    async def make_noise(database, currValue):
        print(database, 'is used! for get Last')
        prevValue = await pg.getLast(database=database)
        if prevValue < currValue.amount:
            print('hoyyyyyyyyyyyyyyyyy')
            print('\n'*10, ' UPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
    