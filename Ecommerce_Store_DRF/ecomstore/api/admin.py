from django.contrib import admin

# Register your models here.
from .models import Clothes, Category, Cart

admin.site.register(Clothes)
admin.site.register(Category)
admin.site.register(Cart)