from django.core.management.base import BaseCommand
from faker import Faker
from EKomAPP.models import FormTemplates, CustomUser
import random


class Command(BaseCommand):
    "Создание 20 записей шаблонов для пользователей"
    def handle(self, *args, **kwargs):
        fake = Faker()

        # Получаем всех пользователей
        users = list(CustomUser.objects.all())
        if not users:
            self.stdout.write(self.style.ERROR("Не найдено пользователей для создания шаблонов"))
            return

        for _ in range(20):
            user = random.choice(users)
            FormTemplates.objects.create(
                user_template=user,
                name=f'{fake.name()}-{user}-TEMPLATE',
                email=fake.unique.email(),
                phone_number=self.generate_phone_number(),
                date=self.generate_date(),
                description=fake.text(max_nb_chars=200)
            )

    @staticmethod
    def generate_phone_number():
        """ Генерирует телефонный номер в формате +7 123 456 78 90
        """
        return f"+7 {random.randint(100, 999)} {random.randint(100, 999)} {random.randint(10, 99)} {random.randint(10, 99)}"

    @staticmethod
    def generate_date():
        """Генерирует дату в формате YYYY-MM-DD
        """
        fake = Faker()
        return fake.date_between(start_date="-10y", end_date="today")  # Дата в пределах последних 10 лет