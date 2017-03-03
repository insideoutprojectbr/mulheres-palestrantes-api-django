from rest_framework.serializers import ModelSerializer, StringRelatedField


from speaker.models import Speaker, Interest


class SpeakerSerializer(ModelSerializer):

    interests = StringRelatedField(many=True)

    class Meta:
        model = Speaker
        fields = ('id', 'name', 'email', 'interests', 'created_at', 'updated_at')


class InterestSerializer(ModelSerializer):

    class Meta:
        model = Interest
        fields = ('id', 'name')
