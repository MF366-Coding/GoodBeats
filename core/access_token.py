import requests
from datetime import datetime, timedelta
from flask import Flask, request, redirect, jsonify
import base64
import json
import os
from urllib.parse import urlencode

class SpotifyAuth:
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    AUTH_URL = "https://accounts.spotify.com/authorize"
    REDIRECT_URI = "http://localhost:5000/callback"
    CLIENT_ID = "6c47f1feb63e4550988c010b9cd10687"
    CLIENT_SECRET = "5e19d111c36c4f1cb0dbfee37689f910"
    
    def __init__(self):
        self.session = {}

    def get_authorization_url(self):
        params = {
            "client_id": self.CLIENT_ID,
            "response_type": "code",
            "redirect_uri": self.REDIRECT_URI,
            "scope": "user-read-private user-read-email",
            "state": "some_random_state",
            # "show_dialog": True
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

    def get_access_token(self):
        if 'access_token' not in self.session or datetime.now().timestamp() > self.session['expires_in']:
            self.refresh_token()
        return self.session['access_token']

# Example usage in a Flask app
# app = Flask(__name__)
# app.secret_key = '5321-1234-a310'
# spotify_auth = SpotifyAuth()

# @app.route('/')
# def home():
#     return redirect(spotify_auth.get_authorization_url())

# @app.route('/callback')
# def callback():
#     code = request.args.get('code')
#     spotify_auth.exchange_code_for_token(code)
#     return "Authentication successful! You can close this window."

# @app.route('/token')
# def token():
#     access_token = spotify_auth.get_access_token()
#     return jsonify({'access_token': access_token})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',debug=True)