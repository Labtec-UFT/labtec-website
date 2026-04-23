from django.urls import include, path

from app.interfaces.public.api.v1.news import management_urls as news_management_urls
from app.interfaces.public.api.v1.projects import management_urls as projects_management_urls
from app.interfaces.public.api.v1.users import urls as users_urls

urlpatterns = [
    path("news/", include(news_management_urls)),
    path("projects/", include(projects_management_urls)),
    path("users/", include(users_urls)),
]


