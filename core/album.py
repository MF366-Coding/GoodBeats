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
    
    @property
    def albumId(self) -> str:
        """
        Return the ID of the album.

        :return: Album ID
        """
        
        return self.ObtainParameter("id")
    
    @property
    def albumName(self) -> str:
        """
        Return the name of the album.

        :return: Album name
        """
        
        return self.ObtainParameter("name")
    
    @property
    def albumArtists(self) -> list:
        """
        Return the artists of the album.

        :return: Album artists
        """
        
        return self.ObtainParameter("artists")
    
    @property
    def albumTracks(self) -> dict:
        """
        Return the tracks of the album.

        :return: Album tracks
        """
        
        return self.ObtainParameter("tracks")
    
    def singularTrack(self, track_number: int) -> dict:
        """
        Return a singular track of the album.

        :param track_number: The track number

        :return: Singular track
        """
        track_number -= 1
        return self.albumTracks["items"][track_number]
    
    @property
    def albumGenres(self) -> list[str]:
        """
        Return the genres of the album.

        :return: Album genres
        """
        
        return self.ObtainParameter("genres")

    @property
    def albumPopularity(self) -> int:
        """
        Return the popularity of the album.

        :return: Album popularity
        """
        
        return self.ObtainParameter("popularity")

    @property
    def albumReleaseDate(self) -> str:
        """
        Return the release date of the album.

        :return: Album release date
        """
        
        return self.ObtainParameter("release_date")

    @property
    def albumReleaseDatePrecision(self) -> str:
        """
        Return the release date precision of the album.

        :return: Album release date precision
        """
        
        return self.ObtainParameter("release_date_precision")

    @property
    def albumTotalTracks(self) -> int:
        """
        Return the total tracks of the album.

        :return: Album total tracks
        """
        
        return self.ObtainParameter("total_tracks")

    @property
    def albumType(self) -> str:
        """
        Return the type of the album.

        :return: Album type
        """
        
        return self.ObtainParameter("type")

    @property
    def albumLabel(self) -> str:
        """
        Return the label of the album.

        :return: Album label
        """
        
        return self.ObtainParameter("label")



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
    
    return Album(album_data.json())