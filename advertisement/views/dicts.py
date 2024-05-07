from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.response import Response

import common.pagination
from advertisement.models.adv import Advertisement, Review
from advertisement.serializers.api.dicts import AdvertisementListSerializer, ReviewSerializer
from common.views.mixins import ListViewSet, ExtendedViewSet
from users.models.users import User


@extend_schema_view(
    list=extend_schema(summary="Список объявлений", tags=["Объявления"]),
)
class AdvertisementView(ListViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementListSerializer



@extend_schema_view(
    list=extend_schema(summary="Список отзывов объявления", tags=['Отзывы'],
                       parameters=[Open("advertisement_id",OpenApiTypes.INT, OpenApiParameter.PATH)],
    ),
)
class PublicationReviewsView(ListViewSet):
    lookup_url_kwarg = 'advertisement_id'
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(publication=self.kwargs.get("advertisement_id"))




