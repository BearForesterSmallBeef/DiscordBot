import asyncio
import discord


async def work(name):
    print(f'{name} задача началась')
    await asyncio.sleep(5)
    print(f'{name} задача завершилась')


async def main():
    await asyncio.gather(
        asyncio.create_task(work("Первая")),
        asyncio.create_task(work("Вторая")),
        asyncio.create_task(work("Третья")),
    )


if __name__ == "__main__":
    asyncio.run(main())
