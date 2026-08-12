from django.apps import AppConfig

from .constants import APP_NAME

class PaymentMethodsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = APP_NAME
