export {};

interface Coffee {
  getCost(): number;
  getDescription(): string;
}

class SimpleCoffee implements Coffee {
  getCost(): number {
    return 10;
  }
  getDescription(): string {
    return "Simple coffee";
  }
}

class MilkCoffee implements Coffee {
  constructor(private coffee: Coffee) {}
  getCost(): number {
    return this.coffee.getCost() + 2;
  }
  getDescription(): string {
    return this.coffee.getDescription() + "、ミルク";
  }
}

class WhipCoffee implements Coffee {
  constructor(private coffee: Coffee) {}
  getCost(): number {
    return this.coffee.getCost() + 5;
  }
  getDescription(): string {
    return this.coffee.getDescription() + "、ホイップ";
  }
}

class VanillaCoffee implements Coffee {
  constructor(private coffee: Coffee) {}
  getCost(): number {
    return this.coffee.getCost() + 5;
  }
  getDescription(): string {
    return this.coffee.getDescription() + "、バニラ";
  }
}

let someCoffee = new SimpleCoffee();
console.log(someCoffee.getCost());
console.log(someCoffee.getDescription());

someCoffee = new MilkCoffee(someCoffee);
console.log(someCoffee.getCost());
console.log(someCoffee.getDescription());

someCoffee = new WhipCoffee(someCoffee);
console.log(someCoffee.getCost());
console.log(someCoffee.getDescription());

someCoffee = new VanillaCoffee(someCoffee);
console.log(someCoffee.getCost());
console.log(someCoffee.getDescription());
