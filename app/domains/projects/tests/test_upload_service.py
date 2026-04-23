from unittest.mock import patch

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from app.service.UploadService import (
    UploadService,
    project_3d_file_upload_to,
    project_image_upload_to,
)


class _UploadStub:
    def __init__(self, name: str, content_type: str, size: int):
        self.name = name
        self.content_type = content_type
        self.size = size


class _ProjectImageInstance:
    project_id = 15


class _Project3DFileInstance:
    project_id = 15


class UploadServiceProjectsTest(SimpleTestCase):
    @patch.object(UploadService, "_random_suffix", return_value="a83fj2")
    def test_project_image_path_is_standardized(self, _mock_suffix):
        path = project_image_upload_to(_ProjectImageInstance(), "foto-final.PNG")

        self.assertTrue(path.startswith("projects/images/project_15_image_a83fj2"))
        self.assertTrue(path.endswith(".png"))

    @patch.object(UploadService, "_random_suffix", return_value="x92kd1")
    def test_project_3d_path_is_standardized(self, _mock_suffix):
        path = project_3d_file_upload_to(_Project3DFileInstance(), "prototipo.GLB")

        self.assertTrue(path.startswith("projects/files_3d/project_15_file_3d_x92kd1"))
        self.assertTrue(path.endswith(".glb"))

    def test_validate_rejects_invalid_extension(self):
        upload = _UploadStub(name="virus.exe", content_type="image/png", size=100)

        with self.assertRaises(ValidationError):
            UploadService.validate_file(upload, context="projects.image")

    def test_validate_rejects_oversized_3d_file(self):
        upload = _UploadStub(
            name="arquivo.stl",
            content_type="model/stl",
            size=UploadService.DEFAULT_MAX_3D_SIZE + 1,
        )

        with self.assertRaises(ValidationError):
            UploadService.validate_file(upload, context="projects.files_3d")

    def test_validate_rejects_empty_file(self):
        upload = _UploadStub(name="arquivo.stl", content_type="model/stl", size=0)

        with self.assertRaises(ValidationError):
            UploadService.validate_file(upload, context="projects.files_3d")

    def test_validate_rejects_invalid_filename(self):
        upload = _UploadStub(name="../arquivo.stl", content_type="model/stl", size=100)

        with self.assertRaises(ValidationError):
            UploadService.validate_file(upload, context="projects.files_3d")

