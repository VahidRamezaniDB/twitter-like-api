from django.urls import path
from .views import CommentView


urlpatterns = [
    path('create/', CommentView.as_view()),
    path('delete/<int:pk>', CommentView.as_view()),
    path('details/<int:pk>', CommentView.as_view()),
    path('like/<int:pk>', CommentView.as_view()),
]
