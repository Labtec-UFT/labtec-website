from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from app.domains.projects.models import (
    Project,
    ProjectImage,
    ProjectVideo,
    Project3DFile,
    Print3DData,
    PrintStep,
)

from app.domains.projects.serializer import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectImageSerializer,
    ProjectVideoSerializer,
    Project3DFileSerializer,
    Print3DDataSerializer,
    PrintStepSerializer,
)
class PublicProjectViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_value_regex = r"\d+"

    queryset = Project.objects.filter(is_published=True).prefetch_related(
        "images",
        "videos",
        "files_3d",
        "print_steps",
        "co_creators",
    ).select_related("creator", "published_by", "print_3d_data")

    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectDetailSerializer


class ManageProjectViewSet(viewsets.ModelViewSet):
    lookup_value_regex = r"\d+"

    queryset = Project.objects.all().prefetch_related(
        "images",
        "videos",
        "files_3d",
        "print_steps",
        "co_creators",
    ).select_related("creator", "published_by", "print_3d_data")

    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectDetailSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        if "is_published" in serializer.validated_data:
            published_by = self.request.user if serializer.validated_data.get("is_published") else None
            serializer.save(published_by=published_by)
            return

        serializer.save()


class ProjectImageViewSet(viewsets.ModelViewSet):
    lookup_value_regex = r"\d+"
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAdminUser]


class ProjectVideoViewSet(viewsets.ModelViewSet):
    lookup_value_regex = r"\d+"
    queryset = ProjectVideo.objects.all()
    serializer_class = ProjectVideoSerializer
    permission_classes = [IsAdminUser]


class Project3DFileViewSet(viewsets.ModelViewSet):
    lookup_value_regex = r"\d+"
    queryset = Project3DFile.objects.all()
    serializer_class = Project3DFileSerializer
    permission_classes = [IsAdminUser]


class Print3DDataViewSet(viewsets.ModelViewSet):
    lookup_value_regex = r"\d+"
    queryset = Print3DData.objects.all()
    serializer_class = Print3DDataSerializer
    permission_classes = [IsAdminUser]


class PrintStepViewSet(viewsets.ModelViewSet):
    lookup_value_regex = r"\d+"
    queryset = PrintStep.objects.all()
    serializer_class = PrintStepSerializer
    permission_classes = [IsAdminUser]
