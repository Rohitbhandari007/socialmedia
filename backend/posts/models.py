from django.db import models
from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    liked = models.ManyToManyField(User, blank=True, related_name='postlikes')
    details = models.TextField(blank=True)
    image = models.ImageField(default="", null=True, upload_to='post/image')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='postauthor')
    date_updated = models.DateTimeField(auto_now=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.liked.count()
