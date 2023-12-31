# Create your views here.
from itertools import product

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


@api_view(['Get'])
def api_overview(request):
    api_urls = {
        'List': '/product/list',
        'Detail view': '/product/details/<ink:id>',
        'Create': '/product/create/',
        'Delete': '/product/delete/<int:id>',
        'Update': '/product/update/<int:id>',
    }
    return Response(api_urls)


# list
@api_view(['Get'])
def showall(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


# create
@api_view(['Post'])
def createproduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# detail view
@api_view(['Get'])
def detailview(request,pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

#delete
@api_view(['Delete'])
def deleteview(request,pk):
    products = Product.objects.get(id=pk)
    products.delete()
    serializer = ProductSerializer(products, many=False)
    return Response('Item deleted successfully')

#update
@api_view(['Post'])
def updateview(request,pk):
    products=Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=products,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

