# Artist class

# pylint: disable=W0622
# pylint: disable=E0401

import requests


class Artist:
    pass

def GetArtistById(id: str, auth) -> Artist:
    """
    Retrieve artist and return Artist object.

    :param id: Artist id.
    :param auth: of type AccessTokenClass.
    :return: Artist object.
    """
    base_url = f"https://api.spotify.com/v1/artists/{id}"
    artist_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )
    print(artist_data.json())