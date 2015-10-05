class DirectedGraph:

    def __init__(self):
        self.__nodes = {}

    def get_nodes(self):
        return self.__nodes

    def add_edge(self, start, end):
        if start in self.__nodes.keys():
            if end not in self.__nodes[start]:
                self.__nodes[start].append(end)
            else:
                return
        else:
            self.__nodes[start] = [end]

    def get_neighbours(self, node):
        return self.__nodes[node]

    def _dfs(self, curr_node, passed_nodes, end):
        if curr_node == end:
            return True
        if self.__nodes[curr_node] == []:
            return

        for naslednik in self.__nodes[curr_node]:
            if naslednik not in passed_nodes:
                passed_nodes.add(naslednik)
                return self._dfs(naslednik, passed_nodes, end)

    def has_path_between(self, start, end):
        ks = self.__nodes.keys()
        if start not in ks and end not in ks:
            return False
        passed = set()
        found = self._dfs(start, passed, end)

        if found:
            return True
        else:
            return False
