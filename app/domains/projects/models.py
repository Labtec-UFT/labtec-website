from django.db import models
from django.conf import settings


class Project(models.Model):
    class ProjectType(models.TextChoices):
        PRINT_3D = "print_3d", "Impressão 3D"
        MODELING = "modeling", "Modelagem"
        HARDWARE = "hardware", "Hardware"
        SOFTWARE = "software", "Software"

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="created_projects",
    )
    co_creators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="co_created_projects",
        blank=True,
    )
    project_type = models.CharField(
        max_length=20,
        choices=ProjectType.choices,
    )
    published_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="published_projects",
    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="projects/images/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Imagem do Projeto"
        verbose_name_plural = "Imagens do Projeto"

    def __str__(self):
        return f"Imagem {self.order} — {self.project.title}"


class ProjectVideo(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="videos",
    )
    url = models.URLField()
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Vídeo do Projeto"
        verbose_name_plural = "Vídeos do Projeto"

    def __str__(self):
        return self.title or f"Vídeo de {self.project.title}"


class Project3DFile(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="files_3d",
    )
    file = models.FileField(upload_to="projects/3d_files/")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Arquivo 3D do Projeto"
        verbose_name_plural = "Arquivos 3D do Projeto"

    def __str__(self):
        return f"{self.name} — {self.project.title}"


class Print3DData(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="print_3d_data",
        limit_choices_to={"project_type": Project.ProjectType.PRINT_3D},
    )
    material = models.CharField(max_length=100)
    weight_grams = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )
    print_time = models.DurationField(
        null=True,
        blank=True,
        help_text="Formato: HH:MM:SS",
    )

    class Meta:
        verbose_name = "Dados de Impressão 3D"
        verbose_name_plural = "Dados de Impressão 3D"

    def __str__(self):
        return f"Dados 3D — {self.project.title}"


class PrintStep(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="print_steps",
    )
    step_number = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ["step_number"]
        unique_together = ("project", "step_number")
        verbose_name = "Etapa de Impressão"
        verbose_name_plural = "Etapas de Impressão"

    def __str__(self):
        return f"Etapa {self.step_number} — {self.project.title}"