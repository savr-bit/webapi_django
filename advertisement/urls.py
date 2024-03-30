from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertisement.views import dicts

router = DefaultRouter()

router.register(r'dicts/publications', dicts.AdvertisementView, 'publications')
router.register(r'dicts/review', dicts.ReviewView,'reviews')

urlpatterns = [

]


urlpatterns += path('advertisement/', include(router.urls)),