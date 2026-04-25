from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Cria um usuário admin customizado"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Nome do admin")

    def handle(self, *args, **options):
        User = get_user_model()

        name = options["name"].lower()
        email = f"{name}@{name}.com"
        password = "admin"

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING("Admin já existe"))
            return

        User.objects.create_superuser(
            email=email,
            password=password,
        )

        self.stdout.write(self.style.SUCCESS(
            f"Admin criado: {email} / senha: {password}"
        ))