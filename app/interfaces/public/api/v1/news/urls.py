from django.urls import path
from .views import (
    ListCreateNews,
    RetrieveUpdateDeleteNews,
)

urlpatterns = [
    path("", ListCreateNews.as_view(), name="news-list-create"),
    path("<int:pk>/", RetrieveUpdateDeleteNews.as_view(), name="news-detail"),
]