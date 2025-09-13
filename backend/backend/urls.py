from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import os
from django.urls import path, include, re_path
from .views import FrontendAppView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('', include('bikes.urls')),
    path('sell/', include('sellbike.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/contact/', include('contact.urls')),
    re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),

]

# Serve frontend static assets before the catch-all
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=os.path.join(settings.BASE_DIR.parent, 'frontend', 'dist', 'assets')
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Catch-all route (React app)
urlpatterns += [
    re_path(r'^.*$', FrontendAppView.as_view()),

]