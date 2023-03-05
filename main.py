import sys
import spotipy
import pickle
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

# Init username incase needing to login.
username = ""
auth_user()

# Since this is a private project => using all scopes.
scopes = ["ugc-image-upload", "user-read-playback-state", "app-remote-control", "user-modify-playback-state", "playlist-read-private", "user-follow-modify", "playlist-read-collaborative", "user-follow-read", "user-read-currently-playing",
          "user-read-playback-position", "user-library-modify", "playlist-modify-private", "playlist-modify-public", "user-read-email", "user-top-read", "streaming", "user-read-recently-played", "user-read-private", "user-library-read"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

playlists = sp.current_user_playlists()

# print(str(playlists))

with open("playlists.json", "a") as file:
    file.write(str(playlists))

# results = sp.current_user_saved_tracks()

# with open("liked_tracks.txt", "a") as file:
#     for idx, item in enumerate(results['items']):
#         track = item['track']
#         print(idx, track['artists'][0]['name'], " – ", track['name'])
#         file.write(
#             str([idx, track['artists'][0]['name'], " – ", track['name']]))


def auth_user():
    # If user has already logged in => can get token from file.
    if os.file.exists(".cache"):
        return

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need a username!")
        print("usage: python main.py [username]")
        sys.exit()
