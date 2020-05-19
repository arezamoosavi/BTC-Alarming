import logging
import asyncio
from app.faust_task import app, adding, greet

logging.basicConfig(filename='faustLogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

async def main():


    await app.start()
    print("app is running. . . . ")

    import random
    print('gre:1!')
    greeting = "HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
    await greet.send(value=greeting)

    print('\n\n', 'adding: 2 . . . . ')
    print(await adding.ask(value=random.randint(1, 55)))


if __name__ == '__main__':

    try:
        asyncio.get_event_loop().run_until_complete(main())

        print('Fasut is Done!')
        exit(1)
        
    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)

