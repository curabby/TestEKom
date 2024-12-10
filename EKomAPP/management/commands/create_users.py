from django.core.management.base import BaseCommand
from faker import Faker
from EKomAPP.models import CustomUser


class Command(BaseCommand):
    """Создание 7 фейковых пользователей"""

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(7):
            CustomUser.objects.create_user(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                password="1234User*",
            )