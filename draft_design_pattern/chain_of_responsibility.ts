abstract class Account {
  private balance: number
  private objNext!: Account

  constructor(balance: number) {
    this.balance = balance
  }

  setNext(obj: Account): void {
    this.objNext = obj
  }

  pay(amountToPay: number): void {
    if (this.canPay(amountToPay)) {
      console.log(`${this.constructor.name}で${amountToPay}ドル支払われました。`)
    } else if (this.objNext) {
      console.log(`${this.constructor.name}で支払いできません。次の支払い方法に進みます。`)
      this.objNext.pay(amountToPay)
    } else {
      console.log("残高が十分なアカウントがありません")
    }
  }

  canPay(amount: number): boolean {
    return this.balance >= amount
  }
}

class Bank extends Account {
  constructor(balance: number) {
    super(balance)
  }
}

class Paypal extends Account {
  constructor(balance: number) {
    super(balance)
  }
}

class Bitcoin extends Account {
  constructor(balance: number) {
    super(balance)
  }
}

let obj1 = new Bank(100)
let obj2 = new Paypal(200)
let obj3 = new Bitcoin(3000)

obj1.setNext(obj2)
obj2.setNext(obj3)

obj1.pay(2209)
