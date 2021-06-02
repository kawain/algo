type
  Door = ref object of RootObj
  WoodenDoor = ref object of Door
    width: float
    height: float

  DoorFactory = ref object


method getWidth(self: Door): float{.base, locks: "unknown".} =
  discard

method getHeight(self: Door): float{.base, locks: "unknown".} =
  discard


method getWidth(self: WoodenDoor): float{.locks: "unknown".} =
  return self.width

method getHeight(self: WoodenDoor): float{.locks: "unknown".} =
  return self.height


proc makeDoor(self: DoorFactory, width: float, height: float): Door =
  return WoodenDoor(width: width, height: height)


proc main() =
  let obj = DoorFactory()
  let door: Door = obj.makeDoor(200, 300)
  echo door.getWidth()
  echo door.getHeight()

main()
