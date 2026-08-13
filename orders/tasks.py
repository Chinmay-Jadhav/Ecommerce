from celery import shared_task 

import time

from .models import Order
from .constants import OrderStatus


# @shared_task
# def process_order(order_id:int) : 
#     print(f"Processing Order : {order_id}")

#     time.sleep(10)  #simulation

#     order = Order.objects.get(pk=order_id)

#     print(f"Payment completed for Order : {order.id}")

#     return f"Order {order.id} processed. "

@shared_task
def process_order(order_id : int)  :
    order = Order.objects.get(pk=order_id)

    try  :
        order.status = OrderStatus.PROCESSING
        order.save(update_fields=["status"])

        #simulation
        time.sleep(10)

        order.status = OrderStatus.COMPLETED
        order.save(update_fields=["status"])

    except Exception : 
        order.status = OrderStatus.CANCELLED
        order.save(update_fields=["status"])
        raise

