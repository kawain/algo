export {};

interface Door {
  open(): void;
  close(): void;
}

class LabDoor implements Door {
  open(): void {
    console.log("研究室のドアを開く");
  }
  close(): void {
    console.log("研究室のドアを閉じる");
  }
}

class Security {
  constructor(private door: Door) {}
  open(password: string): void {
    if (this.authenticate(password)) {
      this.door.open();
    } else {
      console.log("絶対ダメ！開けられません。");
    }
  }
  authenticate(password: string): boolean {
    return password == "abcd";
  }
  close(): void {
    this.door.close();
  }
}

const door = new Security(new LabDoor());
door.open("invalid");

door.open("abcd");
door.close();
