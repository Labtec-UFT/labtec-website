from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PublicProjectViewSet

router = SimpleRouter()
router.register("", PublicProjectViewSet, basename="public-project")

urlpatterns = [
    path("", include(router.urls)),
]

