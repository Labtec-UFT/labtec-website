from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Project,
    ProjectImage,
    ProjectVideo,
    Project3DFile,
    Print3DData,
    PrintStep
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "preview", "order")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:60px;object-fit:cover;border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Preview"


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1
    fields = ("title", "url")


class Project3DFileInline(admin.TabularInline):
    model = Project3DFile
    extra = 1
    fields = ("name", "file", "description", "created_at")
    readonly_fields = ("created_at",)


class PrintStepInline(admin.TabularInline):
    model = PrintStep
    extra = 1
    fields = ("step_number", "description")
    ordering = ("step_number",)


class Print3DDataInline(admin.StackedInline):
    model = Print3DData
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "creator",
        "project_type",
        "is_published",
        "created_at",
        "cover_preview",
    )

    list_filter = (
        "project_type",
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "creator__username",
    )

    ordering = ("-created_at",)

    readonly_fields = ("created_at", "updated_at")

    inlines = [
        ProjectImageInline,
        ProjectVideoInline,
        Project3DFileInline,
        Print3DDataInline,
        PrintStepInline,
    ]

    fieldsets = (
        (None, {
            "fields": (
                "title",
                "short_description",
                "description",
                "project_type",
            )
        }),
        ("Autores", {
            "fields": (
                "creator",
                "co_creators",
            )
        }),
        ("Publicação", {
            "fields": (
                "is_published",
                "published_by",
            )
        }),
        ("Datas", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    def cover_preview(self, obj):
        image = obj.images.first()
        if image and image.image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;border-radius:6px;" />',
                image.image.url
            )
        return "-"
    cover_preview.short_description = "Preview"


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):

    list_display = ("project", "order", "preview")
    ordering = ("order",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Preview"


@admin.register(ProjectVideo)
class ProjectVideoAdmin(admin.ModelAdmin):

    list_display = ("project", "title", "url")
    search_fields = ("title", "url")


@admin.register(Project3DFile)
class Project3DFileAdmin(admin.ModelAdmin):

    list_display = ("project", "name", "created_at")
    search_fields = ("name",)