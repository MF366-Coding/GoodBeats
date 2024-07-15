# Get access token.

# pylint: disable=W0622
# pylint: disable=E0401

import json
import os
import requests


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
        # [*] Read secret.json
        # [!?] imagine not having access to it

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
            
            # [i] This took 2 hours to figure out btw ^^^^^^^^^^^^^^^^^^ (skill issue :trollface:)
            self.access_token, self.token_type = some_shite.json()["access_token"], some_shite.json()["token_type"]
