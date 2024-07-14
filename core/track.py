# Track class and api

import requests
from .access_token import AccessTokenClass

class Track:
    pass

def GetTrackById(id: str, auth: AccessTokenClass) -> Track:
    """
    Retrieve song and return Track object.

    :param id: Song id.
    :param auth: of type AccessTokenClass.
    :return: Track object.
    """
    base_url = f"https://api.spotify.com/v1/tracks/{id}"
    track_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )
    print(track_data.json())