# Get access token.

# pylint: disable=W0622
# pylint: disable=E0401

# TODO; FIXME

import json
import os
import requests
import secrets
import base64


class AccessTokenClass:
    access_token: str
    token_type: str

    def __init__(self) -> None:
        self.access_token = ""
        self.token_type = ""
        self.scopes = ''
        self.refresh_token = ''

    def Generate(self):
        """
        Generate access token.
        """
        # [*] Read secret.json
        # [!?] imagine not having access to it

        where_are_we = os.path.dirname(__file__)
        
        try:
            with open(f"{where_are_we}/secret.json", "rt", encoding="UTF-8") as secret:
                values = json.loads(secret.read())

        except FileNotFoundError:
            # [*] Try finding it in the parent directory
            with open(f"{where_are_we}/../secret.json", "rt", encoding="UTF-8") as secret:
                values = json.loads(secret.read())

        state = secrets.token_urlsafe(16)

        authorization = requests.get(
            "https://accounts.spotify.com/authorize",
            data={
                "client_id": values['ClientID'],
                "response_type": "code",
                "redirect_uri": "http://localhost:8080",
                "state": state,
                "scope": "playlist-read-private playlist-modify-private playlist-modify-public user-read-playback-position user-top-read user-read-recently-played user-library-modify user-library-read user-read-email user-read-private",
                "show_dialog": False,
                "client_secret": values['ClientSecret']
            },
            timeout=1
        )

        # Base64 encoding stuff
        encoded_client_stuff = base64.b64encode(bytes(f'{values["ClientID"]}:{values["ClientSecret"]}', encoding='utf-8'))

        print(authorization.text)

        some_shite = requests.post(
            "https://accounts.spotify.com/authorize",
            data={
                "grant_type": "authorization_code",
                "response_type": authorization.text,
                "redirect_uri": "http://localhost:8080",
            },
            headers={
                "Authorization": f"Basic {str(encoded_client_stuff, encoding='utf-8')}",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            timeout=1
        )

        print(some_shite.json())

        # [i] This took 2 hours to figure out btw ^^^^^^^^^^^^^^^^^^ (skill issue :trollface:)
        token_json = some_shite.json()
        self.access_token, self.token_type, self.scopes, self.refresh_token = token_json["access_token"], token_json["token_type"], token_json['scope'], token_json['refresh_token>']
                
        # [*] return this type of class itself with self.access_token and self.token_type
        return self

    def RefreshCurrentToken(self):
        where_are_we = os.path.dirname(__file__)

        try:
            with open(f"{where_are_we}/secret.json", "rt", encoding="UTF-8") as secret:
                values = json.loads(secret.read())

        except FileNotFoundError:
            # [*] Try finding it in the parent directory
            with open(f"{where_are_we}/../secret.json", "rt", encoding="UTF-8") as secret:
                values = json.loads(secret.read())

        # Base64 encoding stuff
        encoded_client_stuff = base64.b64encode(f'{values["ClientID"]}:{values["ClientSecret"]}')

        some_shite = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "client_id": values['ClientID'],
            },
            headers={
                "Authorization": f"Basic {str(encoded_client_stuff, encoding='utf-8')}",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            timeout=1
        )

        token_json = some_shite.json()

        self.access_token, self.token_type, self.scopes, self.refresh_token = token_json["access_token"], token_json["token_type"], token_json['scope'], token_json['refresh_token>']

        return self


