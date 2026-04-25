from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from app.service.ValidationService import ValidationService


class ValidationServiceProjectRulesTest(SimpleTestCase):
    def test_rejects_published_project_without_minimum_content(self):
        payload = {
            "title": "abc",
            "short_description": "curta",
            "description": "breve",
            "is_published": True,
        }

        with self.assertRaises(ValidationError):
            ValidationService.validate_project_payload(payload)

    def test_accepts_valid_project_payload(self):
        payload = {
            "title": "Projeto de Impressao 3D",
            "short_description": "Descricao curta com tamanho valido",
            "description": "Descricao detalhada do projeto com informacoes suficientes.",
            "is_published": True,
        }

        ValidationService.validate_project_payload(payload)

    def test_rejects_invalid_print_3d_weight(self):
        payload = {
            "material": "PLA",
            "weight_grams": "-2",
        }

        with self.assertRaises(ValidationError):
            ValidationService.validate_print_3d_data(payload)

