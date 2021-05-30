# Observerパターンの例
# 状態の変化を通知する
import os
import random
import strformat


type
  Observer = ref object of RootObj
  DigitObserver = ref object of Observer
  GraphObserver = ref object of Observer

  NumberGenerator = ref object of RootObj
    observers: seq[Observer]
  RandomNumberGenerator = ref object of NumberGenerator
    number: int


method getNumber(self: NumberGenerator): int{.base.}
method getNumber(self: RandomNumberGenerator): int


# https://nim-lang.org/docs/manual_experimental.html#guards-and-locks-lock-levels
method update(
  self: Observer, ganerator: NumberGenerator
){.base, locks: "unknown".} =
  discard

method update(self: DigitObserver, ganerator: NumberGenerator) =
  sleep(100)
  echo fmt"""DigitObservser: {ganerator.getNumber()}"""

method update(self: GraphObserver, ganerator: NumberGenerator) =
  sleep(100)
  stdout.write "GraphicObserver:"
  let count = ganerator.getNumber()
  for _ in 0..<count:
    stdout.write '*'
  echo ""


method addObserver(self: NumberGenerator, observer: Observer) {.base.} =
  self.observers.add(observer)

method deleteObserver(self: NumberGenerator, observer: Observer) {.base.} =
  self.observers.delete(self.observers.find(observer))

method notifyObserver(self: NumberGenerator){.base.} =
  for o in self.observers:
    o.update(self)

method getNumber(self: NumberGenerator): int{.base.} =
  discard

# https://nim-lang.org/docs/manual_experimental.html#guards-and-locks-lock-levels
method execute(self: NumberGenerator) {.base, locks: "unknown".} =
  discard

method getNumber(self: RandomNumberGenerator): int =
  return self.number

method execute(self: RandomNumberGenerator) =
  for _ in 0..20:
    self.number = rand(10)
    # 親のメソッドを呼び出したい時
    procCall NumberGenerator(self).notifyObserver()


proc main() =
  randomize()

  let generator = RandomNumberGenerator(number: 0)
  let observer1 = DigitObserver()
  let observer2 = GraphObserver()
  generator.addObserver(observer1)
  generator.addObserver(observer2)
  generator.execute()

  echo "終了"


main()
