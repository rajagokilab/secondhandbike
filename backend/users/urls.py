from django.urls import path
from .views import RegisterView, CustomLoginView  # import your custom login
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import MyTokenObtainPairView  # optional if using custom JWT view

urlpatterns = [
    # Registration endpoint
    path('register/', RegisterView.as_view(), name='register'),

    # Login endpoint using your custom login view
    path('login/', CustomLoginView.as_view(), name='custom_login'),

    # Optional: if you want a standard JWT login view
    # path('login/jwt/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Token refresh endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
