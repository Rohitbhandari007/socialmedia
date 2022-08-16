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
        ordering = ['-id']

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        return self.liked.count()


class Comment(models.Model):
    body = models.TextField()
    liked = models.ManyToManyField(
        User, blank=True, related_name="comment_likes")
    author = models.ForeignKey(
        User, related_name="authors", on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name="parent_post", on_delete=models.CASCADE)
    created = models.DateTimeField(
        auto_now_add=True)
    isEdited = models.BooleanField(default=False, blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='parentchild')

    def __str__(self):
        return str(self.body[:15])

    @property
    def is_parent(self):
        return True if self.parent is None else False

    @property
    def like_comment(self):
        return self.liked.count()

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created').all()
