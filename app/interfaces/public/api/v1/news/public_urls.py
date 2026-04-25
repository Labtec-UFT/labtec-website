from django.urls import path

from .views import PublicListNews, PublicRetrieveNews

urlpatterns = [
    path("", PublicListNews.as_view(), name="public-news-list"),
    path("<int:pk>/", PublicRetrieveNews.as_view(), name="public-news-detail"),
]

