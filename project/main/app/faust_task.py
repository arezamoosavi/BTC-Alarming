import os
import logging
import faust
from app.collectBtc import BTCValues

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


@app.timer(interval=10)
async def fetchBitcoin():
    #fn: to get data1 and save
    await BTCValues.get_save_USD()
    await BTCValues.get_save_EUR()

    print('Done First phase!')


