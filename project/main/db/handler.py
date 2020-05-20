import os
from tortoise import Tortoise
from db.models import BTC_EUR, BTC_USD

db_url = os.getenv('POSTGRES_URL')

class DBPostgre:

    def __init__(self):
        self.db_url = os.getenv('POSTGRES_URL')
    
    async def initdb(self):
        await Tortoise.init(db_url=self.db_url, modules={"models": ["db.models"]})
        await Tortoise.generate_schemas()

    async def checkall(self):
        await self.initdb()
        print("all EUR: ")
        print(await BTC_EUR.all())
        
        print("all USD: ")
        print(await BTC_USD.all())
    

    async def saveData(self, database, data):
        await self.initdb()
        btc = await database.create(**data)
        print('SAVED to USD_BTC table!!')
        return btc