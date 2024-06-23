from django.db import models
import datetime
from category.models import TaskCategory
# Create your models here.


class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(default=datetime.date.today)
    task=models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.taskTitle
