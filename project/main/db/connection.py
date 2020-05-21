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
        
        print(dict(row), type(row))

        # test ideas:1
        print('------test idea1---------')
        record=('Ali',datetime.utcnow())
        await conn.execute('''
            INSERT INTO testusers(name, dob) VALUES($1, $2)
            ''', record[0], record[1])
        allrow = await conn.fetch('SELECT name FROM testusers')
        print(allrow, type(allrow))

        print([dict(row) for row in allrow])
        print('# test ideas:1 :::::SAVED to USD_BTC table!!')

        # test ideas:2
        print('------test idea2---------')
        db = 'testusers'
        trow = await conn.fetch('SELECT name FROM {}'.format(db))
        print(trow[-1])
        print('# test ideas:2 :::::Got it!!')


        # test ideas:3
        print('------test idea3---------')
        record=('Alireza',datetime.utcnow())
        que = '''INSERT INTO {}(name, dob) VALUES($1, $2)'''.format('testusers')
        await conn.execute(que, record[0], record[1])

        allrow = await conn.fetch('SELECT name FROM {}'.format('testusers'))
        print(allrow, type(allrow))
        print([dict(row) for row in allrow])
        print('# test ideas:3 :::::Worked!!')


        # Drop Table
        query = "DROP TABLE IF EXISTS {} CASCADE;".format("testusers")
        await conn.execute(query)

        print('\n\n', 'connection was succesfull!','\n\n', datetime.utcnow(), '\n\n\n' )
        await conn.close()