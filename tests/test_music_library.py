from lib.MusicLibrary import MusicLibrary
from unittest.mock import Mock
def test_search_matches():
    music_library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    music_library.add (fake_matching)
    fake_notmatching = Mock()
    fake_notmatching.matches.return_value = False
    music_library.add (fake_notmatching)
    assert music_library.search("laptop") == [fake_matching]


class FakeMatchingTrack():
    def matches (self, keyword):
        return True
    
class FakeNotmatchingTrack():
    def matches (self, keyword):
        return False