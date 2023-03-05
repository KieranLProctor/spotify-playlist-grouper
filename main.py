import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need a username!")
    print("usage: python main.py [username]")
    sys.exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))

playlists = sp.user_playlists(username)

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
