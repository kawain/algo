export {};

function getRandomInt(max: number): number {
  return Math.floor(Math.random() * max);
}

interface Observer {
  update(generator: NumberGenerator): void;
}

abstract class NumberGenerator {
  private observers: Observer[] = [];
  addObserver(observer: Observer): void {
    this.observers.push(observer);
  }
  deleteObserver(observer: Observer): void {
    this.observers = this.observers.filter((v) => v !== observer);
  }
  notifyObservers(): void {
    for (const v of this.observers) {
      v.update(this);
    }
  }
  abstract getNumber(): number;
  abstract execute(): void;
}

class DegitObserver implements Observer {
  update(generator: NumberGenerator): void {
    console.log("DegitObserver:", generator.getNumber());
  }
}

class GraphObserver implements Observer {
  update(generator: NumberGenerator): void {
    const count: number = generator.getNumber();
    let a = "";
    for (let i = 0; i < count; i++) {
      a += "*";
    }
    console.log("GraphObserver:", a);
  }
}

class RandomNumberGenerator extends NumberGenerator {
  private num: number;
  constructor() {
    super();
    this.num = 0;
  }
  getNumber(): number {
    return this.num;
  }
  execute(): void {
    for (let i = 0; i < 20; i++) {
      this.num = getRandomInt(10);
      this.notifyObservers();
    }
  }
}

const generator = new RandomNumberGenerator();
const degitObserver = new DegitObserver();
const graphObserver = new GraphObserver();
generator.addObserver(degitObserver);
generator.addObserver(graphObserver);
generator.execute();
