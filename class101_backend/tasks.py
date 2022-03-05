from celery import Celery

# app = Celery('celery_start')
# app.config_from_object('celery_config.py')
app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

import time

@app.task
def add(x, y):
    return x + y

@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)
