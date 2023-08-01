from rest_framework import serializers 

from .models import Song, Album, Artist, Playlist, PlaylistSong

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Album
        fields = ('url','id','name')

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Artist
        fields = ('url', 'id', 'name')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    album = AlbumSerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)
    album_id = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all(), source='album', write_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(), source='artist', write_only=True)

    class Meta:
        model = Song
        fields = ('url', 'id', 'title', 'remote_url', 'album_id', 'artist_id', 'album', 'artist')

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Playlist
        fields = ('url', 'id', 'name')

class PlaylistSongSerializer(serializers.HyperlinkedModelSerializer):
    playlist = PlaylistSerializer(read_only=True)
    song = SongSerializer(read_only=True)
    playlist_id = serializers.PrimaryKeyRelatedField(queryset=Playlist.objects.all(), source='playlist', write_only=True)
    song_id = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), source='song', write_only=True)

    class Meta:
        model = PlaylistSong
        fields = ('url', 'id', 'playlist_id', 'playlist', 'song_id', 'song', 'created_at')