import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=8)
    profile_picture = serializers.ImageField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'password',
            'full_name',
            'phone_number',
            'is_staff',
            'is_superuser',
            'is_active',
            'profile_picture',
        ]

        extra_kwargs = {
            'is_staff': {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_active': {'read_only': True},
        }

    def validate_email(self, value):
        queryset = User.objects.filter(email=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Este email já está cadastrado.")
        return value

    def validate_password(self, value):
        try:
            validate_password(value, self.instance)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages)
        return value

    def validate_full_name(self, value):
        if not value:
            raise serializers.ValidationError("Nome completo é obrigatório.")

        pattern = r'^[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Informe nome e sobrenome válidos."
            )
        return value

    def validate_phone_number(self, value):
        if value in (None, ""):
            return value

        pattern = r'^55\d{11}$'

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Telefone deve estar no formato: 5563999999999"
            )

        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user