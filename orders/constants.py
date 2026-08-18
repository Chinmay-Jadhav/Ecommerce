from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"
    PROCESSING = "PROCESSING", "Processing"
    FAILED = "FAILED", "Failed"

APP_NAME = "orders"

INVALID_QUANTITY_ERROR = "Quantity must be greater than zero."
PAYMENT_METHOD_INACTIVE_ERROR = "Selected payment method is unavailable"
INSUFFICIENT_STOCK_ERROR = "Requested quantity exceeds available stocks."

ORDER_ROUTE = "orders"
ORDER_BASENAME = "orders"

ORDER_TOTAL_PRICE_MAX_DIGITS = 10
ORDER_TOTAL_PRICE_DECIMAL_PLACES = 2

ORDER_STATUS_MAX_LENGTH = 20
PAYMENT_TRANSACTION_ID_MAX_LENGTH = 100
GATEWAY_ORDER_ID_MAX_LENGTH = 100