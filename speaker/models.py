from django_gravatar.helpers import get_gravatar_url
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Speaker(AbstractUser):
    email = models.EmailField(unique=True, max_length=100, db_index=True)
    location = models.CharField(blank=True, null=True, max_length=100, db_index=True)
    facebook = models.CharField(blank=True, null=True, max_length=50)
    twitter = models.CharField(blank=True, null=True, max_length=50)
    github = models.CharField(blank=True, null=True, max_length=50)
    linkedin = models.CharField(blank=True, null=True, max_length=50)
    behance = models.CharField(blank=True, null=True, max_length=50)
    medium = models.CharField(blank=True, null=True, max_length=50)
    image_url = models.URLField(blank=True, null=True, max_length=300)
    site = models.URLField(blank=True, null=True, max_length=300)
    published = models.BooleanField(default=False, db_index=True)
    interests = models.ManyToManyField('Interest')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.email)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def photo(self):
        return self.image_url or get_gravatar_url(self.email, size=80)

    @property
    def facebook_url(self):
        return "https://facebook.com/{}".format(self.facebook) if self.facebook else None

    @property
    def twitter_url(self):
        return "https://twitter.com/{}".format(self.twitter) if self.twitter else None

    @property
    def linkedin_url(self):
        return "https://www.linkedin.com/in/{}".format(self.linkedin) if self.linkedin else None

    @property
    def github_url(self):
        return "https://github.com/{}".format(self.github) if self.github else None

    @property
    def behance_url(self):
        return "https://www.behance.net/{}".format(self.behance) if self.behance else None

    @property
    def medium_url(self):
        return "https://medium.com/{}".format(self.medium) if self.medium else None


class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return "{}".format(self.name)
