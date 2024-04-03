from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as user_urls
from advertisement.urls import urlpatterns as advertisement_urls


app_name = 'api'

urlpatterns = [
    # path('activate/', include('core.urls')),
    # path('auth/jwt/create/',CustomTokenObtainPairView.as_view(),name='custom_jwt_create'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
urlpatterns += user_urls
urlpatterns += advertisement_urls
