from lib.MusicLibrary import MusicLibrary
from lib.Track import Track

def test_add_library_search_matches():
    music_library = MusicLibrary()
    track_1 = Track("my title 1", "my artist 1")
    track_2 = Track ("my title 2","my artist 2")
    music_library.add (track_1)
    music_library.add (track_2)
    assert music_library.tracks == [track_1, track_2]
        
def test_search_matches():
    music_library = MusicLibrary()
    track_1 = Track("my title 1", "my artist 1")
    track_2 = Track ("my title 2","my artist 2")
    music_library.add (track_1)
    music_library.add (track_2)
    assert music_library.search("my title 1") == [track_1]

