from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PaymentMethodViewSet
from .constants import (
    PAYMENT_METHOD_BASENAME,
    PAYMENT_METHOD_ROUTE
    )

router = DefaultRouter()
router.register(PAYMENT_METHOD_ROUTE, PaymentMethodViewSet, basename=PAYMENT_METHOD_BASENAME)

urlpatterns = router.urls