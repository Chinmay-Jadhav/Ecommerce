from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/", include("products.urls")),
    path("api/v1/", include("accounts.urls")),
    path("api/v1/", include("payment_methods.urls")),
    path("api/v1/", include("orders.urls")),
    path("api/v1/", include("payment_gateway.urls")),
]
