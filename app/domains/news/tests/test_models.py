from django.test import TestCase
from app.domains.news.models import NewsModel, NewsImage
from app.domains.users.models import CustomUser
from django.utils import timezone

class NewsModelTest(TestCase):
    def setUp(self):
        self.news = NewsModel.objects.create(
            title="Microsoft inaugura dois data centers de IA no Brasil",
            description="Investimento em infraestrutura e capacitacao tecnologica no Brasil.",
            content="microsoft-inaugura-dois-data-centers-de-ia-no-brasil",
            created_at=timezone.now(),
            is_published=True,
            published_at=timezone.now(),
            author=CustomUser.objects.create(
                email="user@teste.com",
                password="admin123",
                is_staff=True,
                full_name="Usuário de Teste da Silva"
            ),
        )

    def test_create_news_model(self):
        self.assertEqual(self.news.title, "Microsoft inaugura dois data centers de IA no Brasil")
        self.assertTrue(
            abs((self.news.created_at - timezone.now()).total_seconds()) < 1
        )

    def test_delete_news_model(self):
        self.news.delete()
        exists = NewsModel.objects.filter(id=self.news.id).exists()
        self.assertFalse(exists)