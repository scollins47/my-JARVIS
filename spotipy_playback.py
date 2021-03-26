import spotipy
import spotipy_methods as sm
import file_method_helper as fm
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import pprint
# pre: the user file name in Spotipy_data/clients as well as the client_id and secret
# post: generates json with data 
def make_user(user):# needs error checking
	filepath_write = 'Spotipy_data/'+user+'.txt'
	fm.write_to_json(sm.read_spot_data(user), filepath_write, user)

#@param user: String, the name of the client MUST HAVE DATA FILE ASSOCIATED
#@param scope2: String, the scope to use can be found here:
#https://developer.spotify.com/documentation/general/guides/scopes/
#@returns: the token (could be not-authenticated)
def get_client_creds(user):
	filepath = "Spotipy_data/"+user+".txt"
	data = fm.read_from_json(filepath)
	return data
def authenticate(user, scope2):
	data = get_client_creds(user)
	username = data['username']
	client_id = data['client_id']
	client_secret = data['client_secret']
	scope = scope2
	red = 'http://localhost:8080'
	token = util.prompt_for_user_token(username, scope, redirect_uri = red, client_id = client_id, client_secret = client_secret)
	return token

#get_playlist_from_user helper method
def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
		print("    {0} {1} {2}".format(i, track['artists'][0]['name'],
									 track['name']))
#@param user: the user to access spotify data from
def get_playlist_from_user(user):
	authenticate(user, 'playlist-read-private')
	if token:
		sp = spotipy.Spotify(auth=token)
		playlists = sp.user_playlists(username)
		for playlist in playlists['items']:
			if playlist['owner']['id'] == username:
				print()
				print(playlist['name'])
				print('total tracks' , playlist['tracks']['total'])
				results = sp.playlist(playlist['id'],
									  fields="tracks,next")
				tracks = results['tracks']
				show_tracks(tracks)
				while tracks['next']:
					tracks = sp.next(tracks)
					show_tracks(tracks)
	else:
		print("cant get token for", username)
# pre: a valid user.txt in Spotipy_data/ as well as a track uri
# post: queues the track 
def queue_song(user, track_uri = '4p1ajZ2s5MGd5pg3knrI2D'):
	token = authenticate(user, 'user-modify-playback-state')
	sp = spotipy.Spotify(auth=token)
	sp.add_to_queue(track_uri)
	print('added song to queue')
# pre: a user with user data
# post: pauses current song
def pause(user):
	token = authenticate(user, 'user-modify-playback-state')
	sp = spotipy.Spotify(auth=token)
	sp.pause_playback()
	print('song paused')
#pre: a user with user data
#post: skips a song in the playback
def skip(user):
	token = authenticate(user, 'user-modify-playback-state')
	sp = spotipy.Spotify(auth = token)
	sp.next_track()
	print('skipped track')
#pre: a user with user data
#post: rewinds a song
def previous(user):
	token = authenticate(user, 'user-modify-playback-state')
	sp = spotipy.Spotify(auth = token)
	sp.previous_track()
	print('Going back')
def volume(user, volume):
	token = authenticate(user, 'user-modify-playback-state')
	sp = spotipy.Spotify(auth = token)
	sp.volume(volume)
	print('set volume to '+volume)
def search_artist_track(user, artist_name = 'A$AP%20ROCKY', track_name ='Excuse%20Me'):
	data = get_client_creds(user)
	token = spotipy.util.prompt_for_user_token(username=data['username'], client_id=data['client_id'], client_secret=data['client_secret'], redirect_uri='localhost:8080')
	spotify = spotipy.Spotify(token)#WIP
	query = 'name:'+track_name+'%20artist:'+artist_name
	result = spotify.search(q=query, limit = 10)
	return result
