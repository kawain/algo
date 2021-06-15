# template methodパターンは、特定のアルゴリズムの実行手順の骨格部分を定義します。手順は子クラスで実装します
from abc import ABC, abstractmethod


class Builder(ABC):
    # Template method
    def build(self):
        self.test()
        self.lint()
        self.assemble()
        self.deploy()

    @abstractmethod
    def test(self) -> None:
        pass

    @abstractmethod
    def lint(self) -> None:
        pass

    @abstractmethod
    def assemble(self) -> None:
        pass

    @abstractmethod
    def deploy(self) -> None:
        pass


class AndroidBuilder(Builder):
    def test(self):
        print('Androidのテストを実行')

    def lint(self):
        print('AndroidコードのLintを実行')

    def assemble(self):
        print('Androidビルドのアセンブリを実行')

    def deploy(self):
        print('Androidビルドをサーバーにデプロイ')


class IosBuilder(Builder):
    def test(self):
        print('iOSのテストを実行')

    def lint(self):
        print('iOSコードのLintを実行')

    def assemble(self):
        print('iOSビルドのアセンブリを実行')

    def deploy(self):
        print('iOSビルドをサーバーにデプロイ')


androidBuilder = AndroidBuilder()
androidBuilder.build()

iosBuilder = IosBuilder()
iosBuilder.build()
