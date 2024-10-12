from celery.task import task

@task
def add(x, y):
    return x + y

@task
def display(value):
    print(f'Hooray! I am running Celery. Value from user is {value}')