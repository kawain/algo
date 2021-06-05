# commandパターンは、操作をオブジェクト内にカプセル化できるようにします。
# このパターンの背後にある重要なアイデアは、クライアントをレシーバーから分離する手段を提供することです。
# あなた（Client）がリモコン（Invoker）でテレビ（Receiver）の電源をオンにするところも考えられます。
from abc import ABC, abstractmethod


# レシーバ
class Bulb:
    def turnOn(self):
        print("電球がつきました！")

    def turnOff(self):
        print("真っ暗！")


# 各コマンドを実装するインターフェイスを記述し、コマンドのセットを記述

class Command(ABC):
    def __init__(self, bulb: Bulb):
        self.bulb: Bulb = bulb

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


# コマンド
class TurnOn(Command):
    def execute(self):
        self.bulb.turnOn()

    def undo(self):
        self.bulb.turnOff()

    def redo(self):
        self.execute()


class TurnOff(Command):
    def execute(self):
        self.bulb.turnOff()

    def undo(self):
        self.bulb.turnOn()

    def redo(self):
        self.execute()


# クライアントが任意のコマンドでやり取りする相手であるInvokerを記述します
class RemoteControl:
    def submit(self, command: Command):
        command.execute()


# クライアントでどのように利用できるか

bulb = Bulb()

turnOn = TurnOn(bulb)
turnOff = TurnOff(bulb)

# 直実行
turnOn.execute()
turnOn.undo()
turnOn.redo()

# commandパターン
remote = RemoteControl()
remote.submit(turnOn)
remote.submit(turnOff)
