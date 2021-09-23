# 変換するパターン
# 充電器 --- コンセント(国内)
# 充電器 --- 変換プラグ --- コンセント(海外)
from abc import ABC, abstractmethod


class I国内充電器(ABC):
    @abstractmethod
    def get電力(self):
        pass


class I海外充電器(ABC):
    @abstractmethod
    def get海外電力(self):
        pass


class 国内充電器(I国内充電器):
    def get電力(self):
        print("電力")


class 海外充電器(I海外充電器):
    def get海外電力(self):
        print("海外電力")


class 国内コンセント:
    def __init__(self, obj: I国内充電器):
        obj.get電力()


class 海外コンセント:
    def __init__(self, obj: I海外充電器):
        obj.get海外電力()


class 変換プラグ(I海外充電器):
    def __init__(self, obj: I国内充電器):
        self.obj = obj

    def get海外電力(self):
        return self.obj.get電力()


国内コンセント(国内充電器())

henkan = 変換プラグ(国内充電器())
海外コンセント(henkan)
