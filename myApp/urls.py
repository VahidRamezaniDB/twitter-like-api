from django.contrib import admin
from django.urls import path
from views import (create_post_view,
                   dislike_post_view,
                   comment_post_view,
                   delete_post_view,
                   like_comment_view,
                   dislike_comment_view,
                   login_view,
                   like_post_view,
                   edit_post_view,
                   comment_comment_view,
                   home,
                   register_view)
urlpatterns = [
    path('', home, name='home'),
    path('<int:post_id>/delete/', delete_post_view),
    path('<int:user_id>/delete/', create_post_view),
    path('<int:post_id>/delete/', delete_post_view),
    path('<int:post_id>/delete/', delete_post_view),
    path('<int:post_id>/delete/', delete_post_view),
    path('<int:post_id>/delete/', delete_post_view),
    path('<int:post_id>/delete/', delete_post_view),
]