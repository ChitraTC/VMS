from django.shortcuts import render
from  django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from rest_framework import generics
from rest_framework import serializers
from .serializers import EmpSerializer


class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmpSerializer
    queryset = Employee.objects.all()
    # to list
    def get(self,request):
        queryset = self.get_queryset()
        serializer = EmpSerializer(queryset, many=True)
        return Response(serializer.data)

    #     to create Employee

    def post(self, request):
        serializer = EmpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmpSerializer
    queryset = Employee.objects.all()

    #to get detail of particular employee
    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmpSerializer(queryset, many=False)
        return Response(serializer.data)

    #to update
    def patch(self,request,*args,**kwargs):
        queryset = self.get_object()
        serializer = EmpSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #to delete

    def delete(self,request,*args, **kwargs):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

