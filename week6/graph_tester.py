import unittest
from graph import *

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.gr = DirectedGraph()
        self.gr.add_edge("A", "B")
        self.gr.add_edge("A", "E")
        self.gr.add_edge("B", "C")
        self.gr.add_edge("C", "D")
        self.gr.add_edge("D", "B")
        self.gr.add_edge("E", "D")
        self.gr.add_edge("K", "D")

    def test_has_road_true(self):
        self.assertTrue(self.gr.has_path_between("A", "D"))
    def test_has_road_false(self):
        self.assertFalse(self.gr.has_path_between("A", "K"))

if __name__ == "__main__":
    unittest.main()

