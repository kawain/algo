# proxyパターンを使うと、あるクラスが別のクラスの機能を表現できるようになります

from abc import ABC, abstractmethod

# 最初にDoorインターフェイスとその実装を記述


class Door(ABC):
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class LabDoor(Door):
    def open(self) -> None:
        print("研究室のドアを開く")

    def close(self) -> None:
        print("研究室のドアを閉じる")


# 続いて、必要なすべてのドアをセキュアにするproxyを記述します

class Security:
    def __init__(self, door: Door) -> None:
        self.door: Door = door

    def open(self, password: str) -> None:
        if self.authenticate(password):
            self.door.open()
        else:
            print("絶対ダメ！開けられません。")

    def authenticate(self, password: str) -> bool:
        return password == 'abcd'

    def close(self) -> None:
        self.door.close()


door = Security(LabDoor())
door.open('invalid')

door.open('abcd')
door.close()
