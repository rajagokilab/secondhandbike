from django.db import models

class Contact(models.Model):
    REASON_CHOICES = [
        ('buy', 'Buy a bike'),
        ('sell', 'Sell a bike'),
        ('support', 'Customer Support'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    find_out = models.CharField(max_length=50, blank=True)  # maps from frontend findOut
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.reason}"
