from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import *
from .models import User

class SignupView(APIView):
    def post(self, request):
        serializer = UserCreateRequest(data=request.data)

        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            if User.objects.filter(id=id).exists():
                return Response({"이미 존재하는 회원입니다."}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginRequest(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            if User.objects.filter(email=email, password=password).exists():
                user = User.objects.get(email=email)
                id = user.id
                return Response({'userId': id, 'message': '로그인 되었습니다.'}, status=status.HTTP_200_OK)
            return Response({'message': '아이디 또는 비밀번호가 잘못되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)