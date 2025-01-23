from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from ..utils import generate_otp
from ..models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, allow_blank=False, allow_null=True)
    confirm_password = serializers.CharField(
        max_length=255, allow_blank=False, allow_null=True
    )

    class Meta:
        model = CustomUser
        fields = [
            "user_id",
            "email",
            "username",
            "password",
            "confirm_password",
            "created_at",
        ]
        read_only_fields = ["user_id", "created_at"]

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"password": "Incorrect password"})
        return data

    def create(self, validated_date):
        email = validated_date.get("email")
        username = validated_date.get("username")
        password = validated_date.get("password")

        user = CustomUser.objects.create_user(email=email, username=username)
        user.set_password(password)
        user.is_active = True
        user.save()

        return user

    # def save(self, **kwargs):

    #     user = self.create(self.validated_data)

    #     otp = generate_otp()
    #     email_subject = "Activate your account"
    #     email_body = (
    #         f"Hi {user.username}, you otp code is {otp} and expires in 120 seconds "
    #     )
    #     if self.instance is None:
    #         return
    #     try:
    #         send_mail(
    #             email_subject,
    #             email_body,
    #             "emailtest119@yahoo.com",
    #             [user.email],
    #             fail_silently=False,
    #         )
    #     except Exception as e:
    #         raise serializers.ValidationError(
    #             {"email": f"Failed to send OTP: {str(e)}"}
    #         )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("password")
        representation.pop("confirm_password")
        return representation


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(allow_blank=False)
    password = serializers.CharField(max_length=255)
    lookup_field = "user_id"

    def create(self):
        user = self.context.get("user")

        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
        return {
            "token": token.key,
            "email": user.email,
            "username": user.username,
        }

    def save(self, **kwargs):
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        user = authenticate(email=email, password=password)

        if not user:
            raise ValidationError({"error": "Invalid email or password"})

        self.context["user"] = user
        return self.create()
