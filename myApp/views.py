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
from serializer import postActionSerializer


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.


def home(req): pass


def login_view(request): pass


def register_view(request): pass


def create_post_view(request):
    pass


def edit_post_view(request): pass


def action_post_view(request):
    serializer = postActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        post_id = data.get('id')
        action = data.get('action')
        content = data.get('content')



def comment_post_view(request): pass


def comment_comment_view(request): pass


def like_post_view(request): pass


def dislike_post_view(request): pass


def like_comment_view(request): pass


def dislike_comment_view(request): pass
