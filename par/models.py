from django.db import models

class Album(models.Model):
    song_title = models.CharField(max_length=500)
    video_link = models.URLField()
    thumbnail = models.ImageField(upload_to='thumbnail')
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.song_title


class Information(models.Model):
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    youtube_channel = models.URLField()
    twitter_link = models.URLField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"
    
