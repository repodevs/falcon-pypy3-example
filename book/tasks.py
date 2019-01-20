import os
from time import sleep
from dynaconf import settings as conf

import celery


CELERY_BROKER = conf.get('CELERY_BROKER')
CELERY_BACKEND = conf.get('CELERY_BACKEND')

app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)


@app.task
def fib(n):
    sleep(2) # simulate slow computation
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        results = fib(n - 1)
        results.append(results[-1] + results[-2])
        return results

