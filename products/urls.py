from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet
from .constants  import (
    PRODUCT_ROUTE,
    PRODUCT_BASENAME
)

router = DefaultRouter()
router.register(PRODUCT_ROUTE, ProductViewSet, basename = PRODUCT_BASENAME)

urlpatterns = router.urls

