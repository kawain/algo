# Template Methodパターン
import strformat


type
  AbstractDisplay = ref object of RootObj

  HTMLFormatter = ref object of AbstractDisplay
    title: string
    text: string
  PlainTextFormatter = ref object of AbstractDisplay
    title: string
    text: string



method Start(self: AbstractDisplay){.base, locks: "unknown".} =
  discard

method Processing(self: AbstractDisplay){.base, locks: "unknown".} =
  discard

method End(self: AbstractDisplay){.base, locks: "unknown".} =
  discard

proc Execute(self: AbstractDisplay) =
  self.Start()
  self.Processing()
  self.End()


method Start(self: HTMLFormatter){.locks: "unknown".} =
  echo fmt"<html><head><title>{self.title}</title></head>"

method Processing(self: HTMLFormatter){.locks: "unknown".} =
  echo fmt"<body>{self.text}</body>"

method End(self: HTMLFormatter){.locks: "unknown".} =
  echo "</html>"


method Start(self: PlainTextFormatter){.locks: "unknown".} =
  echo fmt"# {self.title}"

method Processing(self: PlainTextFormatter){.locks: "unknown".} =
  echo fmt"{self.text}"

method End(self: PlainTextFormatter){.locks: "unknown".} =
  echo "---"


proc main() =
  let obj1 = HTMLFormatter(title: "はじめまして", text: "本文です")
  let obj2 = PlainTextFormatter(
    title: "こんにちは",
    text: "プレーンの本文です"
  )

  obj1.Execute()
  obj2.Execute()


main()
