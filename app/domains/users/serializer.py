from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'full_name',
            'phone_number',
            'is_staff',
            'is_superuser',
            'is_active',
            'profile_picture',
        ]
        extra_kwargs = {
            'is_staff':     {'read_only': True},
            'is_superuser': {'read_only': True},
            'is_active':    {'read_only': True},
        }

    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return obj.profile_picture.url
        return None

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(password=password, **validated_data)
        return user
