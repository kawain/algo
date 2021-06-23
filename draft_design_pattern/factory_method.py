# インスタンス化ロジックを子クラスに委任する方法
# あるクラスに何らかの一般的な処理があるが、
# 実行時にサブクラスを動的に決定する必要がある場合に便利です。
# 言い換えると、サブクラスで必要になりそうなものを
# クライアントが正確には知らない（または知る必要がない）場合です。
from abc import ABCMeta, abstractmethod


class Interviewer(metaclass=ABCMeta):
    @abstractmethod
    def askQuestions(self) -> None:
        pass


class Developer(Interviewer):
    def askQuestions(self) -> None:
        print("デザインパターンについて尋ねる")


class CommunityExecutive(Interviewer):
    def askQuestions(self) -> None:
        print("コミュニティ育成について尋ねる")


class HiringManager(metaclass=ABCMeta):
    @abstractmethod
    def makeInterviewer(self) -> Interviewer:
        """Factory method"""
        pass

    def takeInterview(self) -> None:
        interviewer = self.makeInterviewer()
        interviewer.askQuestions()


class DevelopmentManager(HiringManager):
    def makeInterviewer(self) -> Interviewer:
        return Developer()


class MarketingManager(HiringManager):
    def makeInterviewer(self) -> Interviewer:
        return CommunityExecutive()


devManager = DevelopmentManager()
devManager.takeInterview()

marketingManager = MarketingManager()
marketingManager.takeInterview()
