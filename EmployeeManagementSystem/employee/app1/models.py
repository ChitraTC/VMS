from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_name = models.CharField(max_length=250,blank=False)
    emp_id = models.CharField(max_length=250,blank=False)
    emp_dept = models.ForeignKey(Department, related_name='employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
