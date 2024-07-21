import requests
from typing import Any


class Playlist:
    def __init__(self, spotifyPlaylist: dict) -> None:
        """
        Initialize the Playlist class with the Spotify playlist data.

        :param spotifyPlaylist: Spotify playlist data.
        """

        self._playlist  = spotifyPlaylist


    def ObtainParameter(self, parameter: str) -> Any:
        """
        Retrieve a parameter.

        This should only be used in case there's no equal property.

        :param parameter: The parameter to retrive

        :return: The parameter
        """
        
        return self._playlist[parameter]
    
    @property
    def playlistId(self) -> str:
        """
        Return the ID of the playlist.

        :return: Playlist ID
        """
        return self.ObtainParameter("id")

    @property
    def playlistName(self) -> str:
        """
        Return the name of the playlist.

        :return: Playlist name
        """
        return self.ObtainParameter("name")

    @property
    def playlistDescription(self) -> str:
        """
        Return the description of the playlist.

        :return: Playlist description
        """
        return self.ObtainParameter("description")

    @property
    def playlistTracks(self) -> dict:
        """
        Return the tracks of the playlist.

        :return: Tracks of the playlist
        """
        return self.ObtainParameter("tracks")
        
        
        
def getPlaylistById(playlist_id: str, auth) -> Playlist:
    """
    Retrieve playlist details by playlist ID.

    :param playlist_id: The ID of the playlist.
    :return: Playlist details as a dictionary.
    """
    base_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    response = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )

    match response.status_code:
        case 401:
            print("Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user..")
        case 403:
            print("Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won't help here.")
        case 429:
            print("The app has exceeded its rate limits.")

    playlist_data = response.json()

    return Playlist(playlist_data)
    
    


