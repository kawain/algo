import tables
import strformat


type
  KarakTea = ref object
    val: string

  TeaMaker = ref object
    availableTea: Table[string, KarakTea]

  TeaShop = ref object
    orders: OrderedTable[int, KarakTea]
    teaMaker: TeaMaker


proc make(self: TeaMaker, preference: string): KarakTea =
  if not self.availableTea.hasKey(preference):
    self.availableTea[preference] = KarakTea(val: preference)
  return self.availableTea[preference]


proc takeOrder(self: TeaShop, teaType: string, table: int) =
  self.orders[table] = self.teaMaker.make(teaType)

proc serve(self: TeaShop) =
  for key, value in self.orders:
    echo fmt"テーブル# {key}にお茶を出す {value.val} {repr(value)}"


proc main() =
  let teaMaker: TeaMaker = TeaMaker()
  let shop: TeaShop = TeaShop(teaMaker: teaMaker)

  shop.takeOrder("砂糖少なめ", 1)
  shop.takeOrder("ミルク多め", 2)
  shop.takeOrder("砂糖なし", 5)
  shop.takeOrder("砂糖なし", 6)
  shop.takeOrder("砂糖少なめ", 7)

  shop.serve()


main()
