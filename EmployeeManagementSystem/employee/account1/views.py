from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import RegisterSerializer, UserSerializer, LoginSerializers


# Create your views here.


class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        return Response(serializer.data)

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializers(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        if not user:
            return Response({
                'status': False,
                'message': 'invalid credentials'
            }, status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'status': True, 'message': 'user login successful', 'token': str(token)}, status.HTTP_200_OK)
from django.shortcuts import render
