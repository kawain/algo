type
  Coffee = ref object of RootObj
  SimpleCoffee = ref object of Coffee
  MilkCoffee = ref object of Coffee
    coffee: Coffee
  WhipCoffee = ref object of Coffee
    coffee: Coffee
  VanillaCoffee = ref object of Coffee
    coffee: Coffee



method getCost(self: Coffee): int {.base, locks: "unknown".} =
  discard

method getDescription(self: Coffee): string {.base, locks: "unknown".} =
  discard


method getCost(self: SimpleCoffee): int {.locks: "unknown".} =
  10

method getDescription(self: SimpleCoffee): string {.locks: "unknown".} =
  "Simple coffee"


method getCost(self: MilkCoffee): int {.locks: "unknown".} =
  self.coffee.getCost() + 2

method getDescription(self: MilkCoffee): string {.locks: "unknown".} =
  self.coffee.getDescription() & "、ミルク"


method getCost(self: WhipCoffee): int {.locks: "unknown".} =
  self.coffee.getCost() + 5

method getDescription(self: WhipCoffee): string {.locks: "unknown".} =
  self.coffee.getDescription() & "、ホイップ"


method getCost(self: VanillaCoffee): int {.locks: "unknown".} =
  self.coffee.getCost() + 5

method getDescription(self: VanillaCoffee): string {.locks: "unknown".} =
  self.coffee.getDescription() & "、バニラ"



proc main() =
  var someCoffee: Coffee = SimpleCoffee()
  echo someCoffee.getCost()
  echo someCoffee.getDescription()

  someCoffee = MilkCoffee(coffee: someCoffee)
  echo someCoffee.getCost()
  echo someCoffee.getDescription()

  someCoffee = WhipCoffee(coffee: someCoffee)
  echo someCoffee.getCost()
  echo someCoffee.getDescription()

  someCoffee = VanillaCoffee(coffee: someCoffee)
  echo someCoffee.getCost()
  echo someCoffee.getDescription()


main()
