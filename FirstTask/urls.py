from django.contrib import admin
from django.urls import path, include
from user.views import login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views, name='log in'),
    path('user/', include('user.urls')),
    path('post/', include('post.urls')),
    path('comment/', include('comment.urls')),
]
