from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from app.domains.news.models import NewsModel
from app.domains.news.serializer import NewsSerializer

class CreateNews(generics.CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListNews(generics.ListAPIView):
    queryset = NewsModel.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

class RetrieveNews(generics.RetrieveAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

class UpdateNews(generics.UpdateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser]

class DeleteNews(generics.DestroyAPIView):
    queryset = NewsModel.objects.all()
    permission_classes = [IsAdminUser]