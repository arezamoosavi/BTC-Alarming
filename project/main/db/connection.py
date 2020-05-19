import os
import asyncpg
from datetime import datetime


class Postgres:

    def __init__(self):
        self.db_url = os.getenv('POSTGRES_URL')

    async def checkConnection(self):
        conn = await asyncpg.connect(self.db_url)
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS testusers(
                id serial PRIMARY KEY,
                name text,
                dob date
                    )
                ''')

        # Insert a record into the created table.
        await conn.execute('''
            INSERT INTO testusers(name, dob) VALUES($1, $2)
            ''', 'Bob', datetime.utcnow())

        # Select a row from the table.
        row = await conn.fetchrow(
            'SELECT * FROM testusers WHERE name = $1', 'Bob')
        
        print(row, type(row))

        # Drop Table
        query = "DROP TABLE IF EXISTS {} CASCADE;".format("testusers")
        await conn.execute(query)

        print('\n\n', 'connection was succesfull!','\n\n', datetime.utcnow(), '\n\n\n' )
        await conn.close()