from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"
    PROCESSING = "PROCESSING", "Processing"

APP_NAME = "orders"

INVALID_QUANTITY_ERROR = "Quantity must be greater than zero."
PAYMENT_METHOD_INACTIVE_ERROR = "Selected payment method is unavailable"
INSUFFICIENT_STOCK_ERROR = "Requested quantity exceeds available stocks."

ORDER_ROUTE = "orders"
ORDER_BASENAME = "orders"