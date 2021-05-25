# Strategyがジェネリクス
import strformat


type

  HTMLFormatter = ref object
  PlainTextFormatter = ref object


  Report = ref object
    title: string
    text: seq[string]



proc outputReport(
  self: HTMLFormatter,
  title: string,
  text: seq[string]
) =
  echo fmt"<html><head><title>{title}</title></head>"
  echo "<body>"
  for v in text:
    echo fmt"<p>{v}</p>"
    echo "</body>"
    echo "</html>"



proc outputReport(
  self: PlainTextFormatter,
  title: string,
  text: seq[string]
) =
  echo fmt"**{title}**"
  for v in text:
    echo fmt" - {v}"



proc outputReport[T](self: Report, obj: T) =
  obj.outputReport(self.title, self.text)



proc main() =
  let title = "Monthly report"
  let contents = @["good", "best"]

  # Ouput by Markdown
  let report1 = Report(
    title: title,
    text: contents
  )
  report1.outputReport(PlainTextFormatter())

  echo "-----"

  # Output by HTML
  let report2 = Report(
    title: title,
    text: contents
  )
  report2.outputReport(HTMLFormatter())


main()


