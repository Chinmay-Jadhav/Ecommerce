from django.conf import settings

from celery import shared_task 

import time
import requests

from .models import Order
from .constants import OrderStatus

@shared_task
def process_order(order_id : int)  :
    order = Order.objects.get(pk=order_id)

    process_payload = {
        "order_id" : order.id ,
        "amount" : str(order.total_price) ,
        "payment_method" : order.payment_method.name ,
    }

    process_response = requests.post(
        f"{settings.BASE_URL}/api/v1/payment-gateway/process/",
        json=process_payload ,
    )

    process_data = process_response.json()

    callback_payload = {
        "order_id" : order.id ,
        "transaction_id" : process_data["transaction_id"] ,
        "status" : process_data["status"] ,
    }

    requests.post(
        f"{settings.BASE_URL}/api/v1/payment-gateway/callback/" ,
        json=callback_payload ,
    )

    # try  :
    #     order.status = OrderStatus.PROCESSING
    #     order.save(update_fields=["status"])

    #     #simulation
    #     time.sleep(10)

    #     order.status = OrderStatus.COMPLETED
    #     order.save(update_fields=["status"])

    # except Exception : 
    #     order.status = OrderStatus.CANCELLED
    #     order.save(update_fields=["status"])
    #     raise

