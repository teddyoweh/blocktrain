import asyncio
from dask.distributed import Scheduler

async def main():
    scheduler = Scheduler(host='10.66.106.228', port=8786)
    await scheduler.start()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
