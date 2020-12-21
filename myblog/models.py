from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
class Blogpost(models.Model):
    title=models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail',args=str((self.id)))


