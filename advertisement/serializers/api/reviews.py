from crum import get_current_user
from rest_framework.exceptions import ParseError, ValidationError

from common.serializers.mixins import ExtendedModelSerializer
from advertisement.models.adv import Advertisement, Category, Review
from users.serializers.nested.users import UserShortSerializer


class ReviewListSerializer(ExtendedModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Review
        fields = '__all__'

class ReviewRetrieveSerializer(ExtendedModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Review
        fields = '__all__'





class ReviewCreateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Review
        exclude = (
            'created_by',
            'updated_by',
            'created_at',
            'updated_at',
        )


class ReviewUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Review
        exclude = (
            'created_by',
            'updated_by',
            'created_at',
            'updated_at',
            'publication'
        )

    def validate(self, attrs):
        user = get_current_user()
        if (Review.objects.get(pk=self.context['view'].kwargs.get('pk')).created_by != user):
            raise ParseError(
                "Это не ваш отзыв"
            )
        return attrs



