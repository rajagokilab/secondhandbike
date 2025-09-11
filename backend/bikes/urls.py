from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BikeViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'bikes', BikeViewSet, basename='bike')

urlpatterns = [
    path('api/', include(router.urls)),  # URL will be: /api/bikes/
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
