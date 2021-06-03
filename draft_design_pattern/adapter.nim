type
  Lion = ref object of RootObj
  AfricanLion = ref object of Lion
  AsianLion = ref object of Lion

  Hunter = ref object

  WildDog = ref object
  WildDogAdapter = ref object of Lion
    dog: WildDog



method roar(self: Lion) {.base, locks: "unknown".} =
  discard

method roar(self: AfricanLion) {.locks: "unknown".} =
  echo "がお"

method roar(self: AsianLion) {.locks: "unknown".} =
  echo "ぐう"

proc hunt(self: Hunter, lion: Lion) =
  lion.roar()

proc bark(self: WildDog) =
  echo "わん"

method roar(self: WildDogAdapter) {.locks: "unknown".} =
  self.dog.bark()



proc main() =
  let hunter = Hunter()
  let obj1 = AfricanLion()
  hunter.hunt(obj1)
  let obj2 = AsianLion()
  hunter.hunt(obj2)

  let wildDog = WildDog()
  let wildDogAdapter = WildDogAdapter(dog: wildDog)
  hunter.hunt(wildDogAdapter)


main()
