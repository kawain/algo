import strformat


type
  Account = ref object of RootObj
    name: string
    balance: int
    successor: Account
  Bank = ref object of Account
  Paypal = ref object of Account
  Bitcoin = ref object of Account


method setNext(self: Account, obj: Account) {.base.} =
  self.successor = obj

method canPay(self: Account, amount: int): bool {.base.} =
  self.balance >= amount

method pay(self: Account, amountToPay: int) {.base.} =
  if self.canPay(amountToPay):
    echo fmt"{self.name}で{amountToPay}ドル支払われました。"
  elif self.successor != nil:
    echo fmt"{self.name}で支払いできません。次の支払い方法に進みます。"
    self.successor.pay(amountToPay)
  else:
    echo "残高が十分なアカウントがありません"

let
  bank: Account = Bank(name: "Bank", balance: 100)
  paypal: Account = Paypal(name: "Paypal", balance: 200)
  bitcoin: Account = Bitcoin(name: "Bitcoin", balance: 300)

bank.setNext(paypal)
paypal.setNext(bitcoin)

bank.pay(300)

