from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserCreateRequest(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128)
    nickname = serializers.CharField(max_length=20)

class UserLoginRequest(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128)