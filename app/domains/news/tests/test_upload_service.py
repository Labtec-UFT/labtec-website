from unittest.mock import patch

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase

from app.service.UploadService import UploadService, news_image_upload_to


class _UploadStub:
    def __init__(self, name: str, content_type: str, size: int):
        self.name = name
        self.content_type = content_type
        self.size = size


class _NewsImageCoverInstance:
    news_id = 3
    is_cover = True


class _NewsImageGalleryInstance:
    news_id = 3
    is_cover = False


class UploadServiceNewsTest(SimpleTestCase):
    @patch.object(UploadService, "_random_suffix", return_value="x92kd1")
    def test_news_cover_path_is_standardized(self, _mock_suffix):
        path = news_image_upload_to(_NewsImageCoverInstance(), "capa.JPG")

        self.assertTrue(path.startswith("news/cover/news_3_cover_x92kd1"))
        self.assertTrue(path.endswith(".jpg"))

    @patch.object(UploadService, "_random_suffix", return_value="a83fj2")
    def test_news_gallery_path_is_standardized(self, _mock_suffix):
        path = news_image_upload_to(_NewsImageGalleryInstance(), "galeria.WEBP")

        self.assertTrue(path.startswith("news/gallery/news_3_gallery_a83fj2"))
        self.assertTrue(path.endswith(".webp"))

    def test_validate_rejects_invalid_news_content_type(self):
        upload = _UploadStub(name="capa.jpg", content_type="application/pdf", size=1024)

        with self.assertRaises(ValidationError):
            UploadService.validate_file(upload, context="news.cover")

    def test_validate_rejects_missing_content_type(self):
        upload = _UploadStub(name="capa.jpg", content_type="", size=1024)

        with self.assertRaises(ValidationError):
            UploadService.validate_file(upload, context="news.cover")

