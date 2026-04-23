from django.apps import AppConfig

class ProjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.domains.projects"

    def ready(self):
        import app.domains.projects.signals

