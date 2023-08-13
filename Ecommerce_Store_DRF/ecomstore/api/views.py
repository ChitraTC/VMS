from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from .models import Clothes,Cart
# from .serializers import ClothSerializer
from rest_framework import generics, status, permissions
from .serializers import ClothSerializer , CartSerializer
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.

class ListClothes(generics.ListCreateAPIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_class ='list.html'
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClothSerializer
    queryset = Clothes.objects.all()

    #methos is used to list the products in the form of list
    def list(self,request):
        queryset = self.get_queryset()
        serializer = ClothSerializer(queryset,many=True)
        # objects={'object_list' :queryset}
        # return JsonResponse(json.dumps(objects))
        return Response(serializer.data)

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClothSerializer
    queryset = Clothes.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothSerializer(queryset, many=False)
        return Response(serializer.data)

    def patch(self,request,*args,**kwargs):
        queryset = self.get_object()
        serializer = ClothSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args, **kwargs):
        queryset = self.get_object()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try :
            product = Clothes.objects.get(id=product_id)
            cart_item = Cart(user=request.user,product=product,quantity=quantity)
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error":"Product doest not exist"},status=status.HTTP_404_NOT_FOUND)
