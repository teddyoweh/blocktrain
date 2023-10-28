# tasks.py

from celery import Celery

app = Celery('myapp', broker='tcp://172.20.10.10:6379/0')

@app.task
def my_task(task_input):
    # Your task code here
    result = task_input * 2
    return result
