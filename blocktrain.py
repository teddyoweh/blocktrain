from celery import Celery

app = Celery('main')
app.conf.broker_url = 'redis://172.20.10.10:6379/0'
app.conf.result_backend = 'redis://172.20.10.10:6379/0'
