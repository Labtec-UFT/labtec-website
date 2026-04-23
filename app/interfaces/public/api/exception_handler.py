from __future__ import annotations

import uuid

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler


def _extract_message(data) -> str:
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list) and value:
                return str(value[0])
            if isinstance(value, str):
                return value
    if isinstance(data, list) and data:
        return str(data[0])
    if isinstance(data, str):
        return data
    return "Falha de validacao."


def custom_exception_handler(exc, context):
    if isinstance(exc, DjangoValidationError):
        if hasattr(exc, "message_dict"):
            exc = ValidationError(exc.message_dict)
        else:
            exc = ValidationError(exc.messages)

    response = exception_handler(exc, context)
    request = context.get("request")
    trace_id = None

    if request is not None:
        trace_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())

    if response is None:
        return Response(
            {
                "error": {
                    "code": "internal_server_error",
                    "message": "Erro interno inesperado.",
                    "fields": {},
                    "trace_id": trace_id,
                }
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    data = response.data
    fields = data if isinstance(data, dict) else {"non_field_errors": data}

    error_code = "api_error"
    if response.status_code == status.HTTP_400_BAD_REQUEST:
        error_code = "validation_error"
    elif response.status_code == status.HTTP_401_UNAUTHORIZED:
        error_code = "unauthorized"
    elif response.status_code == status.HTTP_403_FORBIDDEN:
        error_code = "forbidden"
    elif response.status_code == status.HTTP_404_NOT_FOUND:
        error_code = "not_found"

    response.data = {
        "error": {
            "code": error_code,
            "message": _extract_message(data),
            "fields": fields if isinstance(fields, dict) else {},
            "trace_id": trace_id,
        }
    }
    return response

