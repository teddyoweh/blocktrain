from blocktrain import blocktrain
import asyncio
 
scheduler_manager = blocktrain(role="scheduler")
asyncio.run(scheduler_manager.start(host="10.66.133.208",port=55877))

 

