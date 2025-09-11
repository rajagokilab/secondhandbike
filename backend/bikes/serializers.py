
# serializers.py
from rest_framework import serializers
from .models import Bike, BikeImage

class BikeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeImage
        fields = ["id", "image"]

class BikeSerializer(serializers.ModelSerializer):
    images = BikeImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bike
        fields = "__all__"
