# Strategyパターン
# アルゴリズムを実装した部分を交換
# 参照 https://pydp.info/GoF_dp/behavior/21_Strategy/index.html
import strformat


type

  Formatter = ref object of RootObj

  HTMLFormatter = ref object of Formatter
  PlainTextFormatter = ref object of Formatter


  Report = ref object
    title: string
    text: seq[string]
    formatter: Formatter


method outputReport(
  self: Formatter,
  title: string,
  text: seq[string]
){.base, locks: "unknown".} =
  discard


method outputReport(
  self: HTMLFormatter,
  title: string,
  text: seq[string]
){.locks: "unknown".} =
  echo fmt"<html><head><title>{title}</title></head>"
  echo "<body>"
  for v in text:
    echo fmt"<p>{v}</p>"
    echo "</body>"
    echo "</html>"


method outputReport(
  self: PlainTextFormatter,
  title: string,
  text: seq[string]
){.locks: "unknown".} =
  echo fmt"**{title}**"
  for v in text:
    echo fmt" - {v}"




proc outputReport(self: Report) =
  self.formatter.outputReport(self.title, self.text)




proc main() =
  let title = "Monthly report"
  let contents = @["good", "best"]

  # Ouput by Markdown
  let report = Report(
    title: title,
    text: contents,
    formatter: PlainTextFormatter()
  )
  report.outputReport()

  echo "-----"

  # Output by HTML
  let reportHtml = Report(
    title: title,
    text: contents,
    formatter: HTMLFormatter()
  )
  reportHtml.outputReport()



main()
