import strutils


type
  WritingState = ref object of RootObj
  UpperCase = ref object of WritingState
  LowerCase = ref object of WritingState
  Default = ref object of WritingState

  TextEditor = ref object
    state: WritingState


method write(self: WritingState, words: string) {.base, locks: "unknown".} =
  discard

method write(self: UpperCase, words: string) {.locks: "unknown".} =
  echo words.toUpper()

method write(self: LowerCase, words: string) {.locks: "unknown".} =
  echo words.toLower()

method write(self: Default, words: string) {.locks: "unknown".} =
  echo words


proc setState(self: TextEditor, state: WritingState) =
  self.state = state

proc type(self: TextEditor, words: string) =
  self.state.write(words)


proc main() =
  let editor = TextEditor(state: Default())
  editor.type("First line")

  editor.setState(UpperCase())
  editor.type("Second line")
  editor.type("Third line")

  editor.setState(LowerCase())
  editor.type("Fourth line")
  editor.type("Fifth line")


main()
