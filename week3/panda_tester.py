import unittest
import re
from panda_network import Panda, PandaSocialNetwork


class PandaClassTester(unittest.TestCase):
    def test_the_class_for_existence(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertTrue(isinstance(panda, Panda))

    def test_does_func_name_work(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(panda.name(), 'Ivo')

    def test_does_the_email_func_work_shouldnt(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertNotEqual(panda.email(), 'Ivo')

    def test_does_the_email_func_work_should(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(panda.email(), 'ivo@pandamail.com')

    def test_gender_work_should(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(panda.gender(), "male")

    def test_gender_work_shouldnt(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertNotEqual(panda.gender(), "mae")

    def test_isMale_true(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertTrue(panda.isMale())

    def test_isMale_false(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertFalse(panda.isFemale())

    def test_str_should(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertEqual(str(panda), 'Ivo')

    def test_str_shouldnt(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertNotEqual(str(panda), 'ivo')

    def test_eq_should(self):
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        notPanda = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertTrue(panda == notPanda)

class TestPandaNetwork(unittest.TestCase):
    def test_dictionary_retrieval_function_should(self):
        panda_ntw = PandaSocialNetwork()
        self.assertEqual(panda_ntw.pandas(), {})

    def test_dictionarry_after_adding_panda(self):
        panda_ntw = PandaSocialNetwork()
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_ntw.add_panda(panda)
        self.assertEqual(panda_ntw.pandas(), {panda: []})

    def test_adding_same_panda_again(self):
        panda_ntw = PandaSocialNetwork()
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_ntw.add_panda(panda)
        with self.assertRaises(ValueError):
            panda_ntw.add_panda(panda)

    def testing_if_panda_is_in_the_network_should(self):
        panda_ntw = PandaSocialNetwork()
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_ntw.add_panda(panda)
        self.assertTrue(panda_ntw.has_panda(panda))

    def testing_if_adds_panda_should(self):
        panda_ntw = PandaSocialNetwork()
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_ntw.add_panda(panda)
        panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
        panda_ntw.make_friends(panda, panda2)
        with self.assertRaises(ValueError):
            panda_ntw.make_friends(panda2, panda)

    def testing_if_are_friends_func_works_should(self):
        panda_ntw = PandaSocialNetwork()
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_ntw.add_panda(panda)
        panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
        panda_ntw.make_friends(panda, panda2)
        self.assertTrue(panda_ntw.are_friends(panda, panda2))

    def testing_if_friends_of_func_should(self):
        panda_ntw = PandaSocialNetwork()
        panda = Panda("Ivo", "ivo@pandamail.com", "male")
        panda_ntw.add_panda(panda)
        panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
        panda_ntw.make_friends(panda, panda2)
        self.assertEqual(panda_ntw.friends_of(panda), [panda2])
if __name__ == '__main__':
    unittest.main()