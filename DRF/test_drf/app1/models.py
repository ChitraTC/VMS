from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=300)
    phone_num = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=300)