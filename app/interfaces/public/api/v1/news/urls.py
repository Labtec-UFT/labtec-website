from django.urls import include, path

urlpatterns = [
    path("", include("app.interfaces.public.api.v1.news.management_urls")),
]