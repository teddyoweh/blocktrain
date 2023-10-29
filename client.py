from blocktrain import cluster
import asyncio
from func import prime_factors
if __name__ == "__main__":
    
    scheduler_address = "10.66.106.228:55877"
    cluster = cluster(scheduler_address)
    asyncio.run(cluster.start())
    # worker_ips = cluster.view_worker_ips()
    # print("Worker IP addresses:")
    # for ip in worker_ips:
    #     print(ip)
    results = cluster.distribute_function(prime_factors,100000000000000000000100000000000000000000100000000000000000000100000000000000000000)
    print(results)

 
    cluster.close()