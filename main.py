from celery import Celery

app = Celery('main')
app.config_from_object('celeryconfig')

@app.task
def your_task():
    
    result = "This is the result of your task"
    return result

if __name__ == '__main__':
    result = your_task.delay()  
    task_result = result.get()  
    print(task_result)  
