import logging
import asyncio
from app.fetch_btc import getBTC

logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(getBTC(times=3))
        exit(1)

    except Exception as e:
        logging.error('Error! {}'.format(e))
        exit(0)

