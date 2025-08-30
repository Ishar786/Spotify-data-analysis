import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Authenticate
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Example: Fetch playlist
playlist_link = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"  # Today's Top Hits
playlist_uri = playlist_link.split("/")[-1].split("?")[0]

results = sp.playlist_tracks(playlist_uri)

tracks = []
for item in results["items"]:
    track = item["track"]
    tracks.append({
        "track_name": track["name"],
        "artist": track["artists"][0]["name"],
        "album": track["album"]["name"],
        "release_date": track["album"]["release_date"],
        "popularity": track["popularity"],
        "duration_ms": track["duration_ms"]
    })

df = pd.DataFrame(tracks)
df.to_csv("data/raw_spotify_data.csv", index=False)
print("Data saved to data/raw_spotify_data.csv")
