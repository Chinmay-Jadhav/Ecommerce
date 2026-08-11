from django.db import models

# Create your models here.
class PaymentMethod(models.Model)  :
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 

        ordering = ["-created_at"]

    def __str__(self):
        return self.name

"""
name : mode of payment(upi, cc, dc, cod, netbanking)
is_active : if mode is available
"""