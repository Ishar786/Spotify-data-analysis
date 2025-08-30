from dotenv import load_dotenv
import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load env vars
load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise Exception("Spotify credentials not found in .env")

# Auth
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(client_id=client_id,
                                          client_secret=client_secret)
)

# Collect tracks with pagination
tracks = []
query = "arijit singh"
limit = 50  # max per request
offset = 0

while True:
    results = sp.search(q=query, type="track", limit=limit, offset=offset)
    items = results["tracks"]["items"]
    if not items:  # no more results
        break

    for item in items:
        track_info = {
            "track_name": item["name"],
            "artist": item["artists"][0]["name"],
            "id": item["id"]
        }

        try:
            features = sp.audio_features([item["id"]])[0]
            if features:  # sometimes None
                track_info.update(features)
        except Exception as e:
            print(f"Skipping {item['name']} ({item['id']}): {e}")

        tracks.append(track_info)

    offset += limit

# Save to CSV
df = pd.DataFrame(tracks)
df.to_csv("spotify_tracks.csv", index=False)
print(f"Saved {len(df)} tracks with audio features to spotify_tracks.csv")
