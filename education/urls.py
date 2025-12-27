"""
URL configuration for education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from app.views import CustomTokenObtainPairView, react_app
from django.urls import re_path

urlpatterns = [
    re_path(r'^/*admin/', admin.site.urls),
    re_path(r'^/*api/', include('app.urls')),   # Connect app routes
    re_path(r'^/*api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^/*api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from django.conf import settings
from django.conf.urls.static import static

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Catch-all route for React app - MUST be at the end
# Regex avoids intercepting static, media, api, and admin routes
urlpatterns += [
    re_path(r'^(?!.*(?:admin/|api/|static/|media/)).*$', react_app),
]

