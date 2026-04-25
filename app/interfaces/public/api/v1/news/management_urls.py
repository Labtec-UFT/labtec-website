from django.urls import path

from .views import ManageListCreateNews, ManageRetrieveUpdateDeleteNews

urlpatterns = [
    path("", ManageListCreateNews.as_view(), name="management-news-list-create"),
    path("<int:pk>/", ManageRetrieveUpdateDeleteNews.as_view(), name="management-news-detail"),
]

