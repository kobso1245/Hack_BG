import re
import json


class PandaException(Exception):
    pass


class PandaAlreadyThere(PandaException):

    def __init__(self, value='PandaAlreadyThere'):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PandasAlreadyFriends(PandaException):

    def __init__(self, value='PandasAlreadyFriends'):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Panda:

    def __init__(self, name, email, gender):
        if not re.match(r'\w[\w\.-]*@\w[\w\.-]+\.\w+', email):
            print("Wrong email!")
            return
        if not (gender.lower() == 'male' or gender.lower() == 'female'):
            print("Wrong gender!")
            return
        self.__name = name
        self.__email = email
        self.__gender = gender.lower()

    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == 'male'

    def isFemale(self):
        return self.__gender == 'female'

    def __str__(self):
        return self.__name

    def __repr__(self):
        return "Panda({}, {}, {})".format(self.__name, self.__email, self.__gender)

    def __eq__(self, other):
        return (self.__name == other.name() and
                self.__email == other.email() and
                self.__gender == other.gender())

    def __hash__(self):
        return hash(self.__name + self.__email +
                    self.__gender)

    def get_pandas_info(self):
        return "{} {} {}".format(self.__name, self.__email, self.__gender)


class PandaSocialNetwork:

    def __init__(self):
        self.__pandas = {}

    def pandas(self):
        return self.__pandas

    def add_panda(self, panda):
        if panda in self.__pandas:
            raise PandaAlreadyThere
        self.__pandas[panda] = []

    def has_panda(self, panda):
        return panda in self.__pandas

    def get_pandas(self):
        return self.__pandas

    def make_friends(self, other1, other2):
        if(other2 in self.__pandas.keys() and
           other1 in self.__pandas[other2]):
                return
        if other1 in self.__pandas.keys():
            self.__pandas[other1].append(other2)
        else:
            self.__pandas[other1] = [other2]
        if other2 in self.__pandas.keys():
            self.__pandas[other2].append(other1)
        else:
            self.__pandas[other2] = [other1]

    def are_friends(self, other1, other2):
        return other2 in self.__pandas[other1]

    def friends_of(self, panda):
        if panda not in self.__pandas.keys():
            return False
        else:
            return self.__pandas[panda]

    def connection_level(self, panda1, panda2):
        if not (panda1 in self.__pandas.keys() and
                panda2 in self.__pandas.keys()):
            return False
        elif panda1 in self.__pandas[panda2]:
            return 1
        else:
            road_table = {}
            for panda in self.__pandas.keys():
                road_table[panda] = ""

            obhodeni = [panda1]
            curr_panda = ""
            while obhodeni != []:
                curr_panda = obhodeni.pop(0)
                if curr_panda == panda2:
                    break
                else:
                    for naslednik in self.__pandas[curr_panda]:
                        if naslednik not in obhodeni:
                            obhodeni.append(naslednik)
                            if type(road_table[naslednik]) is str:
                                road_table[naslednik] = curr_panda
            road_len = 0
            start = panda2
            while start != panda1:
                road_len += 1
                start = road_table[start]
            return road_len

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != 0

    def how_many_gender_in_network(self, level, panda, gender):
        cnt = 0
        for next_panda in self.__pandas.keys():
            if next_panda != panda:
                if(self.connection_level(panda, next_panda) == level and
                   next_panda.gender() == gender):
                    cnt += 1
        return cnt

    def save_to(self, fle):
        to_be_written = []
        for panda in self.get_pandas().keys():
            lst = self.friends_of(panda)
            for panda_friend in lst:
                to_be_written.append(panda.get_pandas_info() + ' ' +
                                     panda_friend.get_pandas_info())
        out = open(fle, 'w')
        json.dump(to_be_written, out)
        out.close()

    def save_tmp(self, fle):
        to_be_written ={repr(x): [] for x in self.get_pandas().keys() }
        for panda in self.get_pandas().keys():
            lst = self.friends_of(panda)
            for panda_friend in lst:
                to_be_written[repr(panda)]. append(repr(panda_friend))
        out = open(fle, 'w')
        json.dump(to_be_written, out)
        out.close()

    def load_from(self, fle):
            in_file = open(fle)
            input_info = json.load(in_file)
            for elem in input_info:
                name = elem.split(' ')
                self.make_friends(Panda(name[0], name[1], name[2]), Panda(name[3],
                                  name[4], name[5]))
            in_file.close()


if __name__ == '__main__':
    panda_ntw = PandaSocialNetwork()
    panda = Panda("Ivo", "ivo@pandamail.com", "male")
    panda2 = Panda("Gosho", "gosho@pandamail.com", "male")
    panda3 = Panda("Toshko", "gosho@pandamail.com", "male")
    panda4 = Panda("Q", "q@pandamail.com", "male")
    panda5 = Panda("L", "l@pandamail.com", "male")
    panda6 = Panda("R", "r@pandamail.com", "male")
    panda7 = Panda("M", "r@pandamail.com", "male")
    panda_ntw.make_friends(panda, panda2)
    panda_ntw.make_friends(panda, panda4)
    panda_ntw.make_friends(panda2, panda4)
    panda_ntw.make_friends(panda2, panda3)
    panda_ntw.make_friends(panda4, panda5)
    panda_ntw.make_friends(panda5, panda6)
    panda_ntw.make_friends(panda3, panda6)
    panda_ntw.save_tmp("dada1.json")
