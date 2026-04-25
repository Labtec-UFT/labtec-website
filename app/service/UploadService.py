import os
import re
import secrets
from dataclasses import dataclass
from typing import Iterable

from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.utils.text import slugify


@dataclass(frozen=True)
class UploadPolicy:
	allowed_extensions: tuple[str, ...]
	allowed_content_types: tuple[str, ...]
	max_size_bytes: int


class UploadService:

	DEFAULT_MAX_IMAGE_SIZE = 8 * 1024 * 1024  # 8MB
	DEFAULT_MAX_3D_SIZE = 150 * 1024 * 1024  # 150MB
	FILENAME_PATTERN = re.compile(r"^[A-Za-z0-9._\- ]+$")

	POLICY_BY_CONTEXT = {
		"projects.image": UploadPolicy(
			allowed_extensions=(".jpg", ".jpeg", ".png", ".gif", ".webp"),
			allowed_content_types=(
				"image/jpeg",
				"image/png",
				"image/gif",
				"image/webp",
			),
			max_size_bytes=DEFAULT_MAX_IMAGE_SIZE,
		),
		"news.cover": UploadPolicy(
			allowed_extensions=(".jpg", ".jpeg", ".png", ".gif", ".webp"),
			allowed_content_types=(
				"image/jpeg",
				"image/png",
				"image/gif",
				"image/webp",
			),
			max_size_bytes=DEFAULT_MAX_IMAGE_SIZE,
		),
		"news.gallery": UploadPolicy(
			allowed_extensions=(".jpg", ".jpeg", ".png", ".gif", ".webp"),
			allowed_content_types=(
				"image/jpeg",
				"image/png",
				"image/gif",
				"image/webp",
			),
			max_size_bytes=DEFAULT_MAX_IMAGE_SIZE,
		),
		"projects.files_3d": UploadPolicy(
			allowed_extensions=(".stl", ".obj", ".gltf", ".glb", ".3mf", ".zip"),
			allowed_content_types=(
				"application/sla",
				"model/stl",
				"model/obj",
				"model/gltf+json",
				"model/gltf-binary",
				"application/octet-stream",
				"application/zip",
				"application/x-zip-compressed",
			),
			max_size_bytes=DEFAULT_MAX_3D_SIZE,
		),
	}

	@staticmethod
	def _clean_extension(filename: str) -> str:
		return os.path.splitext(filename or "")[1].lower()

	@staticmethod
	def _resolve_entity_id(entity_id: int | None) -> str:
		return str(entity_id) if entity_id else "new"

	@staticmethod
	def _random_suffix(size: int = 6) -> str:
		return secrets.token_urlsafe(size)[:size].lower()

	@classmethod
	def _build_standardized_name(
		cls,
		*,
		entity_prefix: str,
		entity_id: int | None,
		kind: str,
		original_filename: str,
	) -> str:
		ext = cls._clean_extension(original_filename)
		token = cls._random_suffix()
		clean_kind = slugify(kind).replace("-", "_") or "file"
		return f"{entity_prefix}_{cls._resolve_entity_id(entity_id)}_{clean_kind}_{token}{ext}"

	@staticmethod
	def _normalize_directories(parts: Iterable[str]) -> str:
		cleaned = [slugify(part).replace("-", "_") for part in parts if part]
		return "/".join(filter(None, cleaned))

	@classmethod
	def _ensure_unique_path(cls, storage, relative_path: str) -> str:
		if not storage.exists(relative_path):
			return relative_path

		directory, filename = os.path.split(relative_path)
		stem, ext = os.path.splitext(filename)
		return f"{directory}/{stem}_{cls._random_suffix(4)}{ext}"

	@classmethod
	def build_upload_path(
		cls,
		*,
		directories: tuple[str, ...],
		entity_prefix: str,
		entity_id: int | None,
		kind: str,
		original_filename: str,
		storage=None,
	) -> str:
		destination = cls._normalize_directories(directories)
		standardized_name = cls._build_standardized_name(
			entity_prefix=entity_prefix,
			entity_id=entity_id,
			kind=kind,
			original_filename=original_filename,
		)
		relative_path = f"{destination}/{standardized_name}"
		active_storage = storage or default_storage
		return cls._ensure_unique_path(active_storage, relative_path)

	@classmethod
	def validate_file(cls, uploaded_file, context: str) -> None:
		policy = cls.POLICY_BY_CONTEXT.get(context)
		if not policy:
			raise ValidationError("Contexto de upload invalido.", code="invalid_upload_context")

		filename = getattr(uploaded_file, "name", "") or ""
		extension = cls._clean_extension(filename)
		content_type = getattr(uploaded_file, "content_type", "")
		size = getattr(uploaded_file, "size", 0)

		if not filename:
			raise ValidationError("Arquivo sem nome nao permitido.", code="missing_filename")

		base_name = os.path.basename(filename)
		if base_name != filename:
			raise ValidationError(
				"Nome de arquivo invalido.",
				code="invalid_filename",
			)

		if not cls.FILENAME_PATTERN.match(base_name):
			raise ValidationError(
				"Nome de arquivo contem caracteres invalidos.",
				code="invalid_filename",
			)

		if size <= 0:
			raise ValidationError("Arquivo vazio nao permitido.", code="empty_file")

		if extension not in policy.allowed_extensions:
			allowed = ", ".join(policy.allowed_extensions)
			raise ValidationError(
				f"Extensao nao permitida. Permitidas: {allowed}.",
				code="invalid_extension",
			)

		if not content_type:
			raise ValidationError("Tipo MIME do arquivo e obrigatorio.", code="missing_content_type")

		if content_type not in policy.allowed_content_types:
			allowed = ", ".join(policy.allowed_content_types)
			raise ValidationError(
				f"Tipo de arquivo nao permitido. Permitidos: {allowed}.",
				code="invalid_content_type",
			)

		if size > policy.max_size_bytes:
			raise ValidationError(
				f"Arquivo excede o tamanho maximo de {policy.max_size_bytes // (1024 * 1024)}MB.",
				code="file_too_large",
			)


def project_image_upload_to(instance, filename: str) -> str:
	return UploadService.build_upload_path(
		directories=("projects", "images"),
		entity_prefix="project",
		entity_id=getattr(instance, "project_id", None),
		kind="image",
		original_filename=filename,
		storage=instance.image.storage if getattr(instance, "image", None) else None,
	)


def project_3d_file_upload_to(instance, filename: str) -> str:
	return UploadService.build_upload_path(
		directories=("projects", "files_3d"),
		entity_prefix="project",
		entity_id=getattr(instance, "project_id", None),
		kind="file_3d",
		original_filename=filename,
		storage=instance.file.storage if getattr(instance, "file", None) else None,
	)


def news_image_upload_to(instance, filename: str) -> str:
	folder = "cover" if getattr(instance, "is_cover", False) else "gallery"
	return UploadService.build_upload_path(
		directories=("news", folder),
		entity_prefix="news",
		entity_id=getattr(instance, "news_id", None),
		kind=folder,
		original_filename=filename,
		storage=instance.image.storage if getattr(instance, "image", None) else None,
	)

