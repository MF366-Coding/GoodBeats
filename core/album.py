# Album class.

# pylint: disable=W0622
# pylint: disable=E0401

import requests


class Album:
    pass


def GetAlbumById(id: str, auth) -> Album:
    """
    Retrieve album and return Album object.

    :param id: Album id.
    :param auth: of type AccessTokenClass.
    :return: Album object.
    """
    base_url = f"https://api.spotify.com/v1/albums/{id}"
    album_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )
    print(album_data.json())