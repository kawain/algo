# Visitorパターン
type

  Visitor = ref object of RootObj

  Visitor1 = ref object of Visitor

  Maru1 = ref object
    name: string
  Maru2 = ref object
    name: string
  Maru3 = ref object
    name: string



method visit(self: Visitor, obj: Maru1){.base, locks: "unknown".} =
  discard

method visit(self: Visitor, obj: Maru2){.base, locks: "unknown".} =
  discard

method visit(self: Visitor, obj: Maru3){.base, locks: "unknown".} =
  discard



method visit(self: Visitor1, obj: Maru1){.locks: "unknown".} =
  echo "Maru1実行 " & obj.name

method visit(self: Visitor1, obj: Maru2) {.locks: "unknown".} =
  echo "Maru2実行 " & obj.name

method visit(self: Visitor1, obj: Maru3) {.locks: "unknown".} =
  echo "Maru3実行 " & obj.name



proc accept(self: Maru1, obj: Visitor) =
  obj.visit(self)

proc accept(self: Maru2, obj: Visitor) =
  obj.visit(self)

proc accept(self: Maru3, obj: Visitor) =
  obj.visit(self)


proc main() =
  let v1: Visitor = Visitor1()

  let maru1 = Maru1(name: "その１")
  maru1.accept(v1)

  let maru2 = Maru2(name: "その２")
  maru2.accept(v1)

  let maru3 = Maru3(name: "その３")
  maru3.accept(v1)


main()

