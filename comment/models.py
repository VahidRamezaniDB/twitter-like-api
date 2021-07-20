from django.db import models


class Comment(models.Model):
    content = models.TextField()
    date = models.DateField()
    userId = models.IntegerField(editable=False)
    likes = models.IntegerField()
    disLikes = models.IntegerField()
    upperComment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def like(self):
        self.likes += 1

    def dislike(self):
        self.disLikes += 1
