export {};

class Bulb {
  turnOn(): void {
    console.log("電球がつきました！");
  }
  turnOff(): void {
    console.log("真っ暗！");
  }
}

interface Command {
  bulb: Bulb;
  execute(): void;
  undo(): void;
  redo(): void;
}

class TurnOn implements Command {
  constructor(public bulb: Bulb) {}
  execute(): void {
    this.bulb.turnOn();
  }
  undo(): void {
    this.bulb.turnOff();
  }
  redo(): void {
    this.execute();
  }
}

class TurnOff implements Command {
  constructor(public bulb: Bulb) {}
  execute(): void {
    this.bulb.turnOff();
  }
  undo(): void {
    this.bulb.turnOn();
  }
  redo(): void {
    this.execute();
  }
}

class RemoteControl {
  submit(command: Command): void {
    command.execute();
  }
}

function main(): void {
  const bulb: Bulb = new Bulb();

  const turnOn: Command = new TurnOn(bulb);
  const turnOff: Command = new TurnOff(bulb);

  // 直実行
  turnOn.execute();
  turnOn.undo();
  turnOn.redo();

  // commandパターン
  const remote = new RemoteControl();
  remote.submit(turnOn);
  remote.submit(turnOff);
}

main();
