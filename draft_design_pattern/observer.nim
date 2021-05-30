# 例は、求職者がいくつかの求人情報サイトに登録し
# 一致する仕事があるたびに通知を受ける
# オブジェクト間の依存関係を定義して、
# オブジェクトがその状態を変更するたびに、
# そのすべての依存関係に通知する
import strformat


type
  Observer = ref object of RootObj
    name: string
    observers: seq[Observer]

  JobSeeker = ref object of Observer
  EmploymentAgency = ref object of Observer

  JobPost = ref object
    title: string


proc getTitle(self: JobPost): string =
  result = self.title


proc onJobPosted(self: Observer, jobObj: JobPost) =
  echo fmt"Hi {self.name}! New job posted: {jobObj.getTitle()}"


proc notify(self: Observer, jobObj: JobPost) =
  for observer in self.observers:
    observer.onJobPosted(jobObj)


proc attach(self: Observer, observer: Observer) =
  self.observers.add(observer)


proc addJob(self: Observer, jobObj: JobPost) =
  self.notify(jobObj)


proc main() =
  # Create subscribers
  let johnDoe = JobSeeker(name: "John Doe")
  let janeDoe = JobSeeker(name: "Jane Doe")

  # Create publisher and attach subscribers
  let jobPostings = EmploymentAgency()
  jobPostings.attach(johnDoe)
  jobPostings.attach(janeDoe)

  # Add a new job and see if subscribers get notified
  jobPostings.addJob(JobPost(title: "Software Engineer"))


main()


# Hi John Doe! New job posted: Software Engineer
# Hi Jane Doe! New job posted: Software Engineer
