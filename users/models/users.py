from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager
from users.models.profile import Profile


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


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if hasattr(instance, "profile"):
        Profile.objects.create(user=instance)
