from django.utils import timezone

import random
import time
import uuid

from .constants import (
    PAYMENT_SUCCESS_RATE,
    PAYMENT_STATUS_SUCCESS,
    PAYMENT_STATUS_FAILED,
    PAYMENT_STATUS_PROCESSING,
)

from orders.models import Order
from orders.constants import OrderStatus

class PaymentGatewayService : 

    @staticmethod
    def process_payment(data : dict)  :

        transaction_id = f"TXN-{uuid.uuid4().hex[:10].upper()}"

        time.sleep(3)

        if random.random() < PAYMENT_SUCCESS_RATE : 
            status = PAYMENT_STATUS_SUCCESS
        else : 
            status = PAYMENT_STATUS_FAILED

        return {
            "transaction_id" : transaction_id, 
            "status" : status,
            }


    @staticmethod
    def process_callback(data : dict) : 
        order = Order.objects.get(pk = data["order_id"])

        order.payment_transaction_id = data["transaction_id"]

        if data["status"] == "SUCCESS"  :
            order.status = OrderStatus.COMPLETED
            order.payment_completed_at = timezone.now()
        else : 
            order.status = OrderStatus.FAILED

        order.save()

        return {
            "message": "Callback processed successfully."
        }
