from celery import Celery
 

app = Celery('myapp')
app.conf.broker_transport_options = {
    'custom_tcp': {
        'host': '172.20.10.10',
        'port': 6379,  # Replace with your custom server's port
    }
}
app.conf.broker_url = 'custom_tcp://'

@app.task
def my_task(task_input):
    # Your task code here
    result = task_input * 2
    return result
