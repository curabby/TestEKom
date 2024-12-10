from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Создает суперпользователя"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Проверяем, существует ли суперпользователь
        if User.objects.filter(email="super-user@mail.com").exists():
            self.stdout.write(self.style.WARNING("Суперпользователь уже существует."))
            return
        # Создаем суперпользователя
        User.objects.create_superuser(
            email="super-user@mail.com",
            password="1234SuperUser*"
        )
        self.stdout.write(self.style.SUCCESS("Суперпользователь успешно создан."))