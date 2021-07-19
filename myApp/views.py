from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User, Post, Comment
from serializer import (PostActionSerializer,
                        PostSerializer,
                        CommentActionSerializer,
                        CommentSerializer)


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.


def home(req): pass


def login_view(request): pass


def register_view(request): pass


def create_post_view(request):
    pass


def action_post_view(request):
    serializer = PostActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        post_id = data.get('id')
        action = data.get('action')

        post = Post.objects.get(id=post_id)

        if action == "like":
            post.like()
            serializer = PostSerializer(post)
            return Response(serializer.data, status=200)

        elif action == "dislike":
            post.dislike()
            serializer = PostSerializer(post)
            return Response(serializer.data, status=200)

        elif action == "delete":
            post.delete()
            return Response({}, status=200)


def action_comment_view(request):
    serializer = CommentActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        comment_id = data.get('id')
        action = data.get('action')

        comment = Comment.objects.get(id=comment_id)
        if action == "like":
            comment.like()
            new_ser = CommentSerializer(comment)
            return Response(new_ser.data, status=200)

        elif action == "dislike":
            comment.dislike()
            new_ser = CommentSerializer(comment)
            return Response(new_ser.data, status=200)

        elif action == "delete":
            comment.delete()
            return Response({}, status=200)


def comment_post_view(request): pass


def comment_comment_view(request): pass


def like_comment_view(request): pass


def dislike_comment_view(request): pass
