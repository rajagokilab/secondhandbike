# from django.db import models

# class Bike(models.Model):
#     year = models.IntegerField(default=2020)
#     model = models.CharField(max_length=100, default="Unknown Model")
#     specs = models.CharField(max_length=255, blank=True, default="")
#     mileage = models.IntegerField(default=0)
#     owner = models.CharField(max_length=50, default="Unknown Owner")
#     price = models.IntegerField(default=0)
#     location = models.CharField(max_length=100, default="Unknown Location")
#     image = models.ImageField(upload_to='bikes/', blank=True, null=True)
#     brand = models.CharField(max_length=50, default="Unknown Brand")
#     fuel = models.CharField(max_length=20, default='Petrol')
#     category = models.CharField(max_length=50, default="Motorcycle")
#     color = models.CharField(max_length=50, default="Unknown")
#     booked = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.model} ({self.year})"
from django.db import models

class Bike(models.Model):
    year = models.IntegerField(default=2020)
    model = models.CharField(max_length=100, default="Unknown Model")
    specs = models.CharField(max_length=255, blank=True, default="")
    mileage = models.IntegerField(default=0)
    owner = models.CharField(max_length=50, default="Unknown Owner")
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default="Unknown Location")
    image = models.ImageField(upload_to='bikes/', blank=True, null=True)
    brand = models.CharField(max_length=50, default="Unknown Brand")
    fuel = models.CharField(max_length=20, default='Petrol')
    category = models.CharField(max_length=50, default="Motorcycle")
    color = models.CharField(max_length=50, default="Unknown")
    booked = models.BooleanField(default=False)
    warranty = models.CharField(max_length=100, blank=True, default="")
    insurance = models.CharField(max_length=100, blank=True, default="")
    registration_no = models.CharField(max_length=50, blank=True, default="")
    chassis_no = models.CharField(max_length=50, blank=True, default="")
    engine_no = models.CharField(max_length=50, blank=True, default="")
    service_history = models.TextField(blank=True, default="")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


# Add BikeImage here, **below the Bike model**
class BikeImage(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='bikes/')

    def __str__(self):
        return f"Image for {self.bike.model}"

