from django.contrib import admin
from django.contrib.admin import TabularInline

from advertisement.models import adv

#################################
# INLINES
#################################

class ReviewInline(TabularInline): # Можно сделать, если будет необходимость
    model = adv.User
    fields = ("reviews_text", "publication", "created_by", "number_of_stars", "publish_date")


#################################
# MODELS
#################################
    
@admin.register(adv.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_by",)

@admin.register(adv.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_description",)

@admin.register(adv.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "file_type", "file", "publication",)

@admin.register(adv.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "created_by", "number_of_stars")