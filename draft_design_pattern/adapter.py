# 変換アダプタ
# アダプタパターンを使用すると、
# 互換性のないオブジェクトをアダプタにラップして、
# 別のクラスと互換性を持たせることができます。
from abc import ABCMeta, abstractmethod

# ハンターがいて、彼がライオンを狩るゲームを考えてみましょう。
# 最初に、すべてのタイプのライオンが実装する必要があるインターフェース Lion があります。


class Lion(metaclass=ABCMeta):
    @abstractmethod
    def roar(self) -> None:
        pass


class AfricanLion(Lion):
    def roar(self) -> None:
        print("がお")


class AsianLion(Lion):
    def roar(self) -> None:
        print("ぐう")


# そしてハンターは、Lion インターフェースの実装で狩りをすることに期待しています

class Hunter:
    def hunt(self, lion: Lion) -> None:
        lion.roar()


# ゲームに WildDog を追加する必要があるとしましょう。
# しかし、WildDog と Lion は別の型なので
# これを直接行うことはできません。
# Hunterと互換性を持たせるには、
# 互換性のあるアダプタを作成する必要があります。


class WildDog:
    def bark(self) -> None:
        print("わん")


# ゲームに互換性を持たせるためのWildDogとLionのアダプタ

class WildDogAdapter(Lion):
    def __init__(self, dog: WildDog) -> None:
        self.dog = dog

    def roar(self) -> None:
        self.dog.bark()


# ハンター
hunter = Hunter()

# 普通のLionインターフェイス
obj1 = AfricanLion()
hunter.hunt(obj1)
obj2 = AsianLion()
hunter.hunt(obj2)

# Lionインターフェイスの WildDogAdapter に WildDog オブジェクトを持たせる
wildDog = WildDog()
wildDogAdapter = WildDogAdapter(wildDog)

# LionインターフェイスになったのでHunterのhuntができる
hunter.hunt(wildDogAdapter)
