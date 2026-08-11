from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Order.objects.filter(user = self.request.user)

