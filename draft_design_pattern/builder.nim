type
  BurgerBuilder = object
    size: int
    cheese: bool
    pepperoni: bool
    lettuce: bool
    tomato: bool

  Burger = object
    size: int
    cheese: bool
    pepperoni: bool
    lettuce: bool
    tomato: bool


proc newBurger(builder: BurgerBuilder): Burger =
  result = Burger()
  result.size = builder.size
  result.cheese = builder.cheese
  result.pepperoni = builder.pepperoni
  result.lettuce = builder.lettuce
  result.tomato = builder.tomato


proc addPepperoni(self: var BurgerBuilder): BurgerBuilder =
  self.pepperoni = true
  self

proc addLettuce(self: var BurgerBuilder): BurgerBuilder =
  self.lettuce = true
  self

proc addCheese(self: var BurgerBuilder): BurgerBuilder =
  self.cheese = true
  self

proc addTomato(self: var BurgerBuilder): BurgerBuilder =
  self.tomato = true
  self

proc build(self: BurgerBuilder): Burger =
  newBurger(self)



proc main() =
  var builder: BurgerBuilder = BurgerBuilder(size: 14)
  builder = builder.addPepperoni()
  builder = builder.addLettuce()
  builder = builder.addTomato()
  let burger: Burger = builder.build()
  echo "size:" & $burger.size
  echo "cheese:" & $burger.cheese
  echo "pepperoni:" & $burger.pepperoni
  echo "lettuce:" & $burger.lettuce
  echo "tomato:" & $burger.tomato


main()
