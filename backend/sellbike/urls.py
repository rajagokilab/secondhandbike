from django.urls import path
from .views import SellBikePageView, bike_valuation

urlpatterns = [
    path('', SellBikePageView.as_view(), name='sell-bike-page'),   # /sell/
    path('valuation/', bike_valuation, name='bike-valuation'),      # /sell/valuation/
]
