# 多重継承

# class Pencil():
#     def __init__(self, color="black"):
#         self.color = color

#     def write(self):
#         print(f"{self.color}で書きます")


# class Eraser():
#     def erase(self):
#         print("消します")


# class RedPencil(Pencil, Eraser):
#     def __init__(self, color="red"):
#         super().__init__(color=color)


# class BluePencil(Pencil, Eraser):
#     def __init__(self, color="blue"):
#         super().__init__(color=color)


# obj1 = RedPencil()
# obj1.write()
# obj1.erase()

# obj2 = BluePencil()
# obj2.write()
# obj2.erase()


# コンポジション
from abc import ABC, abstractmethod


class IBridge(ABC):
    @abstractmethod
    def erase(self):
        pass


class Eraser(IBridge):
    def erase(self):
        print("消します")


class Pencil(IBridge):
    def __init__(self, color="black"):
        self.obj = Eraser()
        self.color = color

    def write(self):
        print(f"{self.color}で書きます")

    def erase(self):
        self.obj.erase()


class RedPencil(Pencil):
    def __init__(self, color="red"):
        super().__init__(color=color)


class BluePencil(Pencil):
    def __init__(self, color="blue"):
        super().__init__(color=color)


obj1 = RedPencil()
obj1.write()
obj1.erase()

obj2 = BluePencil()
obj2.write()
obj2.erase()
