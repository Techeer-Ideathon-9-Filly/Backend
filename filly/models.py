from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class DiaryEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    entries = models.ManyToManyField(DiaryEntry, related_name='tags')

    def __str__(self):
        return self.name
