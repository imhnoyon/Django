from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    classes=models.CharField(max_length=20)
    address=models.TextField(default='jamalpur')

    def __str__(self):
        return f'Roll:{self.roll} ={self.name}'