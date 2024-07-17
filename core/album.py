# Album class.

# pylint: disable=W0622
# pylint: disable=E0401

import requests
from typing import Any


class Album:
    def __init__(self, spotify_album: dict):
        self._album = spotify_album

    def ObtainParameter(self, parameter: str) -> Any:
        """
        Retrieve a parameter.

        This should only be used in case there's no equal property.

        :param parameter: The parameter to retrive

        :return: The parameter
        """

        return self._album[parameter]


def GetAlbumById(id: str, auth) -> Album:
    """
    Retrieve album and return Album object.

    :param id: Album id.
    :param auth: of type AccessTokenClass.
    :return: Album object.
    
    Tip that i learnt after an hr: Playlists are not albums.
    
    """
    base_url = f"https://api.spotify.com/v1/albums/{id}"
    album_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )
    print(album_data.json())