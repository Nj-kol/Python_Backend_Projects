from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')

if __name__ == "__main__":
    app.send_task('tasks.add', (2,2))
    app.send_task('tasks.add', (3,4))
    app.send_task('tasks.add', (6,7))
    app.send_task('tasks.add', (27,9))
    app.send_task('tasks.add', (9,45))
    app.send_task('tasks.add', (8,4))
    app.send_task('tasks.add', (11,23))
    #app.send_task("tasks.display", kwargs=dict(value="Bar"))