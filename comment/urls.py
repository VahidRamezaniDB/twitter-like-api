from django.urls import path
from views import CommentView


urlpatterns = [
    path('create/', CommentView.as_view()),
    path('delete/', CommentView.as_view()),
    path('details/', CommentView.as_view()),
    path('like/', CommentView.as_view()),
]
