import os
import asyncpg
from datetime import datetime

class pgQuery:
    def __init__(self):
        self.db_url = os.getenv('POSTGRES_URL')
    
    async def saveData(self, database, record):  #database='btc_usd',record=85858

        conn = await asyncpg.connect(self.db_url)
        query = '''INSERT INTO {}(amount, created_at) VALUES($1, $2)'''.format(database)
        await conn.execute(query, record, datetime.utcnow())
        await conn.close()
        return 'SAVED to ASyncPg!'

    
    async def getLast(self, database): #database='btc_usd'
        
        conn = await asyncpg.connect(self.db_url)
        row = await conn.fetch('SELECT amount FROM {}'.format(database))
        await conn.close()
        try:
            data = dict(row[-1])
            print('FRom dtQuery.GetLast: ', data)
            return float(data['amount'])
        except Exception as e:
            print('Error! {}'.format(e))
            return 0
        