from rest_framework import serializers

from .models import News, NewsImage

#Essa serializer é para as imagens associadas a uma notícia, usada no detalhe da notícia e na criação/edição.
class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ["id", "image", "description", "created_at"]
        read_only_fields = ["id", "created_at"]

#Essa serializer vai aninhar apenas os campos essenciais para cards e listagens, sem os detalhes de imagens. 
# Para detalhes completos, usaremos a NewsDetailSerializer.
class NewsListSerializer(serializers.ModelSerializer):
    """Serializer para listagem de notícias."""

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "summary",
            "cover_image",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

# Essa serializer inclui todos os detalhes da notícia, incluindo as imagens associadas.
class NewsDetailSerializer(serializers.ModelSerializer):
    """Serializer completo para criação, edição e detalhe de uma notícia."""

    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "content",
            "summary",
            "cover_image",
            "images",
            "is_published",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]