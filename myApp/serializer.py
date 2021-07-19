from abc import ABC

from django.conf import settings
from rest_framework import serializers
from .models import User, Post, Comment


class PostActionSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    action = serializers.CharField()


class CommentActionSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
    id = serializers.IntegerField()
    action = serializers.CharField()


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['content',
                  'date',
                  'user',
                  'like',
                  'dislike']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
