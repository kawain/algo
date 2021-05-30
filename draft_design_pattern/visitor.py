
from abc import ABCMeta, abstractmethod


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, acceptor):
        pass


class ConcreteVisitorA(Visitor):
    def __init__(self):
        self.name = "ConcreteVisitorA"

    def visit(self, acceptor):
        print(self.name + " が " + acceptor.getName() + " を訪問しました。")


class ConcreteVisitorB(Visitor):
    def __init__(self):
        self.name = "ConcreteVisitorB"

    def visit(self, acceptor):
        print(self.name + " が " + acceptor.getName() + " を訪問しました。")


class Acceptor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class ConcreteAcceptorA(Acceptor):
    def __init__(self):
        self.name = "ConcreteAcceptorA"

    def getName(self):
        return self.name

    def accept(self, visitor):
        visitor.visit(self)


class ConcreteAcceptorB(Acceptor):
    def __init__(self):
        self.name = "ConcreteAcceptorB"

    def getName(self):
        return self.name

    def accept(self, visitor):
        visitor.visit(self)


def main():
    viA = ConcreteVisitorA()
    viB = ConcreteVisitorB()
    acA = ConcreteAcceptorA()
    acB = ConcreteAcceptorB()
    acA.accept(viA)
    acB.accept(viA)
    acA.accept(viB)
    acB.accept(viB)


main()
