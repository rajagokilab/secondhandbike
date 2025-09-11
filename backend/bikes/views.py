# from rest_framework import viewsets
# from .models import Bike
# from .serializers import BikeSerializer

# class BikeViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Bike.objects.all()
#     serializer_class = BikeSerializer
# views.py
from rest_framework import viewsets
from .models import Bike
from .serializers import BikeSerializer

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


