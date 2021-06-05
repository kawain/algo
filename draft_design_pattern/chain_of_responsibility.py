# Chain of Responsibilityパターンは、
# オブジェクトのチェイン形成を支援します。
# リクエストはチェインの一方から他方へ、
# あるオブジェクトから別のオブジェクトへと進み、
# 適切なハンドラが見つかるまでこれを繰り返します
from abc import ABC


class Account(ABC):
    def __init__(self, balance):
        self.successor = None
        self.balance = balance

    def setNext(self, account: "Account"):
        self.successor = account

    def pay(self, amountToPay):
        if self.canPay(amountToPay):
            print(f"{self.__class__.__name__}で{amountToPay}ドル支払われました。")
        elif self.successor is not None:
            print(f"{self.__class__.__name__}で支払いできません。次の支払い方法に進みます。")
            self.successor.pay(amountToPay)
        else:
            print("残高が十分なアカウントがありません")

    def canPay(self, amount):
        return self.balance >= amount


class Bank(Account):
    def __init__(self, balance):
        super().__init__(balance)


class Paypal(Account):
    def __init__(self, balance):
        super().__init__(balance)


class Bitcoin(Account):
    def __init__(self, balance):
        super().__init__(balance)


bank = Bank(100)
paypal = Paypal(200)
bitcoin = Bitcoin(3000)

bank.setNext(paypal)
paypal.setNext(bitcoin)

bank.pay(2259)
