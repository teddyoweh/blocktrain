import dask.distributed
import asyncio
import tracemalloc
import subprocess
import sys
tracemalloc.start()
class blocktrain:
    def __init__(self, role, scheduler_address=None):
        self.role = role
        self.scheduler_address = scheduler_address

    async def start(self,host,port):
        scheduler = dask.distributed.Scheduler(host=host,port=port)
        await scheduler.start()
        print(f"Dask scheduler address: {scheduler.address}")
        await asyncio.gather(scheduler.finished())
 


class slave:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.start_worker()

    def check_and_install_dask(self):
        try:
            import dask
            import distributed
        except ImportError:
            self.install_dask_dependencies()
    def install_dask_dependencies(self):
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'dask', 'dask[distributed]'])
        except Exception as e:
            print(f"Failed to install Dask dependencies: {str(e)}")
            sys.exit(1)

    def start_worker(self):
        self.check_and_install_dask()

        cmd = f"python3 -m dask worker {self.host}:{self.port}"

        try:
            subprocess.check_call(cmd, shell=True)
        except Exception as e:
            print(f"Failed to start Dask worker: {str(e)}")
import asyncio
import dask.distributed

class cluster:
    def __init__(self, scheduler_address):
        self.scheduler_address = scheduler_address
        self.client = None
    async def start(self):
        self.client = dask.distributed.Client(self.scheduler_address)

    def view_worker_ips(self):
        if self.client is not None:
            worker_info = self.client.scheduler_info()["workers"]
            worker_ips = [info["host"] for info in worker_info.values()]
            return worker_ips
        else:
            return []
    def distribute_function(self, func,*args, **kwargs):
        if self.client is not None:
            futures = [self.client.submit(func, *args, **kwargs, workers=worker)
                       for worker in self.client.scheduler_info()["workers"]]
            results = self.client.gather(futures)
            return results[0] if results else None  
        else:
            return None
    def close(self):
        if self.client is not None:
            self.client.close()
    


