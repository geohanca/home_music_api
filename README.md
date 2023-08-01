# Home Music API  

- REST api to organize, catalog local mp3 files

### technologies used  
  
 - Django 3  
 - django rest framework  
 - eyed3 to read mp3 file metadata (i.e. song title, artist, album, etc)  
 - psycopg2 to connect to postgresql database  
 - python-dotenv for environment variables (.env file)  
 - urllib3 for opening mp3 files to read metadata
 - python venv environment for development  
 - docker for deployment   

**require .env file in project root in the following format**  
DJANGO_SECRET=  
DATABASE_NAME=  
DATABASE_USER=  
DATABASE_PASSWORD=  
DATABASE_HOST_IP=  
DATABASE_PORT=  
CORS_ALLOWED_LIST=  
ADMIN_USER_NAME=  
ADMIN_USER_EMAIL=  
ADMIN_USER_PASSWORD=  

**required postgresql database running on the local network with a database already created**


## Endpoints  

**GET songapi/song/**  
- return json of all songs in database  
- id, title, remote_url, album, artist  
- search allowed, songapi/song/?search=  

**POST songapi/song/**  
- write song data to database  
- title, remote_url, album_id, artist_id  

**GET songapi/album/**  
- return json of all albums in database  
- id, name  
- search allowed, songapi/album/?search=  

**POST songapi/album/**  
- write album data to database  
- name  

**GET songapi/artist/**  
- return json of all artists in database  
- id, name  
- search allowed, songapi/artist/?search=  

**POST songapi/artist/**  
- write artist data to database  
- name  

**GET songapi/playlist/**  
- return json of all playlist names in database  
- id, name  
- search allowed, songapi/playlist/?search=  

**POST songapi/playlist/**  
- write playlist name to database  
- name  

**GET songapi/playlistsong/**  
- return json of all linked playlists and songs (join table)  
- id, playlist_id, song_id  
- search allowed, songapi/playlistsong/?search=  

**POST songapi/playlistsong/**  
- write linked playlist and song id's to database
- playlist_id, song_id  

**GET songapi/settings/**  
- read all user settings  
- id, source_ip, source_script_path  

**POST songapi/settings/**  
- write user settings to database  
- source_ip, source_script_path  

**PUT songapi/refresh/**  
- return json of both mp3 files added to database and deleted from database  
- when files are added to or deleted from the local harddrive the refresh  
endpoint will update the database to reflect the files in the directory path

**GET songapi/randomplaylist/**  
- return json message  

**POST songapi/randomplaylist/**  
- create new playlist with designated number of random songs
- name=newplaylistname, amount=numberofsongs  
