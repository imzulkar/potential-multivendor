from rest_framework import serializers, validators
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from authentications.models import User, VendorInformation


class NewUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            validators.UniqueValidator(
                queryset=User.objects.all(),
                message="This email is already in use. Please use a different email.",
            )
        ],
    )

    password1 = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
        required=True,
        label="Retype Password",
    )

    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    # vendor informations
    business_name = serializers.CharField(required=False, write_only=True)
    business_email = serializers.EmailField(required=False, write_only=True)
    vendor_address = serializers.CharField(required=False, write_only=True)
    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "role",
            "profile_picture",
            # vendor fields
            "business_name",
            "business_email",
            "vendor_address",
        ]

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise validators.ValidationError(
                {
                    "password1": "Password Doesn't Match",
                }
            )
        if attrs.get("role")=="VENDOR":
            if not attrs.get("business_name") and not attrs.get("business_email") and not attrs.get('vendor_address'):
                raise validators.ValidationError(
                    "Business name, Email , address required"
                )

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        email = validated_data["email"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        phone_number = validated_data["phone_number"]
        profile_picture = validated_data["profile_picture"]
        user = User.objects.create(
            email=email,first_name=first_name, last_name=last_name, phone_number=phone_number,profile_picture=profile_picture
        )
        user.set_password(validated_data["password1"])
        user.save()
        self.update_vendor_information(user, validated_data)
        return user

    def update_vendor_information(self,user, validated_data):
        business_name = validated_data.get("business_name")
        business_email = validated_data.get("business_email")
        vendor_address = validated_data.get("vendor_address")

        vendor = VendorInformation.objects.create(user=user, business_name=business_name,business_email=business_email, address=vendor_address)
        return vendor
