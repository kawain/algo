# facadeパターンは、複雑なサブシステムへのシンプルなインターフェイスを提供します

class Computer:
    def getElectricShock(self) -> None:
        print("ビリビリ！")

    def makeSound(self) -> None:
        print("ピッ！ポッ！")

    def showLoadingScreen(self) -> None:
        print("読み込み中...")

    def bam(self) -> None:
        print("準備ができました！")

    def closeEverything(self) -> None:
        print("ビーッ！ビーッ！ビビビビビ！")

    def sooth(self) -> None:
        print("（シーン）")

    def pullCurrent(self) -> None:
        print("プシューッ!")


# 次にfacadeを記述します

class ComputerFacade:
    def __init__(self, computer: Computer) -> None:
        self.computer: Computer = computer

    def turnOn(self) -> None:
        self.computer.getElectricShock()
        self.computer.makeSound()
        self.computer.showLoadingScreen()
        self.computer.bam()

    def turnOff(self) -> None:
        self.computer.closeEverything()
        self.computer.pullCurrent()
        self.computer.sooth()


computer = ComputerFacade(Computer())
computer.turnOn()
computer.turnOff()
