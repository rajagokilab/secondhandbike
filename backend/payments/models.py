from django.db import models
from django.conf import settings  # important!
from bikes.models import Bike  # your Bike model

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # use settings.AUTH_USER_MODEL
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.user.username} - {self.bike.model} - {self.amount}"
