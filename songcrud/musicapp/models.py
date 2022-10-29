from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    sond_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.sond_id.title