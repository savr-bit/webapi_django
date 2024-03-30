import pdb

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from advertisement.models.adv import Advertisement, Review
from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.profile import ProfileShortSerializer, \
    ProfileUpdateSerializer

User = get_user_model()


class AdvertisementListSerializer(ExtendedModelSerializer):
    class Meta:
        model = Advertisement
        fields = (
            'name',
            'ad_type',
            'description',
            'price',
            'category',
        )

class ReviewListSerializer(ExtendedModelSerializer):
    publication = AdvertisementListSerializer()
    class Meta:
        model = Review
        fields = (
            'review_text',
            'publication',
            'number_of_stars',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
        )