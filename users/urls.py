from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import users




urlpatterns = [
    # path('users/reg/', users.RegistrationView.as_view(), name='reg'),
    path('users/me/', users.MeView.as_view(), name='me'),
    path('users/change-passwd/', users.ChangePasswordView.as_view(), name='change_passwd'),
    path('users/registration', users.RegistrationView.as_view({'post' : 'create'}), name='reg'),
    path('users/authuser/<int:id>', users.AuthUserView.as_view({"get" : "retrieve"}), name='authuser')
]

