
from django.urls import path

from app1 import views

urlpatterns = [
    path('api_overview/',views.api_overview,name='overview'),
    path('product_list/', views.showall, name='Product_list'),
    path('product_create/',views.createproduct,name='product_create'),
    path('product_details/<int:pk>',views.detailview,name='product_detail'),
    path('product_delete/<int:pk>',views.deleteview,name='product_delete'),
    path('product_update/<int:pk>',views.updateview,name='product_update')


]