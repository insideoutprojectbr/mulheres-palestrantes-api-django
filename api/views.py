from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


from speaker.models import Speaker
from api.serializers import SpeakerSerializer


class SpeakerViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def create(self, request):
        return super(SpeakerViewSet, self).create(request)

    def destroy(self, request, pk):
        return super(SpeakerViewSet, self).destroy(request)
