from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from app.domains.news.models import NewsModel
from app.domains.news.serializer import NewsSerializer


class PublicListNews(generics.ListAPIView):
    queryset = NewsModel.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class PublicRetrieveNews(generics.RetrieveAPIView):
    queryset = NewsModel.objects.filter(is_published=True)
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class ManageListCreateNews(generics.ListCreateAPIView):
    queryset = NewsModel.objects.all().order_by("-created_at")
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ManageRetrieveUpdateDeleteNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]
