from lib.Track import Track

def test_matches_full_title():
    track = Track ("title1", "artist1")
    assert track.matches("title1") == True
    
    
def test_not_matches():
    track = Track ("title1", "artist1")
    assert track.matches("toto") == False