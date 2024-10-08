import requests
from datetime import datetime, timedelta
from flask import Flask, request, redirect, jsonify
import base64
import json
import os
from urllib.parse import urlencode


class SpotifyAuth:
    secrets_file = os.path.join(os.path.dirname(__file__), "secret.json")

    if not os.path.exists(secrets_file):
        raise FileNotFoundError(f"Secrets file not found: {secrets_file}")

    
    with open(secrets_file, 'r', encoding='utf-8') as f:
        secrets = json.load(f)

    TOKEN_URL = "https://accounts.spotify.com/api/token"
    AUTH_URL = "https://accounts.spotify.com/authorize"
    REDIRECT_URI = "http://localhost:5000/callback"
    CLIENT_ID = secrets['ClientID']
    CLIENT_SECRET = secrets['ClientSecret']
    
    def __init__(self):
        self.session = {}

    def get_authorization_url(self):
        params = {
            "client_id": self.CLIENT_ID,
            "response_type": "code",
            "redirect_uri": self.REDIRECT_URI,
            # Will need to fix scope asap currently has all permissions which is good for testing
            "scope": "user-read-private user-read-email user-library-read user-library-modify playlist-read-private playlist-modify-public playlist-modify-private user-top-read user-read-recently-played user-read-playback-position user-read-currently-playing user-modify-playback-state user-read-playback-state user-follow-read user-follow-modify",
            "state": "some_random_state",
            # Remove later only for testing
            "show_dialog": True
        }
        auth_url = f"{self.AUTH_URL}?{urlencode(params)}"
        return auth_url

    def exchange_code_for_token(self, code):
        encoded_client_stuff = base64.b64encode(f'{self.CLIENT_ID}:{self.CLIENT_SECRET}'.encode()).decode()
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self.REDIRECT_URI
            },
            headers={
                "Authorization": f"Basic {encoded_client_stuff}",
                "Content-Type": "application/x-www-form-urlencoded"
            }
        )
        token_json = response.json()
        self.session['access_token'] = token_json['access_token']
        self.session['expires_in'] = datetime.now().timestamp() + token_json['expires_in']
        self.session['refresh_token'] = token_json['refresh_token']
        self.session['token_type'] = token_json['token_type']
        self.session['scope'] = token_json['scope']
        
        with open('token.json', 'w') as f:
            json.dump(token_json, f)

    def refresh_token(self):
        if 'refresh_token' not in self.session:
            return redirect(self.get_authorization_url())
        
        if datetime.now().timestamp() > self.session['expires_in']:
            encoded_client_stuff = base64.b64encode(f'{self.CLIENT_ID}:{self.CLIENT_SECRET}'.encode()).decode()
            response = requests.post(
                self.TOKEN_URL,
                data={
                    'grant_type': 'refresh_token',
                    'refresh_token': self.session['refresh_token']
                },
                headers={
                    "Authorization": f"Basic {encoded_client_stuff}",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
            )
            token_json = response.json()
            self.session['access_token'] = token_json['access_token']
            self.session['expires_in'] = datetime.now().timestamp() + token_json['expires_in']
            self.session['token_type'] = token_json['token_type']
            self.session['scope'] = token_json['scope']

    # Probably redundant
    # def get_access_token(self):
    #     if 'access_token' not in self.session or datetime.now().timestamp() > self.session['expires_in']:
    #         self.refresh_token()
    #     return self.session['access_token']

# Basically after all THE SHIT up above this is the abstraction
class AccessTokenClass:
    def __init__(self, token_file='token.json'):
        self.token_file = token_file

    def Generate(self):
        try:
            with open(self.token_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.access_token = data["access_token"]
                self.token_type = data["token_type"]
                return self
        except FileNotFoundError:
            print("AcessTokenClass here, Im calling an error so the error offically means that the file isnt found but its prolly something else")


# Code only if ran from another file
# later


# Example usage in a Flask app
if __name__ == '__main__':
    app = Flask(__name__)
    app.secret_key = '5321-1234-a310'
    spotify_auth = SpotifyAuth()

    @app.route('/')
    def home():
        return redirect(spotify_auth.get_authorization_url())

    @app.route('/callback')
    def callback():
        code = request.args.get('code')
        spotify_auth.exchange_code_for_token(code)
        return "Authentication successful! You can close this window."

    @app.route('/token')
    def token():
        access_token = spotify_auth.get_access_token()
        return jsonify({'access_token': access_token})

    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=True)
        # print token
        print(token())