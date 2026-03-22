from django.apps import AppConfig

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.domains.news'

    def ready(self):
        import app.domains.news.signals