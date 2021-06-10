export {};

class Computer {
  getElectricShock(): void {
    console.log("ビリビリ！");
  }
  makeSound(): void {
    console.log("ピッ！ポッ！");
  }
  showLoadingScreen(): void {
    console.log("読み込み中...");
  }
  bam(): void {
    console.log("準備ができました！");
  }
  closeEverything(): void {
    console.log("ビーッ！ビーッ！ビビビビビ！");
  }
  sooth(): void {
    console.log("（シーン）");
  }
  pullCurrent(): void {
    console.log("プシューッ!");
  }
}

class ComputerFacade {
  constructor(private computer: Computer) {}
  turnOn(): void {
    this.computer.getElectricShock();
    this.computer.makeSound();
    this.computer.showLoadingScreen();
    this.computer.bam();
  }

  turnOff(): void {
    this.computer.closeEverything();
    this.computer.pullCurrent();
    this.computer.sooth();
  }
}

const computer = new ComputerFacade(new Computer());
computer.turnOn();
computer.turnOff();
