from django.contrib import admin
from .models import Music, DiaryEntry, Tag

admin.site.register(Music)
admin.site.register(DiaryEntry)
admin.site.register(Tag)
