import logging
import asyncio
from db.connection import Postgres


logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

async def main():

    conn = Postgres()
    await conn.checkConnection()



if __name__ == "__main__":
    
    try:
        asyncio.get_event_loop().run_until_complete(main())
        
        exit(1)

    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)
