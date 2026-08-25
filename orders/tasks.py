from django.conf import settings

from celery import shared_task 

import time
import requests

from .models import Order
from payment_gateway.constants import PAYMENT_GATEWAY_PATH

@shared_task
def process_order(order_id : int)  :
    order = Order.objects.get(pk=order_id)

    process_payload = {
            "order_id" : order_id ,
            "amount" : order.total_price ,  
            "payment_method" : order.payment_method.name ,
        }

    process_response = requests.post(
        f"{settings.BASE_URL}{PAYMENT_GATEWAY_PATH}",
        json=process_payload,
    )

    process_response.raise_for_status()

    data = process_response.json()

    order.gateway_order_id = data["gateway_order_id"]

    order.save(
        update_fields=[
            "gateway_order_id" ,
            ]
        )


