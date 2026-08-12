from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
                                            )

from .views import UserRegistrationAPIView
from .constants import (
    LOGIN_NAME, LOGIN_PATH,
    REFRESH_NAME, REFRESH_PATH,
    REGISTER_NAME, REGISTER_PATH
)

urlpatterns = [
    # Simple-JWT endpoints
    path(LOGIN_PATH, TokenObtainPairView.as_view(), name=LOGIN_NAME),  
    path(REFRESH_PATH, TokenRefreshView.as_view(), name=REFRESH_NAME),
    path(REGISTER_PATH, UserRegistrationAPIView.as_view(), name=REGISTER_NAME),   
]
