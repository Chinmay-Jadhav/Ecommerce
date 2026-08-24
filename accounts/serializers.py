
from rest_framework import serializers

from .constants import PASSWORD_NOT_MATCHING
                        
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer) : 
    confirm_password = serializers.CharField(write_only = True)

    class Meta : 
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {
            "password" : {
                "write_only" : True
            }
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"] : 
            raise serializers.ValidationError(
                {"confirm_password" : PASSWORD_NOT_MATCHING}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")                  # already used for validation...not needed anymore
        user = User.objects.create_user(**validated_data)
        return user


    