from django.db import models

class Album(models.Model):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    remote_url = models.CharField(max_length=500, blank=True)
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class SingletonModel(models.Model):
    '''
    base class to use for table with one row to store app settings
    '''
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SongApiUserSettings(SingletonModel):
    source_ip = models.CharField(max_length=255, blank=True)
    source_script_path = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Song API User Setting"

    class Meta:
        verbose_name = "Song API User Setting"

class SongApiSourceFiles(SingletonModel):
    source_files = models.TextField(blank=True)

    def __str__(self):
        return "Song API Source File"

    class Meta:
        verbose_name = "Song API Source File"

class Playlist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.playlist.name + ' - ' + self.song.title
