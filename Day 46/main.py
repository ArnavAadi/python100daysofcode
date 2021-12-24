from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

year = input("which year songs you want to listen: ")
response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{year}-01-01/")
page = response.text
soup = BeautifulSoup(page, "html.parser")
songs_tags = soup.select("li ul li h3", class_="")
songs = []
for song in songs_tags:
    song_title = song.text.replace("\n", "")
    songs.append(song_title)
print(songs)

client_id = "00884983bbd0421c90401eec99acb507"
client_secret = "7e66107ddf204dcba23d3db824a8977e"
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                     client_id=client_id, client_secret=client_secret, show_dialog=True, cache_path="token.txt", redirect_uri="https://www.billboard.com/charts/hot-100"))

user_id = sp.current_user()["id"]

sp_res = sp.current_user()
id = "mm8yu363v2u16rk0m7n5a9s4z"

song_uris = []
year = f"{year}-01-01".split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
