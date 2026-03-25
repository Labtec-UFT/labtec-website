from rest_framework import serializers

from .models import (
    Project,
    ProjectImage,
    ProjectVideo,
    Project3DFile,
    Print3DData,
    PrintStep,
)

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "order"]
        read_only_fields = ["id"]


class ProjectVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectVideo
        fields = ["id", "url", "title"]
        read_only_fields = ["id"]


class Project3DFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project3DFile
        fields = ["id", "file", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]


class Print3DDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Print3DData
        fields = ["material", "weight_grams", "print_time"]


class PrintStepSerializer(serializers.ModelSerializer):
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

