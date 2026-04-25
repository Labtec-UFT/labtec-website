from django.urls import include, path

from app.interfaces.public.api.v1.news import public_urls as news_public_urls
from app.interfaces.public.api.v1.projects import public_urls as projects_public_urls

urlpatterns = [
    path("news/", include(news_public_urls)),
    path("projects/", include(projects_public_urls)),
]


