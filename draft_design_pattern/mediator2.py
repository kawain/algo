# https://9cubed.info/article/mediator
from abc import ABC, abstractmethod


class Mediator:
    def __init__(self) -> None:
        self.lst: list['IMedia'] = []

    def add(self, obj: 'IMedia') -> None:
        self.lst.append(obj)

    def testA(self) -> None:
        for obj in self.lst:
            obj.test()


class IMedia(ABC):
    @abstractmethod
    def test(self) -> None:
        pass


class Test(IMedia):
    def test(self) -> None:
        print("test")


class Test2(IMedia):
    def test(self) -> None:
        print("test2")


obj = Test()
obj2 = Test2()

mediator = Mediator()
mediator.add(obj)
mediator.add(obj2)

mediator.testA()
