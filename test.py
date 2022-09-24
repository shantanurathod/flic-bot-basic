from db import find
import asyncio

async def main():
    member = await find({"email":"21bcv009@ietdavv.edu.in"})
    print(member)
    print(type(member))
    x = str(member)
    print(x)
    print(type(x))

asyncio.run(main())

