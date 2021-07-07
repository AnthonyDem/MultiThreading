import asyncio
import time


async def timer():
    print('tick')
    await asyncio.sleep(1)
    print('tock')
    return 'tick tock'


async def tick():
    await asyncio.sleep(1)
    return 'tick'


async def tock():
    await asyncio.sleep(2)
    return 'tock'


async def tick_tock_handler():
    start = time.perf_counter()
    t1 = asyncio.create_task(tick())
    t2 = asyncio.create_task(tock())

    for i, t in enumerate(asyncio.as_completed((t1, t2)), start=1):
        result = await t
        exec_time = time.perf_counter() - start
        print(f' {result} executed in {exec_time}')


async def main():
    t1 = asyncio.create_task(timer())
    t2 = asyncio.ensure_future(timer())

    results = await asyncio.gather(t1, t2)

    print(f' {t1.get_name()} Done - {t1.done()}')
    print(f' {t2.get_name()} Done - {t2.done()}')

    for i in results:
        print(i)


if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(tick_tock_handler())