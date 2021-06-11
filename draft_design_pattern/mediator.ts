export {};

interface ChatRoomMediator {
  showMessage(user: User, message: string): void;
}

class ChatRoom implements ChatRoomMediator {
  showMessage(user: User, message: string): void {
    const d = new Date();
    const y = d.getFullYear();
    const m = d.getMonth() + 1;
    const day = d.getDate();
    const ho = d.getHours();
    const mi = d.getMinutes();
    const sender = user.getName();
    console.log(
      `${y}-${m}-${day} ${ho}:${mi}[${sender}]:${message}`,
    );
  }
}

class User {
  constructor(public name: string, public chatMediator: ChatRoomMediator) {}
  getName(): string {
    return this.name;
  }
  send(message: string): void {
    this.chatMediator.showMessage(this, message);
  }
}

const mediator = new ChatRoom();

const john = new User("John Doe", mediator);
const jane = new User("Jane Doe", mediator);

john.send("こんちは！");
jane.send("よう！");
