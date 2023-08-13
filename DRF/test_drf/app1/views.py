from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from .models import Register
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework import generics, status


# Create your views here.

class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return  Response(serializer.data)

class RegistrationView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registered successfully.'},status=201)
        return Response(serializer.errors,status=400)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return Response(status=status.HTTP_201_CREATED)




class LoginAPI(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request,email = email,password=password)
            if user is not None:
                login(request,user)
                return Response({"Message": 'Login successful'})
            else :
                return Response({"Message":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
