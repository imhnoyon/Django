from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    Bio=models.TextField()
    phone_No=models.CharField(max_length=11)

    def __str__(self):
        return self.name