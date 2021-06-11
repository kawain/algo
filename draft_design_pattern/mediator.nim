import strformat
import times


type
  ChatRoomMediator = ref object of RootObj
  ChatRoom = ref object of ChatRoomMediator

  User = ref object
    name: string
    chatMediator: ChatRoomMediator


# プロトタイプ宣言
proc getName(self: User): string


method showMessage(self: ChatRoomMediator, user: User, message: string) {.base,
    locks: "unknown".} =
  discard


method showMessage(self: ChatRoom, user: User, message: string) {.
    locks: "unknown".} =
  let date = now().format("yyyy-MM-dd(ddd)HH:mm")
  let sender = user.getName()
  echo fmt"{date}[{sender}]{message}"


proc getName(self: User): string =
  self.name

proc send(self: User, message: string) =
  self.chatMediator.showMessage(self, message)


proc main() =
  let mediator = ChatRoom()

  let john = User(name: "John Doe", chatMediator: mediator)
  let jane = User(name: "Jane Doe", chatMediator: mediator)

  john.send("こんちは！")
  jane.send("よう！")

main()

