# Artist class

import requests
from .access_token import AccessTokenClass

class Artist:
    pass

def GetArtistById(id: str, auth: AccessTokenClass) -> Artist:
    """
    Retrieve album and return Album object.

    :param id: Album id.
    :param auth: of type AccessTokenClass.
    :return: Album object.
    """
    base_url = f"https://api.spotify.com/v1/artists/{id}"
    artist_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )
    print(artist_data.json())