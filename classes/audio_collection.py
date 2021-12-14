class Track:

    def __init__(self, name, duration):
        self.__name = name
        self.__duration = int(duration)

    def get_name(self):
        return self.__name

    def get_duration(self):
        return self.__duration

    def show(self):
        print(f"<{self.__name}-{self.__duration} мин>")


class Album:

    def __init__(self, name, author, tracks):
        self.__name = name
        self.__author = author
        self.__tracks = tracks.copy()

    def show(self):
        print(f'"{self.__author}": {self.__name}')

    def get_tracks(self):
        self.show()
        for track in self.__tracks:
            track.show()
        print()

    def add_track(self, track):
        self.__tracks.append(track)

    def get_duration(self):
        self.show()
        duration = 0
        for track in self.__tracks:
            duration += track.get_duration()
        print(f"Длительность всего альбома: {duration} мин\n")


audio_collection = [
    Album("Shockwave", "Feint", [Track("Snake Eyes", 4), Track("Fall Away", 5), Track("Shatter", 3)]),
    Album("Fort Boyard", "Gilead", [Track("Fort Boyard", 5), Track("Medieval Groove", 4), Track("Komartanz", 4)])
]

for album in audio_collection:
    album.get_duration()
    # album.get_tracks()
