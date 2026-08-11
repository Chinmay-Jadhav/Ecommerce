from django.urls import path, include



from . import views

urlpatterns = [
    path('products/', include('products.urls')),
    path('auth/', include("accounts.urls")),
    path("payment-methods/", include("payment_methods.urls")),
    path("orders/", include("orders.urls")),
]