from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def create(self, email, nickname, password):
        user = User.objects.create(
            email=email,
            password=password,
            nickname=nickname
        )

        user.save()

        return user

class UserCreateRequest(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128)
    nickname = serializers.CharField(max_length=20)

class UserLoginRequest(serializers.Serializer):
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128)