from django.db import models
from user.models import User
from post.models import Post


class Comment(models.Model):
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, default=0)
    disLikes = models.IntegerField(null=True, default=0)
    upperComment = models.ForeignKey('Comment', on_delete=models.CASCADE, default=None, blank=True)
    upperPost = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, blank=True)

    def __str__(self):
        return self.content[:15]+'...'

    def like(self):
        self.likes += 1

    def dislike(self):
        self.disLikes += 1
