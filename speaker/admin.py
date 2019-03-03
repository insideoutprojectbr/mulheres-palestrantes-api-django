from django.contrib import admin

from speaker.models import Speaker, Interest


class SpeakerAdmin(admin.ModelAdmin):
    pass


class InterestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Interest, InterestAdmin)
