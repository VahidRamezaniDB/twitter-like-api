from django.db import models

# Create your models here.


class User(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=55)
    userName = models.CharField(max_length=40)
    passWord = models.CharField(max_length=86)
    DOB = models.DateField()

    def __str__(self):
        return self.userName
