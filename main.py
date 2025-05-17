from bs4 import *
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "353ad4d8628145399babecc9f9d63ddb"
CLIENT_SECRET = "e868b480a5a84d698dd5f8ae257e9399"
USERNAME="31nc43mh37nzo6pzohrxsduymf4a"

date=input("Enter the date in YYYY-MM-DD format: ")

year=date.split("-")[0]
month=date.split("-")[1]
day=date.split("-")[2]
url="https://www.billboard.com/charts/hot-100/"+date+"/"

response=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
if response.status_code==200:
    print("Success")

soup=BeautifulSoup(response.text,"html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


scope = "user-library-read"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=USERNAME,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id= sp.current_user()["id"]

all_uris=[]
for song in song_names:
    result=sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uri=result["tracks"]["items"][0]["uri"]
        #print(f"Found {song} in Spotify")
        all_uris.append(song_uri)
    except IndexError:
        print(f"{song} not found in Spotify")
        continue
    
playlist_id = sp.user_playlist_create(user=user_id, name=f"{month} {day}, {year} Billboard 100", public=False)
sp.playlist_add_items(playlist_id["id"], all_uris)
