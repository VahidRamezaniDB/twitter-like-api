from abc import ABC

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLogInSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=86)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass