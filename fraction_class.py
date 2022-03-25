import math


class Fraction:
    def __init__(self, numerator, denominator):
        try:
            if (numerator < 0) and (denominator < 0):
                top = int(numerator / math.gcd(abs(numerator), abs(denominator)))
                bottom = int(denominator / math.gcd(abs(numerator), abs(denominator)))
                self.numerator = abs(top)
                self.denominator = abs(bottom)
            else:
                self.numerator = int(numerator / math.gcd(abs(numerator), abs(denominator)))
                self.denominator = int(denominator / math.gcd(abs(numerator), abs(denominator)))
        except ValueError:
            print("Please enter an integer!")
        except ZeroDivisionError:
            print("Denominator can't be zero!")
        except:
            print("Please enter an integer!")

    def __str__(self):
        # gcd = math.gcd(abs(self.numerator), abs(self.denominator))
        #top = self.numerator/gcd
        #bottom = self.denominator/gcd
        return f"irreducible fraction: {self.numerator}/{self.denominator}"

    def __add__(self, other):
        if self.denominator == other.denominator:
            top = self.numerator + other.numerator
            return f"{top}/{self.denominator}"
        else:
            top = self.numerator * other.denominator + other.numerator * self.denominator
            bottom = self.denominator * other.denominator
            return f"{top}/{bottom}"

    def __sub__(self, other):
        if self.denominator == other.denominator:
            top = self.numerator - other.numerator
            return f"{top}/{self.denominator}"
        else:
            top = self.numerator * other.denominator - other.numerator * self.denominator
            bottom = self.denominator * other.denominator
            return f"{top}/{bottom}"

    def __mul__(self, other):
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        return f"{top}/{bottom}"

    def __div__(self, other):
        top = self.numerator * other.denominator
        bottom = self.denominator * other.numerator
        return str(top) + "/" + str(bottom)

    def compering(self, other):
        fraction1 = self.numerator/self.denominator
        fraction2 = other.numerator/other.denominator
        if fraction1 < fraction2:
            return f"{other.numerator}/{other.denominator} is bigger than {self.numerator}/{self.denominator}"
        else:
            return f"{self.numerator}/{self.denominator} is bigger than {other.numerator}/{other.denominator}"

    def getNum(self):
        return self.numerator

    def getDem(self):
        return self.denominator


def main():
    f1 = Fraction(5, -10)
    f2 = Fraction(3, 4)
    print(f1.compering(f2))
    print(f1.getDem())
    print(f1)
    print(f1+f2)
    print(f2-f1)
    print(f2*f1)
    print(f1.__div__(f2))
