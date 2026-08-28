from django.conf import settings

from celery import shared_task 

import time
import requests
import json
import decimal

from .models import Order
from payment_gateway.constants import PAYMENT_GATEWAY_PATH

class NumberStr(float) : 
    def __init__(self, o):
        self.o = o
    def __repr__(self):
        return str(self.o)

def decimal_serializer(o) : 
    if isinstance(o, decimal.Decimal) : 
        return NumberStr(o)
    raise TypeError(f"{repr(o)} is not JSON serializable")

@shared_task
def process_order(order_id : int)  :
    order = Order.objects.get(pk=order_id)

    process_payload = {
            "order_id" : order_id ,
            "amount" : order.total_price ,  
            "payment_method" : order.payment_method.name ,
        }

    payload = json.dumps(
        process_payload,
        default=decimal_serializer,
    )

    process_response = requests.post(
        f"{settings.BASE_URL}{PAYMENT_GATEWAY_PATH}",
        data=payload,
        headers={
            'Content-Type': 'application/json',
            'Accept' : 'application/json'
            },
    )

    process_response.raise_for_status()

    data = process_response.json()

    order.gateway_order_id = data["gateway_order_id"]

    order.save(
        update_fields=[
            "gateway_order_id" ,
            ]
        )


