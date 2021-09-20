from abc import ABC, abstractmethod


class ClassA:
    def print(self):
        obj = self.create()
        print(obj.get_msg())

    def create(self):
        obj: ITest = ClassB()
        return obj


class ClassAEx(ClassA):
    # オーバライド
    def create(self):
        obj: ITest = ClassC()
        return obj


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


obj = ClassA()
obj.print()

obj = ClassAEx()
obj.print()
