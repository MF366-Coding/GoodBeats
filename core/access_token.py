# Get access token.

import json
import os
import requests
import base64

class AccessTokenClass:
    access_token: str
    token_type: str

    def __init__(self) -> None:
        self.access_token = ""
        self.token_type = ""

    def Generate(self) -> None:
        """
        Generate access token.
        """
        # Read secret.json
        # imagine not having access to it

        where_are_we = os.path.dirname(__file__)
        with open(f"{where_are_we}/secret.json", "rt", encoding="UTF-8") as secret:
            values = json.loads(secret.read())
            some_shite = requests.post(
                "https://accounts.spotify.com/api/token",
                data={
                    "grant_type": "client_credentials",
                    "client_id": values['ClientID'],
                    "client_secret": values['ClientSecret']
                }
            )
            # This took 2 hours to figure out btw ^^^^^^^^^^^^^^^^^^
            self.access_token, self.token_type = some_shite.json()["access_token"], some_shite.json()["token_type"]