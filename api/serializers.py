from rest_framework import serializers

from speaker.models import Speaker, Interest


class SpeakerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    interests = serializers.StringRelatedField(many=True)
    created_at = serializers.ReadOnlyField(source='date_joined')
    fb = serializers.ReadOnlyField(source='facebook_url')
    twitter = serializers.ReadOnlyField(source='twitter_url')
    github = serializers.ReadOnlyField(source='github_url')
    linkedin = serializers.ReadOnlyField(source='linkedin_url')
    behance = serializers.ReadOnlyField(source='behance_url')
    medium = serializers.ReadOnlyField(source='medium_url')

    class Meta:
        model = Speaker
        fields = ('id', 'email', 'username', 'last_name', 'first_name',
                  'interests', 'site', 'created_at', 'updated_at', 'password',
                  'fb', 'linkedin', 'behance', 'github', 'twitter', 'medium', 'photo',)


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ('id', 'name')
