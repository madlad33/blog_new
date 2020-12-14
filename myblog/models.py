from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blogpost(models.Model):
    title=models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100,default='T-blogs')
    body=models.TextField(max_length=1000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title + ' | ' + str(self.author)




