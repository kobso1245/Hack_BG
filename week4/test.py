import json


class A:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
class B:
    def __init__(self, name):
        self.name = name
        self.other = []

    def add(self, other):
        self.other.append(other)

if __name__=="__main__":
    a = A("test")
    b = B("B")
    c = A("A")
    b.add(a)
    b.add(c)
    print(b.__dict__)
    fl = open("Test.json", "w")
    json.dump(b.__dict__, fl, indent=4)
