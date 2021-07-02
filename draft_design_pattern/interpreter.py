# https://9cubed.info/article/interpreter
from abc import ABC, abstractmethod


class IValue(ABC):
    @abstractmethod
    def getValue(self) -> int:
        pass


class Value(IValue):
    def __init__(self, value) -> None:
        self.value: int = value

    def getValue(self) -> int:
        return self.value


class Add(IValue):
    def __init__(self, value1, value2) -> None:
        self.value1: IValue = value1
        self.value2: IValue = value2

    def getValue(self) -> int:
        return self.value1.getValue() + self.value2.getValue()


class Mul(IValue):
    def __init__(self, value1, value2) -> None:
        self.value1: IValue = value1
        self.value2: IValue = value2

    def getValue(self) -> int:
        return self.value1.getValue() * self.value2.getValue()


obj = Mul(Add(Value(1), Value(2)), Value(3))

print(obj.getValue())
