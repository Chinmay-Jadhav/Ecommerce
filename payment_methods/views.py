from django.shortcuts import render

from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response

from .models import PaymentMethod
from .serializers import PaymentMethodSerializer


class PaymentMethodViewSet(viewsets.ModelViewSet)  :
    permission_classes = [permissions.IsAuthenticated]
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter] 
    search_fields = ["name"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]
