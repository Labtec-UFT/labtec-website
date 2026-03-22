from django.contrib import admin
from django.utils.html import format_html
from .models import NewsModel, NewsImage

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ('image', 'preview', 'description', 'is_cover', 'order')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px; height:60px; object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Preview"


class NewsAdmin(admin.ModelAdmin):
    model = NewsModel

    list_display = ('id', 'title', 'author', 'is_published', 'created_at', 'cover_preview')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content', 'summary')
    ordering = ('-created_at',)

    inlines = [NewsImageInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'summary')
        }),
        ('Publicação', {
            'fields': ('is_published', 'published_at', 'author')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    def cover_preview(self, obj):
        cover = obj.images.filter(is_cover=True).first()
        if cover and cover.image:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; object-fit:cover; border-radius:50%;" />',
                cover.image.url
            )
        return "-"
    cover_preview.short_description = "Capa"

class NewsImageAdmin(admin.ModelAdmin):
    model = NewsImage
    list_display = ('news', 'image', 'is_cover', 'order', 'created_at', 'preview')
    list_filter = ('is_cover', 'news')
    ordering = ('order',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; object-fit:cover;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Preview"

admin.site.register(NewsModel, NewsAdmin)
admin.site.register(NewsImage, NewsImageAdmin)