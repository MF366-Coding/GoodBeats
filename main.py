from flask import Flask, jsonify, request, redirect
import requests
from core.access_token import SpotifyAuth

app = Flask(__name__)

@app.route('/playlists', methods=['GET'])
def get_playlists():
    # Initialize the SpotifyAuth instance
    spotify_auth = SpotifyAuth()

    # Get the access token
    try:
        access_token = spotify_auth.get_access_token()
    except KeyError as e:
        return jsonify({"error": str(e)}), 401

    # Define the endpoint to get the user's playlists
    playlists_url = "https://api.spotify.com/v1/me/playlists"

    # Make the request to the Spotify Web API
    response = requests.get(
        playlists_url,
        headers={
            "Authorization": f"Bearer {access_token}"
        },
        timeout=1
    )

    # Check if the request was successful
    if response.status_code == 200:
        playlists = response.json()
        return jsonify(playlists)
    else:
        return jsonify({"error": "Failed to get playlists", "status_code": response.status_code, "response": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)