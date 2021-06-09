# commandパターンは、操作をオブジェクト内にカプセル化できるようにします。
# このパターンの背後にある重要なアイデアは、クライアントをレシーバーから分離する手段を提供することです。
# あなた（Client）がリモコン（Invoker）でテレビ（Receiver）の電源をオンにするところも考えられます。
from abc import ABC, abstractmethod


# レシーバ
class Bulb:
    def turnOn(self) -> None:
        print("電球がつきました！")

    def turnOff(self) -> None:
        print("真っ暗！")


# 各コマンドを実装するインターフェイスを記述し、コマンドのセットを記述

class Command(ABC):
    def __init__(self, bulb: Bulb) -> None:
        self.bulb: Bulb = bulb

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

    @abstractmethod
    def redo(self) -> None:
        pass


# コマンド
class TurnOn(Command):
    def execute(self) -> None:
        self.bulb.turnOn()

    def undo(self) -> None:
        self.bulb.turnOff()

    def redo(self) -> None:
        self.execute()


class TurnOff(Command):
    def execute(self) -> None:
        self.bulb.turnOff()

    def undo(self) -> None:
        self.bulb.turnOn()

    def redo(self) -> None:
        self.execute()


# クライアントが任意のコマンドでやり取りする相手であるInvokerを記述します
class RemoteControl:
    def submit(self, command: Command) -> None:
        command.execute()


# クライアントでどのように利用できるか

bulb = Bulb()

turnOn: Command = TurnOn(bulb)
turnOff: Command = TurnOff(bulb)

# 直実行
turnOn.execute()
turnOn.undo()
turnOn.redo()

# commandパターン
remote = RemoteControl()
remote.submit(turnOn)
remote.submit(turnOff)
