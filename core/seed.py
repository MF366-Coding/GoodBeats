from typing import Any


class Seed:
    def __init__(self, *values: Any, delimiter: str = ','):
        if len(delimiter) != 1:
            raise ValueError('the delimiter must be a single character')

        self._char = delimiter
        self._values = list(*values) # force it to be a list as it's mutable therefore easier to work with later on

    def ToString(self) -> str:
        return str(self)

    def ToTuple(self) -> tuple[Any, ...]:
        return tuple(self._values.copy())

    def Hash(self) -> int:
        return hash(self._values)

    ToInt = Hash

    def Mutate(self, operation: str, *args: Any) -> str | None | Any:
        match operation:
            case 'pop':
                value = self._values.pop(*args)

            case 'remove':
                value = self._values.remove(*args)

            case 'insert' | 'append':
                value = self._values.insert(-1 if len(args) == 1 else args[0], args[1])

            case _:
                value = 'Invalid Mutation'

        return value

    def __str__(self) -> str:
        return self._char.join(self._values)


class ArtistSeed(Seed):
    def __init__(self, artists: tuple):
        super().__init__(*(i.artistId for i in artists))

    def Mutate(self, *_) -> str | None | Any:
        raise Exception('cannot mutate an artist seed')


class GenreSeed(Seed):
    def __init__(self, genres: tuple[str, ...]):
        super().__init__(*genres)

    def Mutate(self, *_) -> str | None | Any:
        raise Exception('cannot mutate a genre seed')


class TrackSeed(Seed):
    def __init__(self, tracks: tuple):
        super().__init__(*(i.trackId for i in tracks))

    def Mutate(self, *_) -> str | None | Any:
        raise Exception('cannot mutate a track seed')