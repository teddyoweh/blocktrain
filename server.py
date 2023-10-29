from blocktrain import blocktrain
import asyncio
 
scheduler_manager = blocktrain(role="scheduler")
asyncio.run(scheduler_manager.start(host="172.20.10.6",port=55877))

 

