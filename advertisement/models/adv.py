from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models
from common.models.mixins import InfoMixin

import common.models.mixins

User = get_user_model()


class Category(models.Model):
    category_description = models.CharField(
        "Категория", max_length = 50
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.category_description}'
    

class Advertisement(InfoMixin):
    class AdCategory(models.TextChoices):
        SERVICE = 'S', _("Услуга")
        PROJECT = 'P', _("Проект")
    
    name = models.CharField(
        "Название", max_length = 255
    )
    ad_type = models.CharField(
        "Тип объявления",max_length = 1, choices = AdCategory
    )
    # created_by = models.ForeignKey(
    #     User, models.CASCADE, related_name = "projects",
    #     verbose_name = "Создатель объявления"
    # )
    # publish_date = models.DateField("Дата публикации")
    description = models.TextField("Описание")
    price = models.PositiveIntegerField("Цена")
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("name", )

    def __str__(self):
        return f"{self.name}({self.id})"

class Attachment(models.Model):
    class AttachmentType(models.TextChoices):
        PHOTO = "Photo", _("Фото")
        VIDEO = "Video", _("Видео")

    file = models.ImageField('Вложение', upload_to='attachments/')
    file_type = models.CharField('Тип файла', choices=AttachmentType.choices, max_length=10)

    publication = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='attachments', verbose_name = "Объявление")

    class Meta:
        verbose_name = 'Вложение'
        verbose_name_plural = 'Вложения'

class Review(InfoMixin):
    review_text = models.TextField("Текст отзыва")
    publication = models.ForeignKey(
        Advertisement, models.CASCADE, related_name = "reviews",
        verbose_name = "Объявление"
    )


    number_of_stars_choices = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    number_of_stars = models.IntegerField("Количество звезд", choices = number_of_stars_choices)


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"





