export {};

interface WritingState {
  write(words: string): void;
}

class UpperCase implements WritingState {
  write(words: string): void {
    console.log(words.toUpperCase());
  }
}

class LowerCase implements WritingState {
  write(words: string): void {
    console.log(words.toLowerCase());
  }
}

class Default implements WritingState {
  write(words: string): void {
    console.log(words);
  }
}

class TextEditor {
  constructor(private state: WritingState) {}
  setState(state: WritingState): void {
    this.state = state;
  }
  type(words: string): void {
    this.state.write(words);
  }
}

const editor = new TextEditor(new Default());
editor.type("First line");

editor.setState(new UpperCase());
editor.type("Second line");
editor.type("Third line");

editor.setState(new LowerCase());
editor.type("Fourth line");
editor.type("Fifth line");
