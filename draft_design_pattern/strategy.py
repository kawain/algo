# strategyパターンを使うことで、状況に応じてアルゴリズムや戦略を切り替えられます
from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: list[int]) -> list[int]:
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset: list[int]) -> list[int]:
        print("バブルソートを実行")
        return dataset


class QuickSortStrategy(SortStrategy):
    def sort(self, dataset: list[int]) -> list[int]:
        print("クイックソートを実行")
        return dataset


class Sorter:
    def __init__(self, sorter: SortStrategy) -> None:
        self.sorter = sorter

    def sort(self, dataset: list[int]) -> list[int]:
        return self.sorter.sort(dataset)


dataset = [1, 5, 4, 3, 2, 8]

sorter = Sorter(BubbleSortStrategy())
sorter.sort(dataset)

sorter = Sorter(QuickSortStrategy())
sorter.sort(dataset)
