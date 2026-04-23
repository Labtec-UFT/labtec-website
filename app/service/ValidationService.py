from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Any

from django.core.exceptions import ValidationError


@dataclass(frozen=True)
class ValidationRuleError:
    field: str
    message: str


class ValidationService:
    """Centralized domain validation rules shared across serializers and services."""

    @staticmethod
    def validate_project_payload(payload: dict[str, Any]) -> None:
        errors: dict[str, list[str]] = {}

        title = (payload.get("title") or "").strip()
        short_description = (payload.get("short_description") or "").strip()
        description = (payload.get("description") or "").strip()
        is_published = bool(payload.get("is_published", False))

        if not title:
            errors.setdefault("title", []).append("Titulo do projeto e obrigatorio.")

        if short_description and len(short_description) < 10:
            errors.setdefault("short_description", []).append(
                "A descricao curta precisa ter pelo menos 10 caracteres."
            )

        if description and len(description) < 20:
            errors.setdefault("description", []).append(
                "A descricao precisa ter pelo menos 20 caracteres."
            )

        # Business integrity: published projects must have minimum content.
        if is_published:
            if len(title) < 5:
                errors.setdefault("title", []).append(
                    "Projeto publicado precisa de titulo com no minimo 5 caracteres."
                )
            if len(short_description) < 10:
                errors.setdefault("short_description", []).append(
                    "Projeto publicado precisa de descricao curta com no minimo 10 caracteres."
                )
            if len(description) < 20:
                errors.setdefault("description", []).append(
                    "Projeto publicado precisa de descricao com no minimo 20 caracteres."
                )

        if errors:
            raise ValidationError(errors)

    @staticmethod
    def validate_news_payload(payload: dict[str, Any]) -> None:
        errors: dict[str, list[str]] = {}

        title = (payload.get("title") or "").strip()
        content = (payload.get("content") or "").strip()
        is_published = bool(payload.get("is_published", False))

        if not title:
            errors.setdefault("title", []).append("Titulo da noticia e obrigatorio.")

        if not content:
            errors.setdefault("content", []).append("Conteudo da noticia e obrigatorio.")

        if is_published and len(content) < 30:
            errors.setdefault("content", []).append(
                "Noticia publicada precisa de conteudo com no minimo 30 caracteres."
            )

        if errors:
            raise ValidationError(errors)

    @staticmethod
    def validate_print_3d_data(payload: dict[str, Any]) -> None:
        errors: dict[str, list[str]] = {}

        material = (payload.get("material") or "").strip()
        weight_grams = payload.get("weight_grams")

        if not material:
            errors.setdefault("material", []).append("Material e obrigatorio para impressao 3D.")

        if weight_grams is not None:
            try:
                weight = Decimal(str(weight_grams))
            except Exception:
                errors.setdefault("weight_grams", []).append("Peso deve ser numerico.")
            else:
                if weight <= 0:
                    errors.setdefault("weight_grams", []).append("Peso deve ser maior que zero.")
                if weight > Decimal("100000"):
                    errors.setdefault("weight_grams", []).append(
                        "Peso excede o limite permitido."
                    )

        if errors:
            raise ValidationError(errors)

