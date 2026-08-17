from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PaymentGatewayViewSet

from .constants import (
    PAYMENT_GATEWAY_BASENAME,
    PAYMENT_GATEWAY_ROUTE,
)

router = DefaultRouter()
router.register(PAYMENT_GATEWAY_ROUTE, PaymentGatewayViewSet, basename=PAYMENT_GATEWAY_BASENAME,)

urlpatterns = router.urls