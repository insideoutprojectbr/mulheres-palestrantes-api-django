from django.conf.urls import url, include
from rest_framework import routers
from api.views import SpeakerViewSet


router = routers.DefaultRouter()
router.register(r"speakers", SpeakerViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    url(r"^auth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
]
