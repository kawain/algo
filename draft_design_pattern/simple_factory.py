# シンプルなファクトリは、
# インスタンス化ロジックをクライアントに公開せずに、
# クライアントのインスタンスを生成するだけです。
from abc import ABCMeta, abstractmethod


class Door(metaclass=ABCMeta):
    @abstractmethod
    def getWidth(self) -> float:
        pass

    @abstractmethod
    def getHeight(self) -> float:
        pass


class WoodenDoor(Door):
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

    def getWidth(self) -> float:
        return self.width

    def getHeight(self) -> float:
        return self.height


class DoorFactory:
    @staticmethod
    def makeDoor(width: float, height: float) -> Door:
        return WoodenDoor(width, height)


door = DoorFactory.makeDoor(100, 200)
print(door.getWidth())
print(door.getHeight())
