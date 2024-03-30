from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.response import Response

import common.pagination
from advertisement.models.adv import Advertisement, Review
from advertisement.serializers.api.dicts import AdvertisementListSerializer, ReviewListSerializer
from common.views.mixins import ListViewSet, ExtendedViewSet
from users.models.users import User


@extend_schema_view(
    list=extend_schema(summary="Список объявлений", tags=["Словари"]),
)
class AdvertisementView(ListViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer



@extend_schema_view(
    list=extend_schema(summary="Список отзывов пользователя", tags=['Словари'],
                       parameters=[OpenApiParameter("user",OpenApiTypes.INT)]),
)
class ReviewView(ListViewSet):
    serializer_class = ReviewListSerializer
    def get_queryset(self):
        return Review.objects.filter(created_by=self.request.query_params.get("user"))




