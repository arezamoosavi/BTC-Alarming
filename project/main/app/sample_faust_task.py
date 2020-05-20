import os
import faust

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
    print('SAMPLE APP STARTED')


@app.agent(test_topic)
async def getnumber(stream):
    async for value in stream:
        print('the number is: ')
        yield value


@app.agent()
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)


from pydantic import BaseModel

class jdict(BaseModel):
    a: float
    b: float


@app.agent(test_topic)
async def getdict(dics):
    async for dic in dics:

        # dic = dict(dic)
        obj = jdict(**dic)

        print('inside: ', obj.dict())

        # yield obj.dict()
