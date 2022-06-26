from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    image = models.ImageField(default="", null=True, upload_to='post/image')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
