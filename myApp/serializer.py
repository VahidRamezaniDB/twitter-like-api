from abc import ABC

from django.conf import settings
from rest_framework import serializers
from .models import User, Post, Comment


class postActionSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    content = serializers.CharField(allow_blank=True, required=False)
    action = serializers.CharField()

