from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

class ExtendedViewSet(GenericViewSet):
    pass

class ListViewSet(ExtendedViewSet, mixins.ListModelMixin):
    pass


class CRUViewSet(ExtendedViewSet,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.ListModelMixin):
    pass

class CRUDViewSet(CRUViewSet,
                  mixins.DestroyModelMixin):
    pass