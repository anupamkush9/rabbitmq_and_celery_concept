# Create your tasks here

from celery import shared_task

@shared_task
def add(x, y):
    import time
    print("##########################3")
    time.sleep(5)
    print("add mehtod is running =======================")
    print( x + y)
    return x+y
