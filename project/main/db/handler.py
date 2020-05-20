import os
from tortoise import Tortoise
from db.models import BTC_EUR, BTC_USD

db_url = os.getenv('POSTGRES_URL')

class DBPostgre:
    
    @staticmethod
    async def create_all():
        await Tortoise.init(db_url=db_url, modules={"models": ["db.models"]})
        await Tortoise.generate_schemas()

        print("all EUR: ")
        print(await BTC_EUR.all())
        
        print("all USD: ")
        print(await BTC_USD.all())
    
    async def addData(database, data):
        pass
    