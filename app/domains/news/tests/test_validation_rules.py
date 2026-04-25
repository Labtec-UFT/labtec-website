from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from app.service.ValidationService import ValidationService


class ValidationServiceNewsRulesTest(SimpleTestCase):
    def test_rejects_news_without_title(self):
        payload = {
            "title": "",
            "content": "Conteudo valido suficiente para publicacao.",
            "is_published": False,
        }

        with self.assertRaises(ValidationError):
            ValidationService.validate_news_payload(payload)

    def test_rejects_short_published_content(self):
        payload = {
            "title": "Titulo valido",
            "content": "curto",
            "is_published": True,
        }

        with self.assertRaises(ValidationError):
            ValidationService.validate_news_payload(payload)

