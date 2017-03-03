from django.conf.urls import url, include
from rest_framework import routers
from speaker.views import SpeakerViewSet


router = routers.DefaultRouter()
router.register(r'speakers', SpeakerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
