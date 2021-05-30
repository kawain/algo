# 例は、求職者がいくつかの求人情報サイトに登録し
# 一致する仕事があるたびに通知を受ける
# オブジェクト間の依存関係を定義して、
# オブジェクトがその状態を変更するたびに、
# そのすべての依存関係に通知する

class Observer:
    def __init__(self, name="", observers=[]) -> None:
        self.name = name
        self.observers = observers

    def onJobPosted(self, jobObj: "JobPost") -> None:
        print(f"Hi {self.name}! New job posted: {jobObj.getTitle()}")

    def notify(self, jobObj: "JobPost") -> None:
        for observer in self.observers:
            observer.onJobPosted(jobObj)

    def attach(self, observer: "Observer") -> None:
        self.observers.append(observer)

    def addJob(self, jobObj: "JobPost") -> None:
        self.notify(jobObj)


class JobSeeker(Observer):
    def __init__(self, name) -> None:
        super().__init__(name)


class EmploymentAgency(Observer):
    def __init__(self) -> None:
        super().__init__()


class JobPost:
    def __init__(self, title) -> None:
        self.title = title

    def getTitle(self) -> str:
        return self.title


if __name__ == "__main__":
    # Create subscribers
    johnDoe = JobSeeker("John Doe")
    janeDoe = JobSeeker("Jane Doe")

    # Create publisher and attach subscribers
    jobPostings = EmploymentAgency()
    jobPostings.attach(johnDoe)
    jobPostings.attach(janeDoe)

    # Add a new job and see if subscribers get notified
    jobPostings.addJob(JobPost("Software Engineer"))


# Hi John Doe! New job posted: Software Engineer
# Hi Jane Doe! New job posted: Software Engineer
