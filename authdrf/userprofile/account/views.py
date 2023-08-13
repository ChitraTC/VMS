from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User
from .serializer import RegisterSerializer,UserSerializer
from rest_framework import generics, status


# Create your views here.
class RegisterView(generics.CreateAPIView):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.object.get_or_created(user=user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
