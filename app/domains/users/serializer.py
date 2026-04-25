import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()
    get_full_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "phone_number",
            "is_staff",
            "is_superuser",
            "is_active",
            "profile_picture",
            "get_full_name",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
            "is_active": {"read_only": True},
        }

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url
        return None

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User.objects.create_user(password=password, **validated_data)
        return user


        pattern = r'^[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Informe nome e sobrenome válidos."
            )
        return value

    def validate(self, attrs):
        login = attrs.get("login")
        password = attrs.get("password")

        pattern = r'^55\d{11}$'

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Telefone deve estar no formato: 5563999999999"
            )

        if user is None:
            raise serializers.ValidationError("Usuário ou senha inválidos")

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token)
        }
