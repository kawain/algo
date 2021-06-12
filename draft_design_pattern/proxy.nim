type
  Door = ref object of RootObj
  LabDoor = ref object of Door

  Security = ref object
    door: Door


method open(self: Door) {.base, locks: "unknown".} =
  discard

method close(self: Door) {.base, locks: "unknown".} =
  discard


method open(self: LabDoor) {.locks: "unknown".} =
  echo "研究室のドアを開く"

method close(self: LabDoor) {.locks: "unknown".} =
  echo "研究室のドアを閉じる"


proc authenticate(self: Security, password: string): bool =
  password == "abcd"

proc open(self: Security, password: string) =
  if self.authenticate(password):
    self.door.open()
  else:
    echo "絶対ダメ！開けられません。"

proc close(self: Security) =
  self.door.close()


proc main() =
  let door = Security(door: LabDoor())
  door.open("invalid")

  door.open("abcd")
  door.close()


main()
