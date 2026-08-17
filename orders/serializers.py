from django.db import transaction

from rest_framework import serializers

from .models import Order
from .tasks import process_order
from .constants import (
    INSUFFICIENT_STOCK_ERROR,
    PAYMENT_METHOD_INACTIVE_ERROR
)

class OrderSerializer(serializers.ModelSerializer)  :

    class Meta : 
        model = Order
        fields = [
            "id",
            "product",
            "payment_method" , 
            "quantity" , 
            "total_price" , 
            "status" , 
            "created_at" , 
            "updated_at" ,
            "payment_transaction_id" , 
            "payment_completed_at" ,
        ]

        read_only_fields = [
            "id",
            "total_price",
            "status",
            "created_at",
            "updated_at",
            "payment_transaction_id",
            "payment_completed_at",
        ]

    def validate(self,attrs) :

        product = attrs["product"]
        payment_method = attrs["payment_method"]
        quantity = attrs["quantity"]

        if not payment_method.is_active :
            raise serializers.ValidationError(
                {
                    "payment_method" : PAYMENT_METHOD_INACTIVE_ERROR
                }
            )

        if quantity > product.stock  :
            raise serializers.ValidationError(
                {
                    "quantity" : INSUFFICIENT_STOCK_ERROR
                }
            )

        return attrs

    # @transaction.atomic
    def create(self, validated_data):
        product = validated_data["product"]
        quantity = validated_data["quantity"]

        total_price = product.price * quantity

        user = self.context["request"].user

        product.stock -= quantity
        product.save()

        #override create() because additional logic is executed before and after obj creation

        order = Order.objects.create(
            user=user,
            total_price = total_price,
            **validated_data    # product + payment_method + quantity
        )

        process_order.delay(order.id)

        return order

    