from rest_framework import serializers

from authentications.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "phone_number", "profile_picture","role")