from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.users import UserShortSerializer
from advertisement.models.adv import Advertisement

class AdvertisementListSerializer(ExtendedModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Advertisement
        fields = '__all__'

class AdvertisementRetrieveSerializer(ExtendedModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Advertisement
        fields = '__all__'

class AdvertisementCreateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('id',
                  'name',
                  'ad_type',
                  'description',
                  'price',
                  'category')


class AdvertisementUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('id',
                  'name',
                  'ad_type',
                  'description',
                  'price',
                  'category')