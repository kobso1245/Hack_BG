MSG = {'cr8': "Account was created",
       '__int__': "__int__ check -> {}{}",
       'dpstd': "Deposited {}{}",
       'blnchk': "balance check -> {}{}",
       'trnsto': "Transfer to {} for {}{}",
       'trnsfr': "Transfer from {} for {}{}",
       'wtdrsc': "{}{} withdrawn",
       'wtdrfl': "Withdraw for {}{} failed",
       '__str__': "Bank account for {} with balance of {}{}"}


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
        self.__history.append(MSG['cr8'])

    def __int__(self):
        self.__history.append(MSG['__int__'].format(self.__balance,
                                                    self.__currency))
        return self.__balance

    def deposit(self, amount):
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if amount <= 0:
            raise ValueError
        self.__balance += amount
        self.__history.append(MSG['dpstd'].format(amount,
                                                  self.__currency))
        return True

    def balance(self):
        self.__history.append(MSG['blnchk'].format(
                                                   self.__balance,
                                                   self.__currency))
        return self.__balance

    def currency(self):
        return self.__currency

    def name(self):
        return self.__name

    def incr_balance(self, amount):
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if amount <= 0:
            raise ValueError
        self.__balance += amount

    def set_history(self, message):
        self.__history.append(message)

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
        self.__history.append(MSG['trnsto'].format(account.name(), amount,
                                                   self.__currency))
        account.set_history(MSG['trnsfr'].format(self.__name, amount,
                                                 self.__currency))
        return True

    def withdraw(self, amount):
        if not(type(amount) is int or type(amount) is float):
            raise TypeError
        if amount <= self.__balance:
            self.__balance -= amount
            self.__history.append(MSG['wtdrsc'].format(amount,
                                                       self.__currency))
            return True
        else:
            self.__history.append(MSG['wtdrfl'].format(amount,
                                                       self.__currency))
            return False

    def __str__(self):
        return MSG['__str__'].format(
                self.__name, self.__balance, self.__currency)

    def history(self):
        return self.__history
