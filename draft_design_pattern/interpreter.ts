export {};

interface IValue {
  getValue(): number;
}

class Value implements IValue {
  constructor(public value: number) {}
  getValue() {
    return this.value;
  }
}

class Add implements IValue {
  constructor(public value1: IValue, public value2: IValue) {}
  getValue() {
    return this.value1.getValue() + this.value2.getValue();
  }
}

class Mul implements IValue {
  constructor(public value1: IValue, public value2: IValue) {}
  getValue() {
    return this.value1.getValue() * this.value2.getValue();
  }
}

const obj = new Mul(new Add(new Value(1), new Value(2)), new Value(3));

console.log(obj.getValue());
