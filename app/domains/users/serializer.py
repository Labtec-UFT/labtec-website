import re
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
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
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está cadastrado.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("A senha deve ter pelo menos 6 caracteres.")
        return value

    def validate_full_name(self, value):
        pattern = r'^[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Informe nome e sobrenome válidos."
            )
        return value

    def validate_phone_number(self, value):
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