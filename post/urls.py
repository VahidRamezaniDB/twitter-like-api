from django.urls import path
from .views import PostViews

urlpatterns = [
    path('details/<int:pk>', PostViews.as_view()),
    path('create/', PostViews.as_view()),
    path('delete/<int:pk>', PostViews.as_view()),
    path('like/<int:pk>', PostViews.as_view())
]