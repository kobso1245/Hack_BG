class Fraction:

    def __init__(self, numerator, denominator):
        den = 1
        if numerator != 0:
            den = gcd(numerator, denominator)
        if den == 1:
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = (numerator // den)
            self.denominator = (denominator // den)

    def __str__(self):
        if self.numerator == self.denominator or self.numerator == 0:
            return str(self.numerator)
        else:
            return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator -
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)


def gcd(a, b):
    if a > b:
        return gcd(a - b, b)
    if a < b:
        return gcd(a, b - a)
    if a == b:
        return a
