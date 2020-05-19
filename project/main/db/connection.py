import os
import asyncpg
from datetime import datetime


class Postgres:

    def __init__(self):
        self.db_url = os.getenv('POSTGRES_URL')

    async def checkConnection(self):
        conn = await asyncpg.connect(self.db_url)
        print('\n\n', 'connection was succesfull!','\n\n', datetime.utcnow(), '\n\n\n' )
        await conn.close()

