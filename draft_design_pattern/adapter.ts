export {};

interface Lion {
  roar(): void;
}

class AfricanLion implements Lion {
  roar(): void {
    console.log("がお");
  }
}

class AsianLion implements Lion {
  roar(): void {
    console.log("ぐう");
  }
}

class Hunter {
  hunt(lion: Lion): void {
    lion.roar();
  }
}

class WildDog {
  bark(): void {
    console.log("わん");
  }
}

class WildDogAdapter implements Lion {
  constructor(private dog: WildDog) {}
  roar(): void {
    this.dog.bark();
  }
}

// ハンター
const hunter = new Hunter();

// 普通のLionインターフェイス
const obj1 = new AfricanLion();
hunter.hunt(obj1);
const obj2 = new AsianLion();
hunter.hunt(obj2);

// Lionインターフェイスの WildDogAdapter に WildDog オブジェクトを持たせる
const wildDog = new WildDog();
const wildDogAdapter = new WildDogAdapter(wildDog);

// LionインターフェイスになったのでHunterのhuntができる
hunter.hunt(wildDogAdapter);
