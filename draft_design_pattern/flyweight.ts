export {};

let objectID = 1;

class KarakTea {
  public objectID = objectID++;
  constructor(public val: string) {}
}

class TeaMaker {
  private availableTea: { [key: string]: KarakTea } = {};
  constructor() {}
  make(preference: string): KarakTea {
    if (!this.availableTea[preference]) {
      this.availableTea[preference] = new KarakTea(preference);
    }
    return this.availableTea[preference];
  }
}

class TeaShop {
  private orders: { [key: number]: KarakTea } = {};
  private teaMaker: TeaMaker;
  constructor(teaMaker: TeaMaker) {
    this.teaMaker = teaMaker;
  }
  takeOrder(teaType: string, table: number) {
    this.orders[table] = this.teaMaker.make(teaType);
  }
  serve() {
    for (const k in this.orders) {
      console.log(
        `テーブル# ${k}にお茶を出す ${this.orders[k].val} , objectID = ${
          this.orders[k].objectID
        }`,
      );
    }
  }
}

const teaMaker = new TeaMaker();
const shop = new TeaShop(teaMaker);

shop.takeOrder("砂糖少なめ", 1);
shop.takeOrder("ミルク多め", 2);
shop.takeOrder("砂糖なし", 5);
shop.takeOrder("砂糖なし", 6);
shop.takeOrder("砂糖少なめ", 7);

shop.serve();
