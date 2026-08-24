from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

from products.models import Product
from payment_methods.models import PaymentMethod

from .constants import (
    OrderStatus,
    ORDER_TOTAL_PRICE_MAX_DIGITS,
    ORDER_TOTAL_PRICE_DECIMAL_PLACES,
    ORDER_STATUS_MAX_LENGTH,
    PAYMENT_TRANSACTION_ID_MAX_LENGTH ,
    GATEWAY_ORDER_ID_MAX_LENGTH , 
    )

class Order(models.Model) : 

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="orders"
        )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        related_name="orders"
        )

    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(
        max_digits=ORDER_TOTAL_PRICE_MAX_DIGITS,
        decimal_places=ORDER_TOTAL_PRICE_DECIMAL_PLACES,
        editable=False
        )
    status = models.CharField(
        max_length=ORDER_STATUS_MAX_LENGTH,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
        )

    payment_transaction_id = models.CharField(
        max_length=PAYMENT_TRANSACTION_ID_MAX_LENGTH,
        blank=True
        )
    payment_completed_at = models.DateTimeField(
        null=True,
        blank=True
        )

    gateway_order_id = models.CharField(
        max_length=GATEWAY_ORDER_ID_MAX_LENGTH,
        blank=True
        )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"