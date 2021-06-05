# mediatorパターンは、mediatorと呼ばれる第三者的なオブジェクトを追加することで、
# colleague（同僚）と呼ばれる2つのオブジェクト同士のやりとりを制御します。
# このパターンでは、クラスは相手のクラスの実装を知る必要がないため、
# クラス間の相互通信の結合を弱める働きがあります。
from abc import ABC, abstractmethod
import datetime as dt

# チャットルームのmediatorを記述


class ChatRoomMediator(ABC):
    @abstractmethod
    def showMessage(self, user: "User", message: str):
        pass


class ChatRoom(ChatRoomMediator):
    def showMessage(self, user: "User", message: str):
        time = dt.datetime.now()
        tdatetime = time.strftime('%Y-%m-%d %H:%M:%S')
        sender = user.getName()
        print(f"{tdatetime}[{sender}]:{message}")


# ユーザー（colleague）を記述


class User:
    def __init__(self, name: str, chatMediator: ChatRoomMediator):
        self.name = name
        self.chatMediator = chatMediator

    def getName(self):
        return self.name

    def send(self, message: str):
        self.chatMediator.showMessage(self, message)


mediator = ChatRoom()

john = User('John Doe', mediator)
jane = User('Jane Doe', mediator)

john.send('こんちは！')
jane.send('よう！')
