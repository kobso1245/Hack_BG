import unittest
from mus_lib import Song, Playlist

class SongTester(unittest.TestCase):
    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44", path="")
        self.song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44", path="")
    def test___str__return(self):
        elem = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(str(self.song), elem)

    def test__str_return_not_work(self):
        elem = "Test - Odin from The Sons of Odin - 3:44"
        self.assertNotEqual(str(self.song), elem)
    
    def test_if___eq__works(self):
        self.assertTrue(self.song == self.song1)

    def test__hash__works(self):
        dct = {}
        dct[self.song] = self.song1
    
    def test_length_seconds(self):
        self.assertEqual(self.song.length(seconds=True), 224)
class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.playlst = Playlist(name="Code")
        self.song1 = Song(title="New odin", artist="Manowar", album="The Sons of Odin", length="1")
        self.song2 = Song(title="New odin temple", artist="Manowar", album="The Sons of Odin5", length="2:50")
        self.song3 = Song(title="New odin tester", artist="Manowar", album="The Sons of Odin4", length="3:20")
        self.song4 = Song(title="New odin odin", artist="Manowar", album="The Sons of Odin2", length="3:30")
        self.song5 = Song(title="New odin much odin", artist="Manowar", album="The Sons of Odin3", length="3:25")
        
    def test_add_song(self):
        self.playlst.add_song(self.song)
        self.assertTrue(self.song in self.playlst.show_songs())

    def test_total_length(self):
        self.playlst.add_song(self.song1)
        self.playlst.add_song(self.song)
        self.assertEqual(self.playlst.total_length(), 225)

    def test_artists(self):
        self.playlst.add_song(self.song1)
        self.playlst.add_song(self.song)
        self.assertEqual(self.playlst.artists(), {self.song.artist(): 2})

    def test_shuffle(self):
        playlist1 = Playlist(name="Coding", shuffle=True)
        playlist1.add_song(self.song)
        playlist1.add_song(self.song1)
        playlist1.add_song(self.song2)
        playlist1.add_song(self.song3)
        playlist1.add_song(self.song4)
        playlist1.add_song(self.song5)
        for i in range(6):
            playlist1.next_song()
        self.assertEqual(len(playlist1.get_passed()), 6)

    def test_repeat(self):
        playlist1 = Playlist(name="Coding", repeat=True)
        playlist1.add_song(self.song)
        playlist1.add_song(self.song1)
        playlist1.add_song(self.song2)
        playlist1.add_song(self.song3)
        playlist1.add_song(self.song4)
        playlist1.add_song(self.song5)
        for i in range(7):
            playlist1.next_song()

    def test_repeat_fails(self):
        playlist1 = Playlist(name="Coding", repeat=False)
        playlist1.add_song(self.song)
        playlist1.add_song(self.song1)
        playlist1.add_song(self.song2)
        playlist1.add_song(self.song3)
        playlist1.add_song(self.song4)
        playlist1.add_song(self.song5)
        for i in range(6):
            playlist1.next_song()
        with self.assertRaises(Exception):
            playlist1.next_song()



if __name__=="__main__":
    unittest.main()
