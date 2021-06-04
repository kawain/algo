# bridgeパターンは、継承ではなくcompositionを優先するためのものです。
# ある階層の実装の詳細は、別の階層にある別のオブジェクトにプッシュされます
from abc import ABCMeta, abstractmethod

# WebPageという階層を設定します


class WebPage(metaclass=ABCMeta):
    def __init__(self, theme: "Theme") -> None:
        self.theme = theme

    @abstractmethod
    def getContent(self) -> str:
        pass


class About(WebPage):
    def __init__(self, theme: "Theme") -> None:
        super().__init__(theme)

    def getContent(self) -> str:
        return self.theme.getColor() + "のAboutページ"


class Careers(WebPage):
    def __init__(self, theme: "Theme") -> None:
        super().__init__(theme)

    def getContent(self) -> str:
        return self.theme.getColor() + "のCareersページ"


# Themeという階層を記述します

class Theme(metaclass=ABCMeta):
    @abstractmethod
    def getColor(self) -> str:
        pass


class DarkTheme(Theme):
    def getColor(self) -> str:
        return 'Dark Black'


class LightTheme(Theme):
    def getColor(self) -> str:
        return 'Off white'


class AquaTheme(Theme):
    def getColor(self) -> str:
        return 'Light blue'


# 2つの階層を次のように使えます

darkTheme = DarkTheme()

about = About(darkTheme)
careers = Careers(darkTheme)

print(about.getContent())
print(careers.getContent())
