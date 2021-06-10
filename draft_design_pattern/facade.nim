type
  Computer = ref object
  ComputerFacade = ref object
    computer: Computer


proc getElectricShock(self: Computer) =
  echo "ビリビリ！"

proc makeSound(self: Computer) =
  echo "ピッ！ポッ！"

proc showLoadingScreen(self: Computer) =
  echo "読み込み中..."

proc bam(self: Computer) =
  echo "準備ができました！"

proc closeEverything(self: Computer) =
  echo "ビーッ！ビーッ！ビビビビビ！"

proc sooth(self: Computer) =
  echo "（シーン）"

proc pullCurrent(self: Computer) =
  echo "プシューッ!"


proc turnOn(self: ComputerFacade) =
  self.computer.getElectricShock()
  self.computer.makeSound()
  self.computer.showLoadingScreen()
  self.computer.bam()

proc turnOff(self: ComputerFacade) =
  self.computer.closeEverything()
  self.computer.pullCurrent()
  self.computer.sooth()


proc main() =
  let computer = ComputerFacade(computer: Computer())
  computer.turnOn()
  computer.turnOff()


main()
