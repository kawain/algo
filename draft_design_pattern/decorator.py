# decoratorパターンは、オブジェクトをdecoratorクラスのオブジェクトにラップすることで、
# 実行時にオブジェクトの振舞いを動的に変更できるようにします
from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def getCost(self) -> int:
        pass

    @abstractmethod
    def getDescription(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def getCost(self) -> int:
        return 10

    def getDescription(self) -> str:
        return "Simple coffee"


class MilkCoffee(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self.coffee = coffee

    def getCost(self):
        return self.coffee.getCost() + 2

    def getDescription(self):
        return self.coffee.getDescription() + '、ミルク'


class WhipCoffee(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self.coffee = coffee

    def getCost(self):
        return self.coffee.getCost() + 5

    def getDescription(self):
        return self.coffee.getDescription() + '、ホイップ'


class VanillaCoffee(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self.coffee = coffee

    def getCost(self):
        return self.coffee.getCost() + 5

    def getDescription(self):
        return self.coffee.getDescription() + '、バニラ'


someCoffee = SimpleCoffee()
print(someCoffee.getCost())
print(someCoffee.getDescription())

someCoffee = MilkCoffee(someCoffee)
print(someCoffee.getCost())
print(someCoffee.getDescription())

someCoffee = WhipCoffee(someCoffee)
print(someCoffee.getCost())
print(someCoffee.getDescription())

someCoffee = VanillaCoffee(someCoffee)
print(someCoffee.getCost())
print(someCoffee.getDescription())
