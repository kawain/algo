type
  Door = ref object of RootObj
  WoodenDoor = ref object of Door
  IronDoor = ref object of Door

  DoorFittingExpert = ref object of RootObj
  Welder = ref object of DoorFittingExpert
  Carpenter = ref object of DoorFittingExpert

  DoorFactory = ref object of RootObj
  WoodenDoorFactory = ref object of DoorFactory
  IronDoorFactory = ref object of DoorFactory


method getDescription(self: Door) {.base, locks: "unknown".} =
  discard

method getDescription(self: WoodenDoor) {.locks: "unknown".} =
  echo "私は木のドアです"

method getDescription(self: IronDoor) {.locks: "unknown".} =
  echo "私は鉄のドアです"


method getDescription(self: DoorFittingExpert) {.base, locks: "unknown".} =
  discard

method getDescription(self: Welder) {.locks: "unknown".} =
  echo "私が取り付けられるのは鉄のドアだけです"

method getDescription(self: Carpenter) {.locks: "unknown".} =
  echo "私が取り付けられるのは木のドアだけです"


method makeDoor(
  self: DoorFactory
): Door{.base, locks: "unknown".} =
  discard

method makeFittingExpert(
  self: DoorFactory
): DoorFittingExpert{.base, locks: "unknown".} =
  discard

method makeDoor(
  self: WoodenDoorFactory
): Door {.locks: "unknown".} =
  WoodenDoor()

method makeFittingExpert(
  self: WoodenDoorFactory
): DoorFittingExpert{.locks: "unknown".} =
  Carpenter()

method makeDoor(
  self: IronDoorFactory
): Door {.locks: "unknown".} =
  IronDoor()

method makeFittingExpert(
  self: IronDoorFactory
): DoorFittingExpert {.locks: "unknown".} =
  Welder()


proc main() =
  let woodenFactory = WoodenDoorFactory()
  var door = woodenFactory.makeDoor()
  var expert = woodenFactory.makeFittingExpert()
  door.getDescription()
  expert.getDescription()

  let ironFactory = IronDoorFactory()
  door = ironFactory.makeDoor()
  expert = ironFactory.makeFittingExpert()
  door.getDescription()
  expert.getDescription()


main()
