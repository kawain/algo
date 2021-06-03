# Simple Factory からのドアの例を拡張します。
# 必要に応じて、木製ドア ショップから木製ドア、
# 鉄製ショップから鉄製ドア、または関連ショップから PVC ドアを入手できます。
# さらに、ドアを取り付けるには、異なる種類の専門家が必要になる場合があります。
# たとえば、木製のドアには大工、鉄製のドアには溶接工などがあります。
# ご覧のとおり、ドア間には依存関係があります。
# 木製のドアには大工、鉄のドアが必要です。 溶接機などが必要です。
from abc import ABCMeta, abstractmethod

# まず最初に、Door インターフェースとその実装があります


class Door(metaclass=ABCMeta):
    @abstractmethod
    def getDescription(self) -> None:
        pass


class WoodenDoor(Door):
    def getDescription(self) -> None:
        print('私は木のドアです')


class IronDoor(Door):
    def getDescription(self) -> None:
        print('私は鉄のドアです')


# 次に、各ドアタイプのフィッティングの専門家がいます

class DoorFittingExpert(metaclass=ABCMeta):
    @abstractmethod
    def getDescription(self) -> None:
        pass


class Welder(DoorFittingExpert):
    def getDescription(self) -> None:
        print('私が取り付けられるのは鉄のドアだけです')


class Carpenter(DoorFittingExpert):
    def getDescription(self) -> None:
        print('私が取り付けられるのは木のドアだけです')


# 木製ドア工場は木製ドアと木製ドア取り付け専門家を作成し、
# 鉄製ドア工場は鉄製ドアと鉄ドア取り付け専門家を作成します


class DoorFactory(metaclass=ABCMeta):
    @abstractmethod
    def makeDoor(self) -> Door:
        pass

    @abstractmethod
    def makeFittingExpert(self) -> DoorFittingExpert:
        pass


# 木製ドアのファクトリーは大工と木製ドアを返す
class WoodenDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return WoodenDoor()

    def makeFittingExpert(self) -> DoorFittingExpert:
        return Carpenter()


# 鉄製ドアのファクトリーで鉄製ドアとそれに合う取付職人を取得
class IronDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return IronDoor()

    def makeFittingExpert(self) -> DoorFittingExpert:
        return Welder()


# 次のように使用できます

woodenFactory = WoodenDoorFactory()
door = woodenFactory.makeDoor()
expert = woodenFactory.makeFittingExpert()
door.getDescription()
expert.getDescription()

ironFactory = IronDoorFactory()
door = ironFactory.makeDoor()
expert = ironFactory.makeFittingExpert()
door.getDescription()
expert.getDescription()
