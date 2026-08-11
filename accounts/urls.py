from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
                                            )

from .views import RegisterAPIView

urlpatterns = [
    # Simple-JWT endpoints
    path('login/', TokenObtainPairView.as_view(), name='login'),  
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path("register/", RegisterAPIView.as_view(), name="register"),   
]
