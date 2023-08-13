from django.db import models


# Create your models here.
from account.models import User
# from ecomstore.account.models import User


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Clothes(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='clothes', on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    price = models.FloatField(null=True, blank=True)
    image_url = models.URLField(max_length=2083)
    clothes_available = models.BooleanField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Clothes,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)