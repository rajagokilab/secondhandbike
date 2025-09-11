# bikes/api_urls.py
from django.urls import path
from .views import bike_valuation

urlpatterns = [
    path('valuation/', bike_valuation, name='bike-valuation'),
]
