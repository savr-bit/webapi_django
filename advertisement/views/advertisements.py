from crum import get_current_user
from django.http import Http404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response

from common.views.mixins import ListViewSet, CRUViewSet, CRUDViewSet
from advertisement.models.adv import Advertisement
from advertisement.serializers.api import advertisements


@extend_schema_view(
    list=extend_schema(summary="Список объявлений Search", tags=['Объявления'])
)
class AdvertisementsSearchView(ListViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = advertisements.AdvertisementsSearchListSerializer


@extend_schema_view(
    list=extend_schema(summary="Список объявлений", tags=['Объявления']),
    retrieve=extend_schema(summary="Детали объявления", tags=['Объявления']),
    create=extend_schema(summary="Создать объявление", tags=['Объявления']),
    update=extend_schema(summary="Изменить объявление", tags=['Объявления']),
    partial_update=extend_schema(summary="Изменить объявление частично", tags=['Объявления']),
    destroy=extend_schema(summary='Удалить объявление', tags=['Объявления']),
)

class AdvertisementsView(CRUDViewSet):
    queryset = Advertisement.objects.all()
    serializer_class=advertisements.AdvertisementListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return advertisements.AdvertisementListSerializer
        elif self.action == 'retrieve':
            return advertisements.AdvertisementRetrieveSerializer
        elif self.action == 'create':
            return advertisements.AdvertisementCreateSerializer
        elif self.action == 'update':
            return advertisements.AdvertisementUpdateSerializer
        elif self.action == 'partial_update':
            return advertisements.AdvertisementUpdateSerializer

        return self.serializer_class

    def get_queryset(self):
        if self.action == 'retrieve':
            return Advertisement.objects.all()
        else:
            return Advertisement.objects.filter(created_by = get_current_user())

    def destroy(self, request, *args, **kwargs):
        user = get_current_user()

        instance = self.get_object()
        if (instance.created_by != user):
            return Response(data={'detail' : 'Вы не можете удалить чужое объявление'},
                                      status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)







