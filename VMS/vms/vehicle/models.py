from django.db import models

v_types = [
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
]

class VehicleModel(models.Model):
    vehicle_number = models.CharField(max_length=50)
    vehicle_type = models.CharField(
        max_length = 50,
        choices=v_types,
        default='2'
        )
    vehicle_model = models.CharField(max_length=200)
    vehicle_description = models.TextField()