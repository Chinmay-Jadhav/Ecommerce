from django.utils import timezone

import uuid

from .constants import (
    PAYMENT_STATUS_CREATED,
    DUMMY_SIGNATURE,
)

from orders.models import Order
from orders.constants import OrderStatus

class PaymentGatewayService : 

    @staticmethod
    def process_payment(data : dict)  :

        gateway_order_id = f"ORDER-{uuid.uuid4().hex[:12].upper()}"

        return {
            "gateway_order_id" : gateway_order_id, 
            "status" : PAYMENT_STATUS_CREATED
            }


    @staticmethod
    def process_callback(data : dict) : 

        if data["signature"] != DUMMY_SIGNATURE  :
            return {
                "message" : "Invalid signature ."
            }

        order = Order.objects.get(
            gateway_order_id = data["gateway_order_id"]
                                  )

        order.payment_transaction_id = data["payment_transaction_id"]

        if data["status"] == "SUCCESS"  :
            order.status = OrderStatus.COMPLETED
            order.payment_completed_at = timezone.now()
        else : 
            order.status = OrderStatus.FAILED

        order.save()

        return {
            "message": "Callback processed successfully."
        }
