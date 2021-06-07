# prototypeパターンは、既存のオブジェクトを「クローン」することでオブジェクトを作成します。
import copy


class Sheep:
    def __init__(self, name: str, category: str = "オオツノヒツジ") -> None:
        self.name = name
        self.category = category

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def setCategory(self, category: str) -> None:
        self.category = category

    def getCategory(self) -> str:
        return self.category


original = Sheep('ジョリー')
print(original.getName())
print(original.getCategory())
print(id(original))

# 参照
reference = original
print(id(reference))

# クローン後、必要なものを変更する
cloned = copy.deepcopy(original)
cloned.setName('ドリー')
print(cloned.getName())
print(cloned.getCategory())
print(id(cloned))

# オリジナル再確認
print(original.getName())
