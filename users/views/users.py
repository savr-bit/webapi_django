import pdb

from django.contrib.auth import get_user_model
from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from djoser import views


from users.serializers.api import users as user_s

User = get_user_model()


@extend_schema_view(
    create=extend_schema(summary='Регистрация пользователя', tags=['Аутентификация & Авторизация']),
)
class RegistrationView(views.UserViewSet):
    pass





@extend_schema_view(
    post=extend_schema(
        request=user_s.ChangePasswordSerializer,
        summary='Смена пароля', tags=['Аутентификация & Авторизация']),
)
class ChangePasswordView(APIView):

    def post(self, request):
        user = request.user
        serializer = user_s.ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)


@extend_schema_view(
    get=extend_schema(summary='Профиль пользователя', tags=['Пользователи']),
    put=extend_schema(summary='Изменить профиль пользователя', tags=['Пользователи']),
    patch=extend_schema(summary='Изменить частично профиль пользователя', tags=['Пользователи']),
)
class MeView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = user_s.UserSerializer
    http_method_names = ('get', 'patch')

    def get_serializer_class(self):
        print(self.request.user.email)
        if self.request.method in ['PUT', 'PATCH']:
            return user_s.MeUpdateSerializer
        return user_s.UserSerializer

    def get_object(self):
        return self.request.user

@extend_schema_view(
    retrieve=extend_schema(summary='Профиль авторизированного пользователя', tags=['Пользователи']),
)
class AuthUserView(views.UserViewSet):
    pass



