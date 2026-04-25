from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient

from app.domains.news.models import NewsModel
from app.domains.projects.models import Project


class AccessControlRoutesTest(APITestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.staff = self.user_model.objects.create_user(
            email="staff@example.com",
            password="StrongPass123!",
            full_name="Staff User",
            is_staff=True,
        )
        self.author = self.user_model.objects.create_user(
            email="author@example.com",
            password="StrongPass123!",
            full_name="Author User",
        )

    def test_legacy_projects_root_is_not_exposed(self):
        response = self.client.get("/api/v1/projects/")

        self.assertEqual(response.status_code, 404)

    def test_public_projects_list_returns_only_published(self):
        Project.objects.create(
            title="Projeto Publico",
            short_description="Descricao curta valida para publico",
            description="Descricao detalhada valida para o projeto publico.",
            creator=self.author,
            is_published=True,
        )
        Project.objects.create(
            title="Projeto Privado",
            short_description="Descricao curta valida para privado",
            description="Descricao detalhada valida para o projeto privado.",
            creator=self.author,
            is_published=False,
        )

        response = self.client.get("/api/v1/public/projects/")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Projeto Publico")

    def test_anonymous_cannot_access_management_projects_list(self):
        response = self.client.get("/api/v1/management/projects/")

        self.assertIn(response.status_code, [401, 403])

    def test_staff_can_access_management_projects_list(self):
        authenticated_client = APIClient()

        token_response = authenticated_client.post(
            "/api/v1/auth/token/",
            {"email": self.staff.email, "password": "StrongPass123!"},
            format="json",
        )
        access_token = token_response.json()["access"]
        authenticated_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        response = authenticated_client.get("/api/v1/management/projects/")

        self.assertEqual(response.status_code, 200)

    def test_public_news_returns_only_published(self):
        NewsModel.objects.create(
            title="Noticia Publica",
            description="Descricao publica valida",
            content="Conteudo publicado suficiente para ser exibido publicamente.",
            is_published=True,
            author=self.staff,
        )
        NewsModel.objects.create(
            title="Noticia Privada",
            description="Descricao privada valida",
            content="Conteudo privado suficiente para nao ser exibido publicamente.",
            is_published=False,
            author=self.staff,
        )

        response = self.client.get("/api/v1/public/news/")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Noticia Publica")




