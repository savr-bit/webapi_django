import pdb

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError, ValidationError
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from users.serializers.nested.profile import ProfileShortSerializer, \
    ProfileUpdateSerializer


User = get_user_model()


class RegistrationSerializer(BaseUserCreateSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
        )


    def create(self, validated_data):
        user = super().create(validated_data)
        user.is_active = True
        user.save(update_fields=["is_active"])
        return user



class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError(
                'Проверьте правильность текущего пароля.'
            )
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(BaseUserSerializer):
    profile = ProfileShortSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'profile',
            'date_joined',
        )

    def validate(self, attrs):
        validate_attrs = super().validate(attrs)

        return validate_attrs


class MeUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileUpdateSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'username',
            'profile',)

    def update(self, instance, validated_data):
        # Проверка наличия профиля
        profile_data = validated_data.pop('profile') if 'profile' in validated_data else None

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            # # Update профиля
            if profile_data:
                self._update_profile(instance.profile, profile_data)

        return instance

    def _update_profile(self, profile, data):
        profile_serializer = ProfileUpdateSerializer(
            instance=profile, data=data, partial=True
        )
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()





