from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
    )
from drf_spectacular.types import OpenApiTypes

from .serializers import (
    UserRegistrationSerializer,
    )
from .constants import USER_REGISTERED_SUCCESSFULLY
from common.serializers import MessageSerializer

# class UserRegistrationAPIView(APIView) : 

#     @extend_schema(
#             summary="Register a new user" ,
#             description="Creates a new user account." , 
#             request=UserRegistrationSerializer,
#             responses={
#                 201 : MessageSerializer ,
#             },
#     )
#     def post(self, request) : 
#         user = request.data
#         serializer = UserRegistrationSerializer(data = user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(
#             {
#                 "message" : USER_REGISTERED_SUCCESSFULLY
#                 },
#             status=status.HTTP_201_CREATED,
#         )


class UserRegistrationViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
) :
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message" : USER_REGISTERED_SUCCESSFULLY ,
            } ,
            status=status.HTTP_201_CREATED,
            headers= headers,
        )