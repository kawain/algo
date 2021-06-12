export {};

class EditorMemento {
  constructor(public content: string) {}
  getContent(): string {
    return this.content;
  }
}

class Editor {
  private content = "";
  type(words: string): void {
    this.content = this.content + " " + words;
  }
  getContent(): string {
    return this.content;
  }
  save(): EditorMemento {
    return new EditorMemento(this.content);
  }
  restore(memento: EditorMemento): void {
    this.content = memento.getContent();
  }
}

const editor = new Editor();

// 何か入力する
editor.type("最初の文です。");
editor.type("次の文です。");

// 後で戻したいステートを保存する: 「最初の文です。」「次の文です。」
const saved: EditorMemento = editor.save();

// もう少し入力する
editor.type("3番目の文です。");

// Contentを出力して保存
console.log(editor.getContent());

// 最後に保存したステートに戻す
editor.restore(saved);

console.log(editor.getContent());
