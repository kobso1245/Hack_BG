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
        return self.__name

    def __eq__(self, other):
        return (self.__name == other.name() and
                self.__email == other.email() and
                self.__gender == other.gender())

    def __hash__(self):
        return hash(self.name() + self.email() +
                    self.gender())

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

    def get_pandas_list(self):
        return list(self.__pandas.keys())

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
            road_table = {panda: '' for panda in self.__pandas.keys()}
            opashka = [panda1]
            obhodeni = set()
            obhodeni.add(panda1)
            curr_panda = ""
            found = False
            while not (opashka == []):
                curr_panda = opashka.pop(0)
                if curr_panda == panda2:
                    found = True
                    break
                else:
                    for naslednik in self.__pandas[curr_panda]:
                        if naslednik not in obhodeni:
                            opashka.append(naslednik)
                            obhodeni.add(naslednik)
                            road_table[naslednik] = curr_panda
            if not found:
                return -1
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
            if lst == []:
                to_be_written.append(panda.get_pandas_info())
            else:
                to_be_written.extend([panda.get_pandas_info() + ' ' +
                                      panda_friend.get_pandas_info() for
                                      panda_friend in lst])
        out = open(fle, 'w')
        json.dump(to_be_written, out)
        out.close()

    def save_tmp(self, fle):
        to_be_written = {repr(x): [] for x in self.get_pandas().keys()}
        for panda in self.get_pandas().keys():
            lst = self.friends_of(panda)
            for panda_friend in lst:
                to_be_written[repr(panda)]. append(repr(panda_friend))
        out = open(fle, 'w')
        json.dump(to_be_written, out)
        out.close()
    
    def pandas_details(self):
        pandas = self.get_pandas_list()
        return [panda.get_pandas_info() for panda in pandas]

    def load_from(self, fle):
            in_file = open(fle)
            input_info = json.load(in_file)
            for elem in input_info:
                name = elem.split(' ')
                if len(name) == 3:
                    self.add_panda(Panda(name[0], name[1], name[2]))
                else:
                    self.make_friends(Panda(name[0], name[1], name[2]),
                                      Panda(name[3], name[4], name[5]))
            in_file.close()

    def show_pandas(self):
        pandas = self.pandas_details()
        for panda in pandas:
            print(panda)

if __name__ == '__main__':
    panda_ntw = PandaSocialNetwork()
    panda_ntw.load_from('dada1.json')
    panda_ntw.add_panda(Panda("Test", "test@pandamail.com", "male"))
    panda_ntw.show_pandas()
    tst = Panda("dadadada", "te@gmail.com", "male")
    print(tst.name())



