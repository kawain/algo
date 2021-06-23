export {};

interface Interviewer {
  askQuestions(): void;
}

class Developer implements Interviewer {
  askQuestions(): void {
    console.log("デザインパターンについて尋ねる");
  }
}

class CommunityExecutive implements Interviewer {
  askQuestions(): void {
    console.log("コミュニティ育成について尋ねる");
  }
}

abstract class HiringManager {
  abstract makeInterviewer(): Interviewer;
  public takeInterview(): void {
    const interviewer = this.makeInterviewer();
    interviewer.askQuestions();
  }
}

class DevelopmentManager extends HiringManager {
  makeInterviewer(): Interviewer {
    return new Developer();
  }
}
class MarketingManager extends HiringManager {
  makeInterviewer(): Interviewer {
    return new CommunityExecutive();
  }
}

const devManager = new DevelopmentManager();
devManager.takeInterview();

const marketingManager = new MarketingManager();
marketingManager.takeInterview();
