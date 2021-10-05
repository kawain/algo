from abc import ABC, abstractmethod


class ICalc(ABC):
    @abstractmethod
    def calc(self, a, b):
        pass


class Add(ICalc):
    def calc(self, a, b):
        return a + b


class Sub(ICalc):
    def calc(self, a, b):
        return a - b


class Mul(ICalc):
    def calc(self, a, b):
        return a * b


class Div(ICalc):
    def calc(self, a, b):
        return a / b


class Calc:
    @classmethod
    def calc(cls, obj, a, b):
        return obj.calc(a, b)


print(Calc.calc(Add(), 9, 3))
print(Calc.calc(Sub(), 9, 3))
print(Calc.calc(Mul(), 9, 3))
print(Calc.calc(Div(), 9, 3))
