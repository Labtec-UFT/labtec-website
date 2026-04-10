from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from app.domains.news.models import NewsModel
from app.domains.news.serializer import NewsSerializer

class ListCreateNews(generics.ListCreateAPIView):
    queryset = NewsModel.objects.all().order_by("-created_at")
    serializer_class = NewsSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDeleteNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]