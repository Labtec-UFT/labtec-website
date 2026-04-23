from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError

from app.service.UploadService import UploadService
from app.service.ValidationService import ValidationService

from .models import (
    Project,
    ProjectImage,
    ProjectVideo,
    Project3DFile,
    Print3DData,
    PrintStep,
)

class ProjectImageSerializer(serializers.ModelSerializer):
    def validate_image(self, value):
        try:
            UploadService.validate_file(value, context="projects.image")
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages)
        return value

    class Meta:
        model = ProjectImage
        fields = ["id", "image", "order"]
        read_only_fields = ["id"]


class ProjectVideoSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=True)

    class Meta:
        model = ProjectVideo
        fields = ["id", "url", "title"]
        read_only_fields = ["id"]


class Project3DFileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, min_length=3)

    def validate_file(self, value):
        try:
            UploadService.validate_file(value, context="projects.files_3d")
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.messages)
        return value

    class Meta:
        model = Project3DFile
        fields = ["id", "file", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]


class Print3DDataSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        try:
            ValidationService.validate_print_3d_data(attrs)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.message_dict if hasattr(exc, "message_dict") else exc.messages)
        return attrs

    class Meta:
        model = Print3DData
        fields = ["material", "weight_grams", "print_time"]


class PrintStepSerializer(serializers.ModelSerializer):
    description = serializers.CharField(min_length=5)

    class Meta:
        model = PrintStep
        fields = ["id", "step_number", "description"]
        read_only_fields = ["id"]

#Essa serializer vai aninhar apenas os campos essenciais para cards e listagens, sem os detalhes de imagens, vídeos e arquivos 3D. 
# Para detalhes completos, usaremos a ProjectDetailSerializer.
class ProjectListSerializer(serializers.ModelSerializer):
    """Serializer para listagem de projetos."""

    creator = serializers.StringRelatedField()
    cover_image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "short_description",
            "project_type",
            "creator",
            "cover_image",
            "is_published",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def get_cover_image(self, obj):
        first = obj.images.first()
        if first:
            request = self.context.get("request")
            return request.build_absolute_uri(first.image.url) if request else first.image.url
        return None

# Essa serializer inclui todos os detalhes do projeto, incluindo imagens, vídeos, arquivos 3D e dados de impressão 3D.
class ProjectDetailSerializer(serializers.ModelSerializer):
    """Serializer completo para criação, edição e detalhe de um projeto."""

    creator = serializers.StringRelatedField(read_only=True)
    published_by = serializers.StringRelatedField(read_only=True)
    co_creators = serializers.StringRelatedField(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    videos = ProjectVideoSerializer(many=True, read_only=True)
    files_3d = Project3DFileSerializer(many=True, read_only=True)
    print_3d_data = Print3DDataSerializer(read_only=True)
    print_steps = PrintStepSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "short_description",
            "description",
            "project_type",
            "creator",
            "co_creators",
            "published_by",
            "images",
            "videos",
            "files_3d",
            "print_3d_data",
            "print_steps",
            "is_published",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, attrs):
        payload = {
            "title": attrs.get("title", getattr(self.instance, "title", "")),
            "short_description": attrs.get(
                "short_description", getattr(self.instance, "short_description", "")
            ),
            "description": attrs.get("description", getattr(self.instance, "description", "")),
            "is_published": attrs.get("is_published", getattr(self.instance, "is_published", False)),
        }

        try:
            ValidationService.validate_project_payload(payload)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(exc.message_dict if hasattr(exc, "message_dict") else exc.messages)

        return attrs

