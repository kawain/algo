type
  EditorMemento = ref object
    content: string

  Editor = ref object
    content: string


proc getContent(self: EditorMemento): string =
  self.content


proc type(self: Editor, words: string) =
  self.content = self.content & " " & words

proc getContent(self: Editor): string =
  self.content

proc save(self: Editor): EditorMemento =
  EditorMemento(content: self.content)

proc restore(self: Editor, memento: EditorMemento) =
  self.content = memento.getContent()


proc main() =
  let editor = Editor()

  # 何か入力する
  editor.type("最初の文です。")
  editor.type("次の文です。")

  # 後で戻したいステートを保存する: 「最初の文です。」「次の文です。」
  let saved: EditorMemento = editor.save()

  # もう少し入力する
  editor.type("3番目の文です。")

  # Contentを出力して保存
  echo editor.getContent()

  # 最後に保存したステートに戻す
  editor.restore(saved)

  echo editor.getContent()


main()
