import requests
import json
from graph import *

STANDARD_FOLLOWERS = "htps://api.github.com/users/{}/followers?page={}&client_id={}&client_secret={}"
STANDARD_FOLLOWING = "https://api.github.com/users/{}/following?page={}&client_id={}&client_secret={}"


def get_id_and_secret(filename):
    jsoned = json.loads(open(filename).read())
    return (jsoned['client_id'], jsoned['client_secret'])

class SocialNetwork:
    def __init__(self, name):
        self.__name = name
        self.__graph = DirectedGraph()
        self.__visited = set()

    def get_lab(self):
        id_sec = get_id_and_secret("client.json")
        req = requests.get("https://api.github.com/users/kobso1245?client_id={}&client_secret={}".format(id_sec[0], id_sec[1])).json()
        return req

    def add_level(self):
        pass

    def get_follow(self, name):
        jsoned = "d"
        cnt = 1
        dct = {}
        dct['followers'] = []
        dct['following'] = []
        id_sec = get_id_and_secret("client.json")
        while jsoned != []:
            jsoned = requests.get(STANDARD_FOLLOWERS.format(name, cnt, id_sec[0],
                                                                   id_sec[1])).json()
            cnt += 1
            for follower in jsoned:
                dct['followers'].append(follower['login'])

        jsoned = "d"
        cnt = 1
        while jsoned != []:
            jsoned = requests.get(STANDARD_FOLLOWING.format(name, cnt, id_sec[0],
                                                                   id_sec[1])).json()
            
            cnt += 1
            for follower in jsoned:
                dct['following'].append(follower['login'])

        return dct


    def get_network_for(self, name):
        return self.get_follow(name)

    def make_graph(self, start_name, level):
        self._dfs_level(level, start_name)

    def _dfs_level(self, level, name):
        
        if level == 0:
            return

        follow = self.get_network_for(name)
        followers = follow['followers']
        following = follow['following']

        self.__visited.add(name)

        for follower in followers:
            self.__graph.add_edge(follower, name)
            if follower not in self.__visited:
                self._dfs_level(level - 1, follower)

        for follower in following:
            self.__graph.add_edge(name, follower)
            if follower not in self.__visited:
                self._dfs_level(level - 1, follower)

