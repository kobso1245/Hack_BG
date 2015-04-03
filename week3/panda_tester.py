import unittest
from panda_network import Panda, PandaSocialNetwork
from panda_network import PandasAlreadyFriends, PandaAlreadyThere


class PandaClassTester(unittest.TestCase):

    def setUp(self):
        self.panda = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_the_class_for_existence(self):
        self.assertTrue(isinstance(self.panda, Panda))

    def test_does_func_name_work(self):
        self.assertEqual(self.panda.name(), 'Ivo')

    def test_does_the_email_func_work_shouldnt(self):
        self.assertNotEqual(self.panda.email(), 'Ivo')

    def test_does_the_email_func_work_should(self):
        self.assertEqual(self.panda.email(), 'ivo@pandamail.com')

    def test_gender_work_should(self):
        self.assertEqual(self.panda.gender(), "male")

    def test_gender_work_shouldnt(self):
        self.assertNotEqual(self.panda.gender(), "mae")

    def test_isMale_true(self):
        self.assertTrue(self.panda.isMale())

    def test_isMale_false(self):
        self.assertFalse(self.panda.isFemale())

    def test_str_should(self):
        self.assertEqual(str(self.panda), 'Ivo')

    def test_str_shouldnt(self):
        self.assertNotEqual(str(self.panda), 'ivo')

    def test_eq_should(self):
        notPanda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertTrue(self.panda == notPanda)

    def test_get_panda(self):
        self.assertEqual(self.panda.get_pandas_info(), "Ivo ivo@pandamail.com male")


class TestPandaNetwork(unittest.TestCase):

    def setUp(self):
        self.panda = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_dictionary_retrieval_function_should(self):
        panda_ntw = PandaSocialNetwork()
        self.assertEqual(panda_ntw.pandas(), {})

    def test_dictionary_after_adding_panda(self):
        panda_ntw = PandaSocialNetwork()
        panda_ntw.add_panda(self.panda)
        self.assertEqual(panda_ntw.pandas(), {self.panda: []})

    def test_adding_same_panda_again(self):
        panda_ntw = PandaSocialNetwork()
        panda_ntw.add_panda(self.panda)
        with self.assertRaises(PandaAlreadyThere):
            panda_ntw.add_panda(self.panda)

    def testing_if_panda_is_in_the_network_should(self):
        panda_ntw = PandaSocialNetwork()
        panda_ntw.add_panda(self.panda)
        self.assertTrue(panda_ntw.has_panda(self.panda))

    def testing_if_adds_panda_should(self):
        panda_ntw = PandaSocialNetwork()
        panda_ntw.add_panda(self.panda)
        panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
        panda_ntw.make_friends(self.panda, panda2)
        with self.assertRaises(PandasAlreadyFriends):
            panda_ntw.make_friends(panda2, self.panda)

    def testing_if_are_friends_func_works_should(self):
        panda_ntw = PandaSocialNetwork()
        panda_ntw.add_panda(self.panda)
        panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
        panda_ntw.make_friends(self.panda, panda2)
        self.assertTrue(panda_ntw.are_friends(self.panda, panda2))

    def testing_if_friends_of_func_should(self):
        panda_ntw = PandaSocialNetwork()
        panda_ntw.add_panda(self.panda)
        with self.assertRaises(PandaAlreadyThere):
            panda_ntw.add_panda(self.panda)
        panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
        panda_ntw.make_friends(self.panda, panda2)
        self.assertEqual(panda_ntw.friends_of(self.panda), [panda2])
if __name__ == '__main__':
    unittest.main()
