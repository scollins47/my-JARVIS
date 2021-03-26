import spotipy
from spotipy_methods 
from spotipy import util
#must change scope for different method types
scope = 'user-modify-playback-state'
token = util.prompt_for_user_token('mlinspinship16', scope, redirect_uri='http://localhost:8080' ,client_id = 'bcf93d38d48440ca800ece19fab24511', client_secret = '75da85585a664043956cacd3a22bf6e9')

if token:
	sp = spotipy.Spotify(auth=token)
	sp.add_to_queue('4p1ajZ2s5MGd5pg3knrI2D')