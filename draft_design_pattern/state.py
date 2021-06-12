# stateパターンは、ステートの変更に応じてクラスの振る舞いを変更します
from abc import ABC, abstractmethod


class WritingState(ABC):
    @abstractmethod
    def write(self, words: str) -> None:
        pass


class UpperCase(WritingState):
    def write(self, words: str) -> None:
        print(words.upper())


class LowerCase(WritingState):
    def write(self, words: str) -> None:
        print(words.lower())


class Default(WritingState):
    def write(self, words: str) -> None:
        print(words)


class TextEditor:
    def __init__(self, state: WritingState) -> None:
        self.state = state

    def setState(self, state: WritingState) -> None:
        self.state = state

    def type(self, words: str) -> None:
        self.state.write(words)


editor = TextEditor(Default())
editor.type("First line")

editor.setState(UpperCase())
editor.type("Second line")
editor.type("Third line")

editor.setState(LowerCase())
editor.type("Fourth line")
editor.type("Fifth line")
