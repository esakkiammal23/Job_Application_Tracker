from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = "Create admin user"

    def handle(self, *args, **kwargs):
        if User.objects.filter(username="admin").exists():
            self.stdout.write("Admin already exists")
            return

        User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="Admin@123"
        )

        self.stdout.write(self.style.SUCCESS("Admin created"))