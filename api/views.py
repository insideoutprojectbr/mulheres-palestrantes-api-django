from rest_framework.viewsets import ModelViewSet

from speaker.models import Speaker
from api.serializers import SpeakerSerializer
from api.permissions import UserPermission


class SpeakerViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def create(self, request):
        return super(SpeakerViewSet, self).create(request)

    def destroy(self, request, pk):
        return super(SpeakerViewSet, self).destroy(request)
