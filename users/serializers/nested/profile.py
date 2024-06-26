from rest_framework import serializers

from users.models.profile import Profile


class ProfileShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'profile_photo',
            'telegram_id',
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            'profile_photo',
            'telegram_id',
        )