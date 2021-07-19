from django.contrib import admin
from myApp.models import User, Comment, Post
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
