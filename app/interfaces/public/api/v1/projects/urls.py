from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    ManageProjectViewSet,
    ProjectImageViewSet,
    ProjectVideoViewSet,
    Project3DFileViewSet,
    Print3DDataViewSet,
    PrintStepViewSet,
)

router = SimpleRouter()

router.register("", ManageProjectViewSet, basename="project")
router.register("project-images", ProjectImageViewSet)
router.register("project-videos", ProjectVideoViewSet)
router.register("project-files-3d", Project3DFileViewSet)
router.register("print-3d-data", Print3DDataViewSet)
router.register("print-steps", PrintStepViewSet)

urlpatterns = [
    path("", include(router.urls)),
]