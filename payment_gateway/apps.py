from django.apps import AppConfig

from .constants import APP_NAME

class PaymentGatewayConfig(AppConfig):
    name = APP_NAME
