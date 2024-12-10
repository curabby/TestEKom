from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(unique=True,  db_index=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class FormTemplates(models.Model):
    user_template = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=16,  # Формат "+7 xxx xxx xx xx" (16 символов с пробелами)
        validators=[
            RegexValidator(
                regex=r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
                message="Введите корректный номер телефона в формате: +7 xxx xxx xx xx"
            )
        ],
        unique=True,  # Уникальность номера
        blank=False,
        null=False
    )
    date = models.DateField(blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.phone_number
