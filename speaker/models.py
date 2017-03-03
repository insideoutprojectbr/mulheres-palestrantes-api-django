from django.db import models
from django.utils.timezone import now


class Speaker(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(unique=True, max_length=100, db_index=True)
    location = models.CharField(blank=True, null=True, max_length=100, db_index=True)
    github = models.CharField(blank=True, null=True, max_length=20)
    facebook = models.CharField(blank=True, null=True, max_length=20)
    linkedin = models.CharField(blank=True, null=True, max_length=20)
    published = models.BooleanField(default=False, db_index=True)
    interests = models.ManyToManyField('Interest')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.email)


class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return "{}".format(self.name)
