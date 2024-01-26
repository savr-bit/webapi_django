from django.contrib import admin
from django.contrib.admin import TabularInline
from django.urls import reverse
from django.utils.html import format_html

from advertisement.models import adv

#################################
# INLINES
#################################

class ReviewInline(TabularInline): # Можно сделать, если будет необходимость
    model = adv.Review
    fields = ("reviews_text", "publication", "created_by", "number_of_stars", "publish_date")

class AttachmentInline(TabularInline): 
    model = adv.Attachment
    fields = ("file", "file_type",)



#################################
# MODELS
#################################
    
@admin.register(adv.Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_by",)
    list_display_links = ("id", "name")
    search_fields = ("name",)

    inlines = (
        AttachmentInline,
    )

@admin.register(adv.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_description",)
    search_fields = ("category_description",)

@admin.register(adv.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ("id", "file_type", "file", "publication_link",)

    def publication_link(self, obj):
        link = reverse(
            'admin:advertisement_advertisement_change', args=[obj.publication.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.publication)


@admin.register(adv.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "created_by", "number_of_stars", "review_text", "publication_link")

    def publication_link(self, obj):
        link = reverse(
            'admin:advertisement_advertisement_change', args=[obj.publication.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.publication)
