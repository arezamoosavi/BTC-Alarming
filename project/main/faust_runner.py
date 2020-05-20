import logging
import asyncio
from app.sample_faust_task import app, getnumber, greet, getdict

logging.basicConfig(filename='faustLogs.log',
                    level=logging.DEBUG,
                    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

async def main():

    
    await app.start()
    print("app is running. . . . ")

    # print('1: Fasust Greeting:')
    # greeting = "1: HI First Faust Task Is Done! . . . "
    # await greet.send(value=greeting)
    # await asyncio.sleep(2)

    # print('2: Fasust Math: ')
    # print(await getnumber.ask(value=85))

    print('3: Faust dic phaze!')
    await getdict.ask(value={'a': 5, 'b': 7})




if __name__ == '__main__':

    try:
        asyncio.get_event_loop().run_until_complete(main())

        print('Sample Fasut is Done!')
        exit(1)
        
    except Exception as e:

        logging.error('Error! {}'.format(e))
        exit(0)

