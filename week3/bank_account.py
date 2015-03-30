
class BankAccount:
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError
        if not (type(name) is str and type(currency) is str):
            raise TypeError
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = []
        self.__history.append("Account was created")

    def __int__(self):
        self.__history.append("__int__ check -> {}{}".format(self.__balance,
                                                             self.__currency))
        return self.__balance

    def deposit(self, amount):
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if amount <= 0:
            raise ValueError
        self.__balance += amount
        self.__history.append("Deposited {}{}".format(amount,
                                                      self.__currency))
        return True

    def balance(self):
        self.__history.append("balance check -> {}{}".format(
                                                             self.__balance,
                                                             self.__currency))
        return int(self)

    def currency(self):
        return self.__currency

    def incr_balance(self, amount):
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if amount <= 0:
            raise ValueError
        self.__balance += amount

    def transfer_to(self, account, amount):
        if self.__currency != account.currency():
            return False
        if not(type(account) is BankAccount):
            raise TypeError
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if self.__balance < amount:
            return False
        account.incr_balance(amount)
        self.__balance -= amount
        return True

    def withdraw(self, amount):
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if amount <= self.__balance:
            self.__balance -= amount
            self.__history.append("{}{} withdrawn".format(amount,
                                                          self.__currency))
            return True
        else:
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(
                self.__name, self.__balance, self.__currency)

    def history(self):
        return self.__history

if __name__ == '__main__':
    account = BankAccount("Rado", 0, "$")
    print(account)
    account.deposit(1000)
    print(account.balance())
    print(str(account))
    print(account.history())
    account.withdraw(500)
    print(account.balance())
    print(account.history())
