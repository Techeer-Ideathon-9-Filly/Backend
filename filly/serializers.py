from rest_framework import serializers
from .models import DiaryEntry, Music, Tag

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist', 'genre']

class DiaryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaryEntry
        fields = ['id', 'title', 'content', 'created_at', 'music']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
