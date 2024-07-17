# Track class and api

# pylint: disable=W0622
# pylint: disable=E0401

import requests
from typing import Any


class Track:
    def __init__(self, spotify_track: dict):
        self._track = spotify_track

    def ObtainParameter(self, parameter: str) -> Any:
        """
        Retrieve a parameter.

        This should only be used in case there's no equal property.

        :param str: The parameter to retrive

        :return: The parameter
        """
        
        return self._track[parameter]

    @property
    def album_id(self) -> str:
        """
        Return the ID of the album where this track is.

        :return: Album ID
        """
        
        return self.ObtainParameter("album")["id"] # [i] this can be used to get the album
    
    @property
    def artist_ids(self) -> list[str]:
        """
        Return the IDs of the artists.
        
        The list is sorted by the following order:
        - Main Artist
        - Featured Artist(s)
        
        :return: Artist ID
        """
        
        ids: list[str] = []
        
        for artist in self.ObtainParameter('artists'):
            ids.append(artist['id'])
        
        return ids
    
    @property
    def track_duration(self) -> int:
        """
        Return the duration of the track in miliseconds.
        
        :return: Duration of the track (ms)
        """
        
        return self.ObtainParameter('duration_ms')
    
    @property
    def explicit(self) -> bool:
        """
        Is the song explicit (a.k.a. contains slurs/swearing)?
        
        :return: Boolean that represents if the song is explicit
        """
        
        # [*] explicit songs eh eh :smiling_imp:
        return self.ObtainParameter('explicit')

    @property
    def is_playable(self) -> bool:
        """
        Can the song be played in the current market?
        
        If no information available, assuming it can.
        
        :return: Boolean that represents if the song can be played in the current market
        """
        
        if 'is_playable' not in self._track:
            # [i] In here, I assume the track is playable because of the song examples I used to test
            return True
        
        return self.ObtainParameter('is_playable')
    
    @property
    def track_name(self) -> str:
        """
        Uhhhh... It really can't get more obvious that this...
        
        Returns the name of the track.
        
        :return: Name of the track
        """
        
        return self.ObtainParameter('name')
    
    @property
    def popularity(self) -> int:
        """
        How popular is the song from 0 to 100?
        
        Returns the level of popularity of the track.
        
        NOTE: This value does not update in real-time.
        According to Spotify, it might take days until this value gets updated.
        
        :return: Level of popularity
        """
        
        return self.ObtainParameter('popularity')
    
    @property
    def preview_url(self) -> str | None:
        """
        Link to a 30 sec preview of the song.
        
        NOTE TO THE DEVS: We can use this later by making a request
        and getting the bytes (response.content).
        
        If not available, will return None.
        
        :return: Link to song preview (None if none available)
        """
        
        return self.ObtainParameter('preview_url')
    
    
def GetTrackById(id: str, auth, printJson: bool = False) -> Track:
    """
    Retrieve song and return Track object.

    :param id: Song id.
    :param auth: of type AccessTokenClass.
    :param printJson: Print the JSON data. Defaults to False.
    :return: Track object.
    """
    
    base_url = f"https://api.spotify.com/v1/tracks/{id}"
    
    track_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        }
    )
    
    # [!] the next code will change. currently for debugging
    match track_data.status_code:
        case 401:
            print("Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.")
            
        case 403:
            print("Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won't help here.")
        
        case 429:
            print("The app has exceeded its rate limits.")
            
        case 200:
            print('"A track" - Spotify API Docs')

        case _:
            print('Some random error I dunno')
    
    if printJson:
        print(track_data.json())
    
    return Track(track_data.json())
