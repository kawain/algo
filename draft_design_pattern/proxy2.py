from abc import ABC, abstractmethod


class ITest(ABC):
    @abstractmethod
    def show_msg(self, s):
        pass


class Test(ITest):
    def show_msg(self, s):
        return s


class ProxyTest(ITest):
    def __init__(self, obj):
        self.obj = obj

    def show_msg(self, s):
        s = "★" + s + "★"
        return self.obj.show_msg(s)


obj = Test()
print(obj.show_msg("test"))

obj2 = ProxyTest(obj)
print(obj2.show_msg("test"))
