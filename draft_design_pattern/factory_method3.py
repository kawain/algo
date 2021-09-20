# factory_method2を用いない(内部でオブジェクトを作成しない)パターン
from abc import ABC, abstractmethod


class ITest(ABC):
    @abstractmethod
    def get_msg(self):
        pass


class ClassB(ITest):
    def get_msg(self):
        return "りんご"


class ClassC(ITest):
    def get_msg(self):
        return "みかん"


class ClassA:
    def __init__(self, obj: ITest):
        self.obj: ITest = obj

    def print(self):
        print(self.obj.get_msg())


obj = ClassA(ClassB())
obj.print()

obj = ClassA(ClassC())
obj.print()
