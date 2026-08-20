from django.shortcuts import render

from rest_framework import mixins, viewsets

from .serializers import UserRegistrationSerializer
from .constants import USER_REGISTERED_SUCCESSFULLY


class UserRegistrationViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
) :
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {
            "message" : USER_REGISTERED_SUCCESSFULLY
        }

        return response