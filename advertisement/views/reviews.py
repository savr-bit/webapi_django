from crum import get_current_user
from django.http import Http404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response

from common.views.mixins import ListViewSet, CRUViewSet, CRUDViewSet
from advertisement.models.adv import Advertisement, Review
from advertisement.serializers.api import advertisements, reviews


@extend_schema_view(
    list=extend_schema(summary="Список отзывов объявления", tags=['Отзывы'])
)
class ReviewsAdvertisementView(ListViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = reviews.ReviewListSerializer

    def get_queryset(self):
        advertisement = Advertisement.objects.get(pk=self.kwargs.get('advertisement_id'))
        return Review.objects.filter(publication=advertisement)




@extend_schema_view(
    list=extend_schema(summary="Список отзывов", tags=['Отзывы']),
    retrieve=extend_schema(summary="Детали отзыва", tags=['Отзывы']),
    create=extend_schema(summary="Создать отзыв", tags=['Отзывы']),
    update=extend_schema(summary="Изменить отзыв", tags=['Отзывы']),
    partial_update=extend_schema(summary="Изменить отзыв частично", tags=['Отзывы']),
    destroy=extend_schema(summary='Удалить отзыв', tags=['Отзывы']),
)

class ReviewView(CRUDViewSet):
    queryset = Advertisement.objects.all()
    serializer_class=advertisements.AdvertisementListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return reviews.ReviewListSerializer
        elif self.action == 'retrieve':
            return reviews.ReviewRetrieveSerializer
        elif self.action == 'create':
            return reviews.ReviewCreateSerializer
        elif self.action == 'update':
            return reviews.ReviewUpdateSerializer
        elif self.action == 'partial_update':
            return reviews.ReviewUpdateSerializer

        return self.serializer_class

    def get_queryset(self):
        if self.action == 'retrieve':
            return Review.objects.all()
        else:
            return Review.objects.filter(created_by = get_current_user())









