# singletonパターンは、あるクラスのオブジェクトが常に1つだけ作成されることを保証します
# https://techacademy.jp/magazine/31657

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singletonクラス")
        else:
            Singleton.__instance = self


s0 = Singleton.getInstance()
s1 = Singleton.getInstance()
print(id(s0))
print(id(s1))

# これはエラー
# s3 = Singleton()
# print(s3)
