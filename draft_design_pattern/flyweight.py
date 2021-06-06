# flyweightパターンは、同じようなオブジェクトをできるだけ共有することで、メモリ使用量や計算コストを最小化します

# 最初にお茶の種類とティーメーカーを記述します

# キャッシュされるものはすべてflyweightになる。
# ここではお茶の種類がflyweightになる。
class KarakTea:
    def __init__(self, val: str) -> None:
        self.val: str = val


# Factoryとして振舞い、お茶を保存する
class TeaMaker:
    def __init__(self) -> None:
        self.availableTea: dict[str, KarakTea] = {}

    def make(self, preference: str) -> KarakTea:
        if preference not in self.availableTea:
            self.availableTea[preference] = KarakTea(preference)
        return self.availableTea[preference]


# 続いてTeaShopを記述し、注文を受けてお茶を出すようにします
class TeaShop:
    def __init__(self, teaMaker: TeaMaker) -> None:
        self.orders: dict[int, KarakTea] = {}
        self.teaMaker: TeaMaker = teaMaker

    def takeOrder(self, teaType: str, table: int):
        self.orders[table] = self.teaMaker.make(teaType)

    def serve(self):
        for v in self.orders:
            print(f"テーブル# {v}にお茶を出す {self.orders[v].val} {id(self.orders[v])}")


teaMaker = TeaMaker()
shop = TeaShop(teaMaker)

shop.takeOrder('砂糖少なめ', 1)
shop.takeOrder('ミルク多め', 2)
shop.takeOrder('砂糖なし', 5)
shop.takeOrder('砂糖なし', 6)
shop.takeOrder('砂糖少なめ', 7)

shop.serve()
