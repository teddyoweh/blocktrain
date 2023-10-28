from celery import Celery

app = Celery('main')
host = "172.20.10.10"
#host = "0.0.0.0"
app.conf.broker_url = f'redis://{host}:6379/0'
app.conf.result_backend = f'redis://{host}:6379/0'

 