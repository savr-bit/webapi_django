from django.urls import path, include
from rest_framework.routers import DefaultRouter

from advertisement.views import advertisements

adv_router = DefaultRouter()
rev_router = DefaultRouter()

adv_router.register(r'search', advertisements.AdvertisementsSearchView, 'advertisements')
# adv_router.register(r'(?P<advertisement_id>\d+)/reviews', dicts.PublicationReviewsView,'reviews')
adv_router.register(r'manage', advertisements.AdvertisementsView, 'advertisements')

urlpatterns = [
]


urlpatterns += path('advertisement/', include(adv_router.urls)),
urlpatterns += path('review/', include(rev_router.urls)),