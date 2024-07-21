# Hi

import core.access_token as access_token
import core.artist as artist
import core.album as album
import core.track as track


if __name__ == '__main__':
    AccessToken = access_token.AccessTokenClass()
    AccessToken.Generate()

    KORN = artist.GetArtistById("3RNrq3jvMZxD9ZyoOZbQOD", AccessToken)
    KORN_BEST = artist.GetArtistTopTracks("3RNrq3jvMZxD9ZyoOZbQOD", AccessToken)
    KORN_TRACKS = track.GetTracksByDict(KORN_BEST, AccessToken)

    print(KORN_TRACKS[0])

    track.SaveTracksToProfile(KORN_TRACKS, AccessToken)

# Rearrange as you wish.