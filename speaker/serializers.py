from rest_framework import serializers


from speaker.models import Speaker, Interest


class SpeakerSerializer(serializers.ModelSerializer):

    interests = serializers.StringRelatedField(many=True)
    fb = serializers.ReadOnlyField(source='facebook_url')
    twitter = serializers.ReadOnlyField(source='twitter_url')
    github = serializers.ReadOnlyField(source='github_url')
    linkedin = serializers.ReadOnlyField(source='linkedin_url')
    behance = serializers.ReadOnlyField(source='behance_url')


    class Meta:
        model = Speaker
        fields = ('id', 'name', 'email', 'interests', 'created_at', 'updated_at',
                  'fb', 'linkedin', 'behance', 'github', 'twitter', 'photo',)

class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ('id', 'name')
