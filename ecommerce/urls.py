from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_spectacular.views import (
    SpectacularAPIView ,
    SpectacularSwaggerView ,
    SpectacularRedocView ,
    )

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/", include("products.urls")),
    path("api/v1/", include("accounts.urls")),
    path("api/v1/", include("payment_methods.urls")),
    path("api/v1/", include("orders.urls")),
    path("api/v1/", include("payment_gateway.urls")),

    path(
        "api/schema/" ,
        SpectacularAPIView.as_view() ,
        name='schema' 
        ) ,
    path(
        "api/schema/swagger-ui/" ,
        SpectacularSwaggerView.as_view(url_name='schema') ,
        name='swagger-ui'
        ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name = 'schema'),
        name='redoc'
    ),

]
