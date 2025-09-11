from django.contrib import admin
from .models import Bike

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'brand', 'price', 'owner', 'booked')
    list_filter = ('brand', 'category', 'fuel', 'year', 'color', 'booked')
    search_fields = ('model', 'brand', 'location')
