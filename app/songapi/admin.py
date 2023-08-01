from django.contrib import admin
from .models import SongApiUserSettings, SongApiSourceFiles, Playlist, PlaylistSong

admin.site.register(SongApiUserSettings)
admin.site.register(SongApiSourceFiles)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
