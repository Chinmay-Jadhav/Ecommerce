from django.db import transaction

from rest_framework import serializers

from .models import Order

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
        ]

        read_only_fields = [
            "id",
            "total_price",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate(self,attrs) :

        product = attrs["product"]
        payment_method = attrs["payment_method"]
        quantity = attrs["quantity"]

        if quantity <= 0 :
            raise serializers.ValidationError(
                {
                    "quantity" : "Quantity must be greater than zero."
                }
            )

        if not payment_method.is_active :
            raise serializers.ValidationError(
                {
                    "payment_method" : "Selected method is unavailable"
                }
            )

        if quantity > product.stock  :
            raise serializers.ValidationError(
                {
                    "quantity" : "Requested quantity exceeds available stocks."
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

        order = Order.objects.create(
            user=user,
            total_price = total_price,
            **validated_data    # product + payment_method + quantity
        )

        return order

    