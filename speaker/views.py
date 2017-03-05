from rest_framework.viewsets import ModelViewSet


from speaker.models import Speaker
from speaker.serializers import SpeakerSerializer


class SpeakerViewSet(ModelViewSet):

    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
