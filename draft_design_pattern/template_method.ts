export {};

abstract class Builder {
  // Template method
  build(): void {
    this.test();
    this.lint();
    this.assemble();
    this.deploy();
  }

  abstract test(): void;
  abstract lint(): void;
  abstract assemble(): void;
  abstract deploy(): void;
}

class AndroidBuilder extends Builder {
  test() {
    console.log("Androidのテストを実行");
  }

  lint() {
    console.log("AndroidコードのLintを実行");
  }

  assemble() {
    console.log("Androidビルドのアセンブリを実行");
  }

  deploy() {
    console.log("Androidビルドをサーバーにデプロイ");
  }
}

class IosBuilder extends Builder {
  test() {
    console.log("iOSのテストを実行");
  }

  lint() {
    console.log("iOSコードのLintを実行");
  }

  assemble() {
    console.log("iOSビルドのアセンブリを実行");
  }

  deploy() {
    console.log("iOSビルドをサーバーにデプロイ");
  }
}

const androidBuilder = new AndroidBuilder();
androidBuilder.build();

const iosBuilder = new IosBuilder();
iosBuilder.build();
