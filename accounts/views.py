from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer

class RegisterAPIView(APIView) : 

    def post(self, request) : 
        user = request.data
        serializer = RegisterSerializer(data = user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message" : "User registered successfully."
                },
            status=status.HTTP_201_CREATED,
        )