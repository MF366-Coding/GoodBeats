# Artist class

# pylint: disable=W0622
# pylint: disable=E0401

import requests
from typing import Any

class Artist:
    def __init__(self, spotify_artist: dict) -> None:
        self._artist = spotify_artist
    
    def ObtainParameter(self, parameter: str) -> Any:
        """
        Retrieve a parameter.

        This should only be used in case there's no equal property.

        :param parameter: The parameter to retrive

        :return: The parameter
        """
        
        return self._artist[parameter]

    @property
    def artistId(self) -> str:
        """
        Return the ID of the artist.

        :return: Artist ID
        """
        
        return self.ObtainParameter("id")

    @property
    def artistName(self) -> str:
        """
        Return the name of the artist.

        :return: Artist name
        """
        
        return self.ObtainParameter("name")

    @property
    def artistFollowers(self) -> int:
        """
        Return the number of followers of the artist.

        :return: Artist followers
        """
        
        return self.ObtainParameter("followers")["total"]

    @property
    def artistPopularity(self) -> int:
        """
        Return the popularity of the artist.

        :return: Artist popularity
        """
        
        return self.ObtainParameter("popularity")

    @property
    def artistGenres(self) -> list[str]:
        """
        Return the genres of the artist.

        :return: Artist genres
        """
        
        return self.ObtainParameter("genres")


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
    
    return Artist(artist_data.json())