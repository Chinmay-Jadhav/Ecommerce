from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
# from .tasks import test_task

class OrderViewSet(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Order.objects.filter(user = self.request.user)


# class TestCeleryAPIView(APIView) :
#     def get(self, request) :
#         test_task.delay()

#         return Response(
#             {"message" : "Task sent to Celery worker."}
#         )

