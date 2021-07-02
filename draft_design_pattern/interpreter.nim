type
  IValue = ref object of RootObj
  Value = ref object of IValue
    value: int
  Add = ref object of IValue
    value1: IValue
    value2: IValue
  Mul = ref object of IValue
    value1: IValue
    value2: IValue


method getValue(self: IValue): int {.base, locks: "unknown".} =
  discard


method getValue(self: Value): int {.locks: "unknown".} =
  self.value


method getValue(self: Add): int {.locks: "unknown".} =
  self.value1.getValue() + self.value2.getValue()


method getValue(self: Mul): int {.locks: "unknown".} =
  self.value1.getValue() * self.value2.getValue()


let obj = Mul(
  value1: Add(value1: Value(value: 1), value2: Value(value: 2)),
  value2: Value(value: 3)
)

echo obj.getValue()
