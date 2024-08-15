import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd
import seaborn as sns
load_dotenv()
def get_artist_top_tracks(artist_id):
    """Gets the top 10 tracks of an artist."""
    client_id = os.environ.get("CLIENT_ID")
    client_secret = os.environ.get("CLIENT_SECRET")

    

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.artist_top_tracks(artist_id,)  
    tracks = results['tracks'][:10]

    track_data = [{
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_ms': track['duration_ms']
    } for track in tracks]

    return track_data
     

artist_id = '7dGJo4pcD2V6oG8kP0tJRR'  
df = pd.DataFrame(get_artist_top_tracks(artist_id))
print(df)

scatter_plot = sns.scatterplot(data = df, x = "popularity", y = "duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")




