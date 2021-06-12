type Sheep = ref object
  name: string
  category: string


proc newSheep(name: string, category: string = "オオツノヒツジ"): Sheep =
  Sheep(name: name, category: category)

proc setName(self: Sheep, name: string) =
  self.name = name

proc getName(self: Sheep): string =
  self.name

proc setCategory(self: Sheep, category: string) =
  self.category = category

proc getCategory(self: Sheep): string =
  self.category


proc main() =
  var original = newSheep("ジョリー")
  echo original.getName()
  echo original.getCategory()

  echo "----"

  # 参照
  var reference = original
  reference.setName("ジョリー参照")
  echo reference.getName()
  echo original.getName()

  echo "----"

  # コピー
  var cloned: Sheep
  cloned.deepCopy(original)

  cloned.setName("ジョリーコピー")
  cloned.setCategory("ヤギ")

  echo cloned.getName()
  echo cloned.getCategory()

  echo "---- オリジナル"

  echo original.getName()
  echo original.getCategory()


main()
