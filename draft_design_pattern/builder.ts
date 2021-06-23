export {};

class Burger {
  builder: BurgerBuilder;
  size: number;
  cheese: boolean;
  pepperoni: boolean;
  lettuce: boolean;
  tomato: boolean;

  constructor(builder: BurgerBuilder) {
    this.builder = builder;
    this.size = builder.size;
    this.cheese = builder.cheese;
    this.pepperoni = builder.pepperoni;
    this.lettuce = builder.lettuce;
    this.tomato = builder.tomato;
  }
}

// builderを記述します
class BurgerBuilder {
  size: number;
  cheese: boolean;
  pepperoni: boolean;
  lettuce: boolean;
  tomato: boolean;
  constructor(size: number) {
    this.size = size;
    this.cheese = false;
    this.pepperoni = false;
    this.lettuce = false;
    this.tomato = false;
  }
  addPepperoni(): BurgerBuilder {
    this.pepperoni = true;
    return this;
  }
  addLettuce(): BurgerBuilder {
    this.lettuce = true;
    return this;
  }
  addCheese(): BurgerBuilder {
    this.cheese = true;
    return this;
  }
  addTomato(): BurgerBuilder {
    this.tomato = true;
    return this;
  }
  build(): Burger {
    return new Burger(this);
  }
}

const burger: Burger = new BurgerBuilder(14)
  .addPepperoni()
  .addLettuce()
  .addTomato()
  .build();

console.log("size:", burger.size);
console.log("cheese:", burger.cheese);
console.log("pepperoni", burger.pepperoni);
console.log("lettuce", burger.lettuce);
console.log("tomato", burger.tomato);
