from rest_framework import serializers

class PaymentProcessSerializer(serializers.Serializer) : 
    order_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_method = serializers.CharField()

class PaymentCallbackSerializer(serializers.Serializer) : 
    gateway_order_id = serializers.CharField()
    payment_transaction_id = serializers.CharField()
    signature = serializers.CharField()
    # order_id = serializers.IntegerField()
    status = serializers.ChoiceField(choices=["SUCCESS", "FAILED"])