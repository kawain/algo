type
  Theme = ref object of RootObj

  DarkTheme = ref object of Theme
  LightTheme = ref object of Theme
  AquaTheme = ref object of Theme


  WebPage = ref object of RootObj
    theme: Theme
  About = ref object of WebPage
  Careers = ref object of WebPage


method getColor(self: Theme): string {.base, locks: "unknown".} =
  discard

method getColor(self: DarkTheme): string {.locks: "unknown".} =
  "Dark Black"

method getColor(self: LightTheme): string {.locks: "unknown".} =
  "Off white"

method getColor(self: AquaTheme): string {.locks: "unknown".} =
  "Light blue"


method getContent(self: WebPage): string {.base, locks: "unknown".} =
  discard

method getContent(self: About): string {.locks: "unknown".} =
  self.theme.getColor() & "のAboutページ"

method getContent(self: Careers): string {.locks: "unknown".} =
  self.theme.getColor() & "のCareersページ"


proc main() =
  let darkTheme = DarkTheme()

  let about = About(theme: darkTheme)
  let careers = Careers(theme: darkTheme)

  echo about.getContent()
  echo careers.getContent()


main()
