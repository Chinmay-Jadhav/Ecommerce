from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import OrderViewSet
from .constants import (
    ORDER_ROUTE, ORDER_BASENAME
)

router = DefaultRouter()
router.register(ORDER_ROUTE, OrderViewSet, basename=ORDER_BASENAME)

urlpatterns = router.urls