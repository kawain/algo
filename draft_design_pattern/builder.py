# builderパターンとは、コンストラクタを汚さないようにしながら、
# さまざまなフレーバー（flavor: 味や香り、転じて追加的な要素）を
# 持つオブジェクトを作成できるようになります。
# オブジェクトにさまざまなフレーバーがある場合や、
# オブジェクトの作成に関連する手順が多い場合に有用です。
# telescoping constructor アンチパターンの解決を目指す
# コンストラクタのパラメータ数が増えて手に負えなくなる
# public function __construct($size, $cheese = true, $pepperoni = true, $tomato = false, $lettuce = true)
# {
# }


# 最初に、作りたいハンバーガーBurgerを記述
class Burger:
    def __init__(self, builder: "BurgerBuilder") -> None:
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.lettuce = builder.lettuce
        self.tomato = builder.tomato


# builderを記述します
class BurgerBuilder:
    def __init__(self, size: int) -> None:
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.lettuce = False
        self.tomato = False

    def addPepperoni(self) -> bool:
        self.pepperoni = True
        return self

    def addLettuce(self) -> bool:
        self.lettuce = True
        return self

    def addCheese(self) -> bool:
        self.cheese = True
        return self

    def addTomato(self) -> bool:
        self.tomato = True
        return self

    def build(self) -> Burger:
        return Burger(self)


burger: Burger = BurgerBuilder(14)\
    .addPepperoni().addLettuce().addTomato().build()

print("size:", burger.size)
print("cheese:", burger.cheese)
print("pepperoni", burger.pepperoni)
print("lettuce", burger.lettuce)
print("tomato", burger.tomato)
