# Track class and api

# pylint: disable=W0622
# pylint: disable=E0401

import requests
from typing import Any


class Track:
    def __init__(self, spotify_track: dict, auth):
        self._track = spotify_track
        self._audio_features = GetTrackAudioFeaturesByID(self.ObtainParameter("id"), auth)

    def ObtainParameter(self, parameter: str, retrieve_from_track: bool = True) -> Any:
        """
        Retrieve a parameter.

        This should only be used in case there's no equal property.

        :param parameter: The parameter to retrive
        :param retrieve_from_track: Whether to retreieve the param from the track or from the audio features. Defaults to True (track).

        :return: The parameter
        """

        if retrieve_from_track:
            return self._track[parameter]

        return self._audio_features[parameter]

    @property
    def trackId(self) -> str:
        """
        Return the ID of the track.

        :return: Track ID
        """

        return self.ObtainParameter('id')

    @property
    def albumId(self) -> str:
        """
        Return the ID of the album where this track is.

        :return: Album ID
        """
        
        return self.ObtainParameter("album")["id"] # [i] this can be used to get the album
    
    @property
    def artistIds(self) -> list[str]:
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
    def trackDuration(self) -> int:
        """
        Return the duration of the track in miliseconds.
        
        :return: Duration of the track (ms)
        """
        
        return self.ObtainParameter('duration_ms')
    
    @property
    def isExplicit(self) -> bool:
        """
        Is the song explicit (a.k.a. contains slurs/swearing)?
        
        :return: Boolean that represents if the song is explicit
        """
        
        # [*] explicit songs eh eh :smiling_imp:
        return self.ObtainParameter('explicit')

    @property
    def isPlayable(self) -> bool:
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
    def trackName(self) -> str:
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
    def previewUrl(self) -> str | None:
        """
        Link to a 30 sec preview of the song.
        
        NOTE TO THE DEVS: We can use this later by making a request
        and getting the bytes (response.content).
        
        If not available, will return None.
        
        :return: Link to song preview (None if none available)
        """
        
        return self.ObtainParameter('preview_url')

    @property
    def danceability(self) -> float:
        """
        How danceable is the song?

        :return: Track's danceability
        """

        return self.ObtainParameter('danceability', False)

    @property
    def energy(self) -> float:
        """
        How energetic is the song?

        :return: Track's energy
        """

        # this is particularly high on metal musics xD

        return self.ObtainParameter('energy', False)

    @property
    def rankedInstrumentalness(self) -> str:
        """
        Using Spotify's API, rank how instrumental the song is.

        Sounds like "ooh" and "aaah" are considered instrumental.

        If you want the value and not the label, use `instrumentalness`.

        :return: Label for Instrumentalness
        """

        instrumentalness_ranked = {
            0.0: "Not Instrumental",
            0.1: "Most Likely Not Instrumental",
            0.2: "Likely Not Instrumental",
            0.5: "Possibly Instrumental",
            0.6: "Likely Instrumental",
            0.9: "Most Likely Instrumental",
            1.0: "Instrumental"
        }

        rounded_instrumentalness = round(self.ObtainParameter('instrumentalness', False), 1)

        if rounded_instrumentalness in instrumentalness_ranked:
            return instrumentalness_ranked[rounded_instrumentalness]

        if rounded_instrumentalness < 0.5:
            return instrumentalness_ranked[0.2]

        if rounded_instrumentalness > 0.5:
            return instrumentalness_ranked[0.6]

    @property
    def instrumentalness(self) -> float:
        """
        Using Spotify's API, get a value that represents how instrumental the song is.

        Sounds like "ooh" and "aaah" are considered instrumental.

        :return: instrumentalness as a float
        """

        return self.ObtainParameter('instrumentalness', False)

    @property
    def rankedLiveness(self) -> str:
        """
        Using Spotify's API, rank if the song is likely to be recorded live.

        If you want the value and not the label, use `liveness`.

        :return: Label rank for liveness
        """

        liveness_ranked = { # in this one, the safety mark is not 0.5 but 0.8
            0.0: "Recorded in Studio",
            0.2: "Most Likely Recorded in Studio",
            0.5: "Likely Recorded in Studio",
            0.7: "Possibly Recorded in Studio",
            0.8: "Likely Played Live",
            0.9: "Most Likely Played Live",
            1.0: "Played Live"
        }

        rounded_liveness = round(self.ObtainParameter('liveness', False), 1)

        if rounded_liveness in liveness_ranked:
            return liveness_ranked[rounded_liveness]

        if rounded_liveness == 0.1:
            return liveness_ranked[0.0]

        if rounded_liveness > 0.5:
            return liveness_ranked[0.2]

        if rounded_liveness == 0.6:
            return liveness_ranked[0.5]

    @property
    def liveness(self) -> float:
        """
        Using Spotify's API, get a value that represents how likely the song is to be played live.

        :return: liveness as a float
        """

        return self.ObtainParameter('liveness', False)

    def __str__(self) -> str:
        return str(self._track)

    def __getitem__(self, value: str) -> Any:
        return self.ObtainParameter(value)
    
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
        },
        timeout=1
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
    
    return Track(track_data.json(), auth)


def GetTrackAudioFeaturesByID(id: str, auth, printJson: bool = False) -> dict:
    """
    Retrieve song and return Track object.

    :param id: Song id.
    :param auth: of type AccessTokenClass.
    :param printJson: Print the JSON data. Defaults to False.
    :return: Track object.
    """

    base_url = f"https://api.spotify.com/v1/audio-features/{id}"

    track_audio_data = requests.get(
        base_url,
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        },
        timeout=1 # always add a timeout boys...
    )

    if printJson:
        print(track_audio_data.json())

    return track_audio_data.json()


def SaveTracksToProfile(tracks: list[Track], auth):
    """
    Save tracks to the library.

    :param tracks: Tracks to save
    :param auth: Token represented by the class AccessTokenClass
    :return:
    """

    base_url = "https://api.spotify.com/v1/me/tracks"

    track_ids = [track.track_id for track in tracks]

    track_data = requests.put(
        base_url,
        json={
            'ids': track_ids
        },
        headers={
            "Authorization": f"{auth.token_type} {auth.access_token}"
        },
        timeout=1
    )

    # [!] the next code will change. currently for debugging
    match track_data.status_code:
        case 401:
            print(
                "Bad or expired token. This can happen if the user revoked a token or the access token has expired. You should re-authenticate the user.")

        case 403:
            print(
                "Bad OAuth request (wrong consumer key, bad nonce, expired timestamp...). Unfortunately, re-authenticating the user won't help here.")

        case 429:
            print("The app has exceeded its rate limits.")

        case 200:
            print('Successssss!')

        case _:
            print('Some random error I dunno')


def GetTracksByDict(track_objects: list[dict], auth) -> list[Track]:
    """
    Easy way to convert a list of tracks in form of dicts to a list of tracks in form of Track class.

    :param track_objects: list of tracks in form of dicts
    :param auth: AccessTokenClass
    :return: list of tracks in form of instances of Track class
    """

    return [Track(track_object, auth) for track_object in track_objects]

