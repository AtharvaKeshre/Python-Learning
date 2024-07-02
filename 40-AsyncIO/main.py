import time
import asyncio

async def fun1():
    await asyncio.sleep(1)
    print("Function 1")
async def fun2():
    await asyncio.sleep(1)
    print("Function 2")
async def fun3():
    await asyncio.sleep(1)
    print("Function 3")

async def main():
    # task = asyncio.create_task(fun1())
    # # await fun1()
    # await fun2()
    # await fun3()
    L = await asyncio.gather(
        fun1(),
        fun2(),
        fun3(),
    )

asyncio.run(main())
