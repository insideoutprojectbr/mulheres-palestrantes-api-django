import logging

from django.conf import settings
from django_gravatar.helpers import get_gravatar_url
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save
from oauth2_provider.models import Application
from hashid_field import HashidField

logger = logging.getLogger()


class User(AbstractUser):
    email = models.EmailField(
        unique=True, max_length=200, db_index=True, blank=True, null=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)


class Speaker(models.Model):
    email = models.EmailField(unique=True, max_length=200, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
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
    updated_at = models.DateTimeField(auto_now=True)
    interests = models.ManyToManyField("Interest")
    user = models.OneToOneField("User", blank=True, null=True)
    confirmation_key = HashidField(blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.name, self.email)

    @property
    def photo(self):
        return self.image_url or get_gravatar_url(self.email, size=80)

    @property
    def facebook_url(self):
        return (
            "{}{}".format(settings.FACEBOOK_URL, self.facebook)
            if self.facebook
            else None
        )

    @property
    def twitter_url(self):
        return (
            "{}{}".format(settings.TWITTER_URL, self.twitter) if self.twitter else None
        )

    @property
    def linkedin_url(self):
        return (
            "{}{}".format(settings.LINKEDIN_URL, self.linkedin)
            if self.linkedin
            else None
        )

    @property
    def github_url(self):
        return "{}{}".format(settings.GITHUB_URL, self.github) if self.github else None

    @property
    def behance_url(self):
        return (
            "{}{}".format(settings.BEHANCE_URL, self.behance) if self.behance else None
        )

    @property
    def medium_url(self):
        return "{}{}".format(settings.MEDIUM_URL, self.medium) if self.medium else None


@receiver(post_save, sender=Speaker)
def model_post_save(sender, **kwargs):
    user = kwargs["instance"]
    try:
        Application.objects.get_or_create(
            name="password",
            user=user,
            client_type="public",
            authorization_grant_type="password",
            skip_authorization=True,
        )
        logger.info("An application was generated for user {}".format(user))
    except Exception as e:
        logger.error("Couldn't generate an application for user {} ".format(user))


class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return "{}".format(self.name)
