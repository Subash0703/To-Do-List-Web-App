from django.db import models


# Create your models here.

class MyTodoList(models.Model):
    task = models.CharField(max_length=50)
    time_interval = models.CharField(max_length=50)

    def __str__(self):
        return self.task

