import imp
from django.contrib import admin
from .models import Album,Information,Contact
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(Album)
admin.site.register(Information)
admin.site.register(Contact)
admin.site.unregister(Group)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("song_title", "video_link")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")

admin.site.site_header = "PAR Entertainment"
admin.site.site_title = "Dashboard"

