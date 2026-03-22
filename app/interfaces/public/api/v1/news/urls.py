from django.urls import path
from .views import (
    CreateNews,
    ListNews,
    RetrieveNews,
    UpdateNews,
    DeleteNews
)

urlpatterns = [
    path('list/', ListNews.as_view(), name='news-list'),
    path('<int:pk>/', RetrieveNews.as_view(), name='news-detail'),
    path('create/', CreateNews.as_view(), name='news-create'),
    path('<int:pk>/update/', UpdateNews.as_view(), name='news-update'),
    path('<int:pk>/delete/', DeleteNews.as_view(), name='news-delete'),
]