from rest_framework import serializers
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import NewsModel, NewsImage

ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif']


class NewsImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        required=True,
        allow_empty_file=False,
    )
    description = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        min_length=3
    )

    class Meta:
        model = NewsImage
        fields = ["id", "image", "description", "is_cover", "order", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_order(self, value):
        if value < 0:
            raise serializers.ValidationError("O campo 'order' não pode ser negativo.")
        return value

    def validate_image(self, image):
        if image.content_type not in ALLOWED_IMAGE_TYPES:
            raise serializers.ValidationError(
                f"Tipo de arquivo não permitido. Tipos aceitos: {', '.join(ALLOWED_IMAGE_TYPES)}"
            )
        return image

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, required=False)
    author = serializers.StringRelatedField(read_only=True)

    title = serializers.CharField(
        required=True,
        max_length=255,
        min_length=5,
        error_messages={
            "blank": "O título não pode ficar vazio.",
            "min_length": "O título deve ter ao menos 5 caracteres.",
            "max_length": "O título não pode ter mais de 255 caracteres."
        }
    )
    description = serializers.CharField(
        required=False,
        max_length=100,
        min_length=10,
        allow_null=True,
        error_messages={
            "min_length": "A descrição deve ter ao menos 10 caracteres.",
            "max_length": "A descrição não pode ter mais de 100 caracteres."
        }
    )

    content = serializers.CharField(
        required=True,
        min_length=10,
        error_messages={
            "blank": "O conteúdo não pode ficar vazio.",
            "min_length": "O conteúdo deve ter ao menos 10 caracteres."
        }
    )
    summary = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        min_length=10,
        error_messages={
            "min_length": "O resumo deve ter ao menos 10 caracteres.",
            "max_length": "O resumo não pode ter mais de 255 caracteres."
        }
    )
    external_link = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[URLValidator(message="URL inválida.")]
    )

    class Meta:
        model = NewsModel
        fields = [
            "id", "title", "description", "content", "summary", "external_link",
            "created_at", "updated_at", "is_published", "published_at",
            "author", "images"
        ]
        read_only_fields = ["id", "created_at", "updated_at", "published_at", "author"]

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        news = NewsModel.objects.create(**validated_data)

        for image_data in images_data:
            NewsImage.objects.create(news=news, **image_data)

        return news

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data is not None:
            existing_images = {img.id: img for img in instance.images.all()}
            for image_data in images_data:
                img_id = image_data.get("id", None)
                if img_id and img_id in existing_images:
                    for attr, val in image_data.items():
                        setattr(existing_images[img_id], attr, val)
                    existing_images[img_id].save()
                else:
                    NewsImage.objects.create(news=instance, **image_data)

        return instance