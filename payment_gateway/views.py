from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PaymentProcessSerializer, PaymentCallbackSerializer
from .services import PaymentGatewayService

# Create your views here.
class PaymentGatewayViewSet(viewsets.ViewSet) : 

    @action(detail = False, methods=["post"])
    def process(self, request) : 

        serializer = PaymentProcessSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        response = PaymentGatewayService.process_payment(serializer.validated_data)

        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def callback(self, request):

        serializer = PaymentCallbackSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        response = PaymentGatewayService.process_callback(
            serializer.validated_data
        )

        return Response(response)