from copy import deepcopy


class Bill:

    def __init__(self, ammount):
        self.ammount = ammount

    def __str__(self):
        return "A {}$ bill".format(self.ammount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.ammount

    def __eq__(self, other):
        return self.ammount == other.ammount

    def __hash__(self):
        return hash(self.ammount)

    def toDict(self):
        return {self.ammount: 1}


class BillBatch:

    def __init__(self, bills):
        self.bills = deepcopy(bills)

    def total(self):
        return sum([int(bill) for bill in self.bills])

    def toDict(self):
        return {int(elem): self.bills.count(elem) for elem in self.bills}

    def __getitem__(self, index):
        return self.bills[index]

    def __len__(self):
        return len(self.bills)

    def __int__(self):
        return self.total()


class CashDesk:

    def __init__(self):
        self.lst = {}

    def take_money(self, money):
        converted = money.toDict()
        for key in converted.keys():
            if int(key) in self.lst.keys():
                self.lst[key] += converted[key]
            else:
                self.lst[key] = converted[key]

    def total(self):
        out = 0
        for key in self.lst.keys():
            out += (int(key) * self.lst[key])
        return out

    def inspect(self):
        to_pairs = sorted([(key, self.lst[key]) for key in self.lst.keys()])
        for elem in to_pairs:
            print("{}$ bills  - {}".format(elem[0], elem[1]))
