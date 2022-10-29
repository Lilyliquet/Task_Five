from django.db import models
from datetime import datetime

# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    date_released = models.DateField()
    likes = models.IntegerField()
    
    def __str__(self):
        return self.title


class Lyric(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT)
    song = models.ForeignKey(Song, on_delete=models.RESTRICT)
    content = models.CharField(max_length=900)
    Song_id = models.IntegerField()
    
    def __str__(self):
        return self.content
