from django.db import models
from categories.models import Category
# from author.models import Author
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(Category) # ekta post many categories er hote pare abar onek category r ekta post hote pare
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='posts/media/uploades/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'