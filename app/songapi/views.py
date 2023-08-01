from distutils.util import strtobool
from rest_framework import viewsets 

from rest_framework.decorators import api_view, permission_classes #for no model 
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from rest_framework import filters

from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer, PlaylistSerializer, PlaylistSongSerializer

from .models import Song, Album, Artist, Playlist, PlaylistSong, SongApiUserSettings, SongApiSourceFiles

from .extra_methods import SongProcessing

class AlbumViewSet(viewsets.ModelViewSet): 
	permission_classes = (IsAuthenticated,)
	'''
	model based:
	define queryset
	specify serializer to be used
	set fields to allow automated search queries, 
	note:
	foreign key uses double underscore notation	(double underscore for search into relatred table)
	'''
	queryset = Album.objects.all()  
	serializer_class = AlbumSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['name'] 

class ArtistViewSet(viewsets.ModelViewSet): 
	permission_classes = (IsAuthenticated,)

	queryset = Artist.objects.all()  
	serializer_class = ArtistSerializer 
	filter_backends = [filters.SearchFilter]
	search_fields = ['name'] 

class SongViewSet(viewsets.ModelViewSet): 
	permission_classes = (IsAuthenticated,)

	queryset = Song.objects.all()  
	serializer_class = SongSerializer 
	filter_backends = [filters.SearchFilter]
	search_fields = ['title', 'album__name', 'artist__name']  

class PlaylistViewSet(viewsets.ModelViewSet):  
	permission_classes = (IsAuthenticated,)

	queryset = Playlist.objects.all()  
	serializer_class = PlaylistSerializer 
	filter_backends = [filters.SearchFilter]
	search_fields = ['name'] 

class PlaylistSongViewSet(viewsets.ModelViewSet):  
	permission_classes = (IsAuthenticated,)

	queryset = PlaylistSong.objects.all()  
	serializer_class = PlaylistSongSerializer 
	filter_backends = [filters.SearchFilter]
	search_fields = ['playlist__id', 'song__id', 'playlist__name', 'song__title', 'created_at'] 

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def settings(request):
	
	if request.method == 'GET':
		obj = SongApiUserSettings.objects.all().values()
		returnData = obj
		return Response(returnData)

	if request.method == 'POST':
		objSettings = SongApiUserSettings.objects.first()
		objSettings.source_ip = request.POST.get('source_ip')
		objSettings.source_script_path = request.POST.get('source_script_path')
		objSettings.save()
		returnData = SongApiUserSettings.objects.all().values()
		return Response(returnData)

	return Response({"message": "settings, GET settings values, POST new settings values"})

@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def refresh(request):

	if request.method == 'PUT':
		objSongs = SongProcessing()
		returnData = objSongs.RefreshSongs()
		return Response(returnData)

	return Response({"message": "PUT perform refresh to update DB"})

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def randomplaylist(request):
	
	if request.method == 'GET':
		obj = SongApiUserSettings.objects.all().values()
		returnData = obj
		return Response({"message": "POST name and number of songs to create random playlist"})

	if request.method == 'POST':
		objSongs = SongProcessing()
		plName = request.POST.get('name')
		plNumber = request.POST.get('amount')
		# print(request.POST.get('name'))
		returnData = objSongs.CreateRandomPlaylist(plName, plNumber)
		return Response(returnData)

	return Response({"message": "POST name and number of songs to create random playlist"})
