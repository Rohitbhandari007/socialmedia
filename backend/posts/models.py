from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    image = models.ImageField(default="", null=True, upload_to='post/image')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.title