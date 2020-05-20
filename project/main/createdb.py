from tortoise import run_async
from db.handler import DBPostgre
import logging

logging.basicConfig(filename='logfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")



if __name__ == "__main__":

    try:
        run_async(DBPostgre.create_all())

        print('DBs are created!')

        exit(1)
    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)