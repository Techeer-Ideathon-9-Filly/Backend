from django.urls import path
from .views import CreateDiaryEntryView, CreateMusicView, TagListView

urlpatterns = [
    path('diary/', CreateDiaryEntryView.as_view(), name='create_diary_entry'),
    path('music/', CreateMusicView.as_view(), name='create_music'),
    path('tags/<int:tagId>', TagListView.as_view(), name='filter_by_tag'),
]
