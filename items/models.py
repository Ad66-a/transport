from django.db import models

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_type

# Create your models here.
