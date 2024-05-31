from rest_framework import generics, status
from rest_framework.response import Response
from .models import DiaryEntry, Music, Tag
from .serializers import DiaryEntrySerializer, MusicSerializer, TagSerializer
from tags.utils import extract_keywords

class CreateDiaryEntryView(generics.CreateAPIView):
    queryset = DiaryEntry.objects.all()
    serializer_class = DiaryEntrySerializer

    def perform_create(self, serializer):
        diary_entry = serializer.save()
        keywords = extract_keywords(diary_entry.content)
        if keywords:
            for keyword in keywords:
                tag, created = Tag.objects.get_or_create(name=keyword)
                tag.entries.add(diary_entry)

class CreateMusicView(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class TagListView(generics.ListAPIView):
    serializer_class = MusicSerializer

    def get_queryset(self):
        tag_id = self.kwargs['tagId']
        tag = Tag.objects.get(id=tag_id)
        entries = tag.entries.all()
        music_ids = entries.values_list('music', flat=True)
        return Music.objects.filter(id__in=music_ids)
