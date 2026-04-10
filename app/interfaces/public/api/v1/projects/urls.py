from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProjectViewSet,
    ProjectImageViewSet,
    ProjectVideoViewSet,
    Project3DFileViewSet,
    Print3DDataViewSet,
    PrintStepViewSet,
)

router = DefaultRouter()

router.register("", ProjectViewSet, basename="project")
router.register("project-images", ProjectImageViewSet)
router.register("project-videos", ProjectVideoViewSet)
router.register("project-files-3d", Project3DFileViewSet)
router.register("print-3d-data", Print3DDataViewSet)
router.register("print-steps", PrintStepViewSet)

urlpatterns = [
    path("", include(router.urls)),
]