from django.shortcuts import render

from rest_framework import status, viewsets, filters, permissions
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product
from .paginations import CustomPagination


class ProductViewSet(viewsets.ModelViewSet) : 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['@name']

    ordering_fields = ['created_at']
    ordering = ["-created_at"]