import os
import logging
import faust
from app.collectBtc_first_method import BTCValues as firstBTC
from app.collectBtc_sec_method import BTCValues as secBTC

logging.basicConfig(filename='mainfaustlogfiles.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

redis_server = os.environ.get('REDIS_SERVER','redis://redis:6380/0')
kafka_broker = os.environ.get('KAFKA_SERVER', 'kafka://kafka:9092')

app = faust.App(
    version=1,
    autodiscover=True,
    origin='app',
    id="1",
    broker=kafka_broker,
    store=redis_server,
    key_serializer='json',
    value_serializer='json',
    )


test_topic = app.topic('test')


@app.task
async def on_started():
    print('MAIN APP STARTED')


# @app.timer(interval=10)
# async def fetchBitcoin():
#     await firstBTC.get_save_USD()
#     await firstBTC.get_save_EUR()

#     print('Done First Method!')


@app.timer(interval=10)
async def fetchBitcoin():
    await secBTC.get_save_USD()
    await secBTC.get_save_EUR()

    print('Done Second Method!')


