export {};

class Sheep {
  constructor(public name: string, public category: string = "オオツノヒツジ") {}
  setName(name: string): void {
    this.name = name;
  }
  getName(): string {
    return this.name;
  }
  setCategory(category: string): void {
    this.category = category;
  }
  getCategory(): string {
    return this.category;
  }
}

const original = new Sheep("ジョリー");
console.log(original.getName());
console.log(original.getCategory());

console.log("---");

// 参照
const reference = original;
reference.setName("ジョリー参照");
console.log(reference.getName());
console.log(original.getName());

console.log("---");

// コピー
// const cloned = JSON.parse(JSON.stringify(original));
// const cloned = { ...original };
const cloned = Object.create(original);
original.setName("オリジナル名");
original.setCategory("オリジナルカテゴリ");
cloned.setName("コピー名");
cloned.setCategory("コピーカテゴリ");
console.log(cloned.getName());
console.log(cloned.getCategory());

console.log("---");

console.log(original.getName());
console.log(original.getCategory());
