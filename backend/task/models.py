from django.db import models

# Create your models here.
class Task(models.Model):
    taskName = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        if self.status == True:
            task_state = "completed"
        else:
            task_state = "not completed"

        text = "Task %s is %s" % (self.taskName, task_state)