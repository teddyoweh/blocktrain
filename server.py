from blocktrain import blocktrain
import asyncio
 
scheduler_manager = blocktrain(role="scheduler")
asyncio.run(scheduler_manager.start(host="10.66.106.228",port=55877))

 

