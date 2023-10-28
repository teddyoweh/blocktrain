import asyncio
from dask.distributed import Worker

async def main():
    worker = await Worker('10.66.106.228:8786')  # Replace with the address of your scheduler
    await worker.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
