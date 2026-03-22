from django.db import models


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.CharField(max_length=500)
    cover_image = models.ImageField(upload_to="news/covers/", blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    id = models.AutoField(primary_key=True)
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="news/images/")
    description = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Imagem da Notícia"
        verbose_name_plural = "Imagens da Notícia"

    def __str__(self):
        return f"Imagem — {self.news.title}"