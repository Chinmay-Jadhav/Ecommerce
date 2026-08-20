from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from .serializers import (
    PaymentProcessSerializer,
    PaymentCallbackSerializer,
    )
from .services import PaymentGatewayService
from .constants import HTTPMethod
from common.serializers import MessageSerializer

# Create your views here.
class PaymentGatewayViewSet(viewsets.ViewSet) : 

    @extend_schema(
            request=PaymentProcessSerializer ,  
            responses={
                200 : MessageSerializer,
            }
    )
    @action(detail = False, methods=[HTTPMethod.POST])
    def process(self, request) : 

        serializer = PaymentProcessSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        response = PaymentGatewayService.process_payment(serializer.validated_data)

        return Response(response, status=status.HTTP_200_OK)

    @extend_schema(
            request=PaymentCallbackSerializer ,
            responses={
                200 : MessageSerializer,
                }
    )
    @action(detail=False, methods=[HTTPMethod.POST])
    def callback(self, request):

        serializer = PaymentCallbackSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        response = PaymentGatewayService.process_callback(
            serializer.validated_data
        )

        return Response(response)