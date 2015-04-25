import requests
import json
from graph import *

STANDARD_FOLLOWERS = "https://api.github.com/users/{}/followers?client_id=676230d310fd2331b65b&client_secret=bd0f5b2cbae63efd234b230c5c31d7cb271da8de"
STANDARD_FOLLOWING = "https://api.github.com/users/{}/following?client_id=676230d310fd2331b65b&client_secret=bd0f5b2cbae63efd234b230c5c31d7cb271da8de"

class SocialNetwork:
    def __init__(self, name):
        self.__name = name
        self.__graph = DirectedGraph()
        self.__visited = set()

    def get_lab(self):
        req = requests.get("https://api.github.com/users/kobso1245?client_id=676230d310fd2331b65b&client_secret=bd0f5b2cbae63efd234b230c5c31d7cb271da8de").json()
        return req

    def add_level(self):
        pass

    def get_network_for(self, name):
        dct = {}
        dct['following'] = []
        dct['followers'] = []

        req_followers = requests.get(STANDARD_FOLLOWERS.format(name)).json()
        req_following = requests.get(STANDARD_FOLLOWING.format(name)).json()

        for follower in req_followers:
            dct['followers'].append(follower["login"])

        for follower in req_following:
            dct["following"].append(follower['login'])
        return dct

    def make_graph(self, start_name, level):
        self._dfs_level(level, start_name)

    def _dfs_level(self, level, name):
        if level == 0:
            return
        
        tple = self.get_network_for(name)
        followers = tple["followers"]
        following = tple["following"]

        for follower in followers:
            if follower not in self.__visited:
                self.__visited.add(follower)
                self.__graph.add_edge(follower, name)
                self._dfs_level(level-1, follower)

        for follow in following:
            if follow not in self.__visited:
                self.__visited.add(follow)
                self.__graph.add_edge(name, follow)
                self._dfs_level(level-1, follow)

if __name__ == "__main__":
    soc = SocialNetwork("da")
    print(json.dumps(soc.get_network_for("kobso1245"), indent=4))
    #soc.make_graph("kobso1245", 2)
