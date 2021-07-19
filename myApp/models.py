from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=55)
    userName = models.CharField(max_length=40)
    passWord = models.CharField(max_length=86)
    DOB = models.DateField()


class Post(models.Model):
    content = models.TextField()
    date = models.DateField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    likes = models.IntegerField()
    disLikes = models.IntegerField()

    def like(self):
        self.likes += 1

    def dislike(self):
        self.disLikes += 1


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
