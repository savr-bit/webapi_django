from django.contrib import admin

from advertisement.models import adv

@admin.register(adv.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_by",)

@admin.register(adv.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_description",)

@admin.register(adv.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "file_type", "file", "publication",)
