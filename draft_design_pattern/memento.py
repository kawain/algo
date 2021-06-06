# mementoパターンは、オブジェクトの現在のステート（状態）をキャプチャし、後でスムーズに取り出せる形式で保存します
# mementoパターンは、オブジェクトのステートを以前のステートに戻す（ロールバックによるundo）能力を提供する

# 最初に、エディタのステートを保持できるmementoオブジェクトを記述

class EditorMemento:
    def __init__(self, content: str) -> None:
        self.content: str = content

    def getContent(self) -> str:
        return self.content


# 続いて、mementoオブジェクトを使うエディタ（ここではoriginator）を記述します

class Editor:
    def __init__(self) -> None:
        self.content = ""

    def type(self, words: str) -> None:
        self.content = self.content + ' ' + words

    def getContent(self) -> str:
        return self.content

    def save(self) -> EditorMemento:
        return EditorMemento(self.content)

    def restore(self, memento: EditorMemento) -> None:
        self.content = memento.getContent()


editor = Editor()

# 何か入力する
editor.type('最初の文です。')
editor.type('次の文です。')

# 後で戻したいステートを保存する: 「最初の文です。」「次の文です。」
saved: EditorMemento = editor.save()

# もう少し入力する
editor.type('3番目の文です。')

# Contentを出力して保存
print(editor.getContent())

# 最後に保存したステートに戻す
editor.restore(saved)

print(editor.getContent())
