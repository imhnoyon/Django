from django.db import models
# Create your models here.


class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryName
