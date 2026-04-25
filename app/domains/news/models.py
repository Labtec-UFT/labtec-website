from django.utils import timezone
from django.db import models
from app.domains.users.models import CustomUser
from app.service.UploadService import news_image_upload_to
from app.service.ValidationService import ValidationService
from app.utils.bleach_utils import clean_html


class NewsModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name="news"
    )

    class Meta:
        db_table = "news"
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.content = clean_html(self.content, strip_opt=True)

        self.full_clean()

        if self.is_published and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def clean(self):
        ValidationService.validate_news_payload(
            {
                "title": self.title,
                "content": self.content,
                "is_published": self.is_published,
            }
        )

    def __str__(self):
        return f"{self.id} - {self.title}"

class NewsImage(models.Model):
    news = models.ForeignKey(
        NewsModel,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to=news_image_upload_to)
    description = models.CharField(max_length=255, blank=True, null=True)
    is_cover = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_cover:
            NewsImage.objects.filter(news=self.news, is_cover=True).exclude(pk=self.pk).update(is_cover=False)

        super().save(*args, **kwargs)

    class Meta:
        db_table = "news_images"
        verbose_name = "Imagem da notícia"
        verbose_name_plural = "Imagens da notícia"

    def __str__(self):
        return f"Imagem da notícia {self.news.title}"