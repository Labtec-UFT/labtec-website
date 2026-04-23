from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied, ValidationError
from rest_framework.test import APIRequestFactory

from app.interfaces.public.api.exception_handler import custom_exception_handler


class ExceptionHandlerTest(SimpleTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def _context(self):
        request = self.factory.post("/api/v1/auth/token/", HTTP_X_REQUEST_ID="req-123")
        return {"request": request, "view": None}

    def test_validation_error_uses_standard_envelope(self):
        exc = ValidationError({"title": ["Campo obrigatorio."]})

        response = custom_exception_handler(exc, self._context())

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"]["code"], "validation_error")
        self.assertEqual(response.data["error"]["message"], "Campo obrigatorio.")
        self.assertEqual(response.data["error"]["trace_id"], "req-123")

    def test_authentication_error_uses_standard_envelope(self):
        exc = AuthenticationFailed("Token invalido.")

        response = custom_exception_handler(exc, self._context())

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["error"]["code"], "unauthorized")

    def test_permission_error_uses_standard_envelope(self):
        exc = PermissionDenied("Acesso negado.")

        response = custom_exception_handler(exc, self._context())

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["error"]["code"], "forbidden")

