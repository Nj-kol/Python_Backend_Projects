
# Celery Demos

* A Celery applications has three components :
  1. A Celery Client
  2. A Broker
  3. One or more Celery Workers

# About the demo project 

## Start Celery Worker(s)

* Format

```bash
celery worker --app $APP \
--broker $BROKER_URL \
--loglevel=info
```

the app name would be the name of the python module containing code for the worker

* Example

```bash
cd ${PROJECT_LOCATION}/my_celery_app

celery worker --app my_worker \
--broker "redis://10.159.21.107:30379/0" \
--loglevel=info
```

# Notes 

* To start celery worker, you have to install the python *celery* package on that machine ( ```pip install celery``` )
* The name of the *app* must be the python module. Here *my_worker* ( rather my_worker.py ) is a python module :

```python
from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
```

* By convention, all the configuration for celery apps (both client and worker) are stored in a file called *celeryconfig.py*
* The *--broker* flag is required only if it has not been specified in the *celeryconfig.py*. So, for example, if all configuration
  is mentioned in the config file, starting the worker is as simple as :

   ```celery worker --app my_worker --loglevel=info```

* The workers need all the code for the tasks you want to run on them. The code for Celery worker *must* be present on different remote machines and started *individually* 

* Both client and worker should have the Celery client

#### Multiple workers

* When you start Multiple workers on different nodes :

  - The Nodes will discover each other

    ```
    [2020-07-24 15:17:33,245: INFO/MainProcess] mingle: searching for neighbors
    [2020-07-24 15:17:34,270: INFO/MainProcess] mingle: sync with 1 nodes
    [2020-07-24 15:17:34,270: INFO/MainProcess] mingle: sync complete
    [2020-07-24 15:17:34,287: INFO/MainProcess] celery@<machine_ip> ready
    ```

  - The tasks will get divided amongst multiple workers

    For example, if you have 6 tasks and two workers then each workers will get 3 tasks

    For an odd number of tasks or works, the distribution is not deterministic but more or less the tasks tend to 
    get distributed evenly among workers

## Start Celery Client

```bash
cd ${PROJECT_LOCATION}/celery_client
python client.py
```

#### Sending arguments to remote functions

* In the case of a distributed system with multiple different applications and repositories, each repository might have its own Celery Worker and its own tasks. You can’t use python to import the task from one code base to another.

* In this case, ***we don’t require the actual function to be imported into our client code***, you only need to provide two things :
 1. The task name
 2. The actual arguments

* There are two ways you can send arguments to remote tasks :

1. Using tuples

This is the simplest way to send the arguments in the order defined in the task function

For example -

For a task defined as :

```python
@task
def add(x, y, z):
    print(f"X is {x}, Y is {y}, Z is {z}")
    return x + y + z
```

In the remote client, you can send call the function as :

```python
app.send_task('tasks.add', (9,45,90))
```

* In the worker logs, you can clearly see the values gets assigned correctly to the variables in an orderly fashion

```bash
[2020-07-24 12:57:52,636: INFO/MainProcess] Received task: tasks.add[4d5ef913-7a07-4169-9a6d-7f9b5ac1c24b]
[2020-07-24 12:57:52,637: WARNING/ForkPoolWorker-7] X is 9, Y is 45, Z is 90
[2020-07-24 12:57:52,637: INFO/ForkPoolWorker-7] Task tasks.add[4d5ef913-7a07-4169-9a6d-7f9b5ac1c24b] succeeded in 0.0002993911039084196s: 144
```

2. Using kwargs

```bash
app.send_task('tasks.add', kwargs={'x': 1, 'y': 2, 'z': 3})
```

* In the worker logs, you can clearly see the values gets assigned correctly to the variables in an orderly fashion

```bash
[2020-07-24 13:04:59,637: INFO/MainProcess] Received task: tasks.add[f9db9ba4-2134-4b9f-a308-826df4be9c1b]
[2020-07-24 13:04:59,639: WARNING/ForkPoolWorker-7] X is 1, Y is 2, Z is 3
[2020-07-24 13:04:59,639: INFO/ForkPoolWorker-7] Task tasks.add[f9db9ba4-2134-4b9f-a308-826df4be9c1b] succeeded in 0.0002810859587043524s: 6
```

Notes 
=====
* The client submits the task(s) to the *Remote Task Queue* (Redis or RabbitMQ)

References
==========
https://docs.celeryproject.org/en/stable/

https://coderbook.com/@marcus/how-to-send-celery-messages-to-remote-worker/

https://stackoverflow.com/questions/18433071/celery-how-to-send-task-from-remote-machine
https://docs.celeryproject.org/en/stable/userguide/calling.html
