from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
from blog_new.util import unique_slug_generator
from ckeditor.fields import RichTextField

class Blogpost(models.Model):
    title=models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100)
    # body=models.TextField(max_length=1000000000)
    body=RichTextField(blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now_add=True)
    categories=models.CharField(max_length=100)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    like=models.ManyToManyField(User,related_name='likes')
    snippet=models.CharField(max_length=300)
    images=models.ImageField(blank=True,null=True,upload_to='images/')
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail',args=str((self.id)))

    def total_likes(self):
        return self.like.count()

    def total_like_after_dislike(self):
        if self.like:
            self.like-=1
            return self.like.count()
        else:
            return self.like.count()



def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(pre_save_receiver, sender=Blogpost)


class Categories(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('home')