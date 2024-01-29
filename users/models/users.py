from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from users.models.managers import CustomUserManager

class User(AbstractUser):
    username = models.CharField(
        "Никнейм", unique = True, max_length=64, null = True, blank = True
    )
    email = models.EmailField("Почта", unique = True, null = True, blank = True)
    phone_number = PhoneNumberField('Телефон', unique = True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.full_name} ({self.pk})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
