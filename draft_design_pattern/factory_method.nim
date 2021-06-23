type
  Interviewer = ref object of RootObj
  Developer = ref object of Interviewer
  CommunityExecutive = ref object of Interviewer

  HiringManager = ref object of RootObj
    interviewer: Interviewer
  DevelopmentManager = ref object of HiringManager
  MarketingManager = ref object of HiringManager


method askQuestions(self: Interviewer) {.base, locks: "unknown".} =
  discard

method askQuestions(self: Developer) {.locks: "unknown".} =
  echo "デザインパターンについて尋ねる"

method askQuestions(self: CommunityExecutive) {.locks: "unknown".} =
  echo "コミュニティ育成について尋ねる"


method makeInterviewer(
  self: HiringManager
): Interviewer{.base, locks: "unknown".} =
  discard


proc takeInterview(self: HiringManager) =
  let interviewer = self.makeInterviewer()
  interviewer.askQuestions()


method makeInterviewer(
  self: DevelopmentManager
): Interviewer{.locks: "unknown".} =
  return Developer()


method makeInterviewer(
  self: MarketingManager
): Interviewer{.locks: "unknown".} =
  return CommunityExecutive()


proc main() =
  let devManager = DevelopmentManager()
  devManager.takeInterview()

  let marketingManager = MarketingManager()
  marketingManager.takeInterview()


main()
