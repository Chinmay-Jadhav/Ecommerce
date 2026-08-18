from rest_framework import serializers

from .constants import (
    MAX_AMOUNT_PRICE,
    AMOUNT_DECIMAL_PLACES,
    PAYMENT_STATUS_SUCCESS,
    PAYMENT_STATUS_FAILED,

)

class PaymentProcessSerializer(serializers.Serializer) : 
    order_id = serializers.IntegerField()
    amount = serializers.DecimalField(
        max_digits=MAX_AMOUNT_PRICE, 
        decimal_places=AMOUNT_DECIMAL_PLACES
        )
    payment_method = serializers.CharField()

class PaymentCallbackSerializer(serializers.Serializer) : 
    gateway_order_id = serializers.CharField()
    payment_transaction_id = serializers.CharField()
    signature = serializers.CharField()
    status = serializers.ChoiceField(
        choices=[
            PAYMENT_STATUS_SUCCESS,
            PAYMENT_STATUS_FAILED
            ]
        )