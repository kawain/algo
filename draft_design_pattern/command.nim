type
  Bulb = ref object

  Command = ref object of RootObj
    bulb: Bulb
  TurnOn = ref object of Command
  TurnOff = ref object of Command

  RemoteControl = ref object


proc turnOn(self: Bulb) =
  echo "電球がつきました！"

proc turnOff(self: Bulb) =
  echo "真っ暗！"


method execute(self: Command) {.base, locks: "unknown".} =
  discard

method undo(self: Command) {.base, locks: "unknown".} =
  discard

method redo(self: Command) {.base, locks: "unknown".} =
  discard


method execute(self: TurnOn) {.locks: "unknown".} =
  self.bulb.turnOn()

method undo(self: TurnOn) {.locks: "unknown".} =
  self.bulb.turnOff()

method redo(self: TurnOn) {.locks: "unknown".} =
  self.execute()


method execute(self: TurnOff) {.locks: "unknown".} =
  self.bulb.turnOff()

method undo(self: TurnOff) {.locks: "unknown".} =
  self.bulb.turnOn()

method redo(self: TurnOff) {.locks: "unknown".} =
  self.execute()


proc submit(self: RemoteControl, command: Command) =
  command.execute()


proc main() =
  let bulb = Bulb()

  let turnOn = TurnOn(bulb: bulb)
  let turnOff = TurnOff(bulb: bulb)

  # 直実行
  turnOn.execute()
  turnOn.undo()
  turnOn.redo()

  # commandパターン
  let remote = RemoteControl()
  remote.submit(turnOn)
  remote.submit(turnOff)


main()
