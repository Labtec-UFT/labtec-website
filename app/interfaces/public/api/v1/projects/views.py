from rest_framework import viewsets, permissions
from django.db.models import Prefetch

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


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().prefetch_related(
        "images",
        "videos",
        "files_3d",
        "print_steps",
        "co_creators",
    ).select_related("creator", "published_by", "print_3d_data")

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        return ProjectDetailSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectVideoViewSet(viewsets.ModelViewSet):
    queryset = ProjectVideo.objects.all()
    serializer_class = ProjectVideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Project3DFileViewSet(viewsets.ModelViewSet):
    queryset = Project3DFile.objects.all()
    serializer_class = Project3DFileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class Print3DDataViewSet(viewsets.ModelViewSet):
    queryset = Print3DData.objects.all()
    serializer_class = Print3DDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PrintStepViewSet(viewsets.ModelViewSet):
    queryset = PrintStep.objects.all()
    serializer_class = PrintStepSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]