from abc import ABC, abstractmethod


class ITest(ABC):
    @abstractmethod
    def get_value(self):
        pass


class TestA(ITest):
    def get_value(self):
        return 100


class TestB(ITest):
    def __init__(self, obj: ITest):
        self.obj = obj

    def get_value(self):
        v = self.obj.get_value()
        return v * 100


obj = TestB(TestA())
print(obj.get_value())
