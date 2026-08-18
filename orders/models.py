from django.db import models
from django.contrib.auth.models import User

from products.models import Product
from payment_methods.models import PaymentMethod

from .constants import OrderStatus

class Order(models.Model) : 

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, related_name="orders")

    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    payment_transaction_id = models.CharField(max_length=100, blank=True)
    payment_completed_at = models.DateTimeField(null=True, blank=True)

    gateway_order_id = models.CharField(max_length=100, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"