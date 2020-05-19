import faust

# redis_server = os.environ.get('REDIS_SERVER')
# kafka_broker = os.environ.get('KAFKA_SERVER')

app = faust.App(
    version=1,
    autodiscover=True,
    origin='app',
    id="1",
    broker='kafka://kafka:9092',
    store='redis://redis:6379/0',
    key_serializer='json',
    value_serializer='json',
    )


test_topic = app.topic('test')


@app.task
async def on_started():
    print('APP STARTED')

@app.timer(interval=10)
async def every_minute():
    print(await adding.ask(value=5))


@app.agent(test_topic)
async def adding(stream):
    async for value in stream:
        print('the number is: ')
        yield value



@app.agent()
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)