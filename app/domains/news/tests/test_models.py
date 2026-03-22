from django.test import TestCase
from app.domains.news.models import NewsModel, NewsImage
from app.domains.users.models import CustomUser
from django.utils import timezone

class NewsModelTest(TestCase):
    def setUp(self):
        self.news = NewsModel.objects.create(
            title="Microsoft inaugura dois data centers de IA no Brasil",
            description="Unidades ficam no estado de SP e fazem parte de investimento de R$ 14,7 bilhões anunciado para o país; empresa também promete capacitar 5 milhões de brasileiros até 2027.",
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