export {};

interface SortStrategy {
  sort(dataset: number[]): number[];
}

class BubbleSortStrategy implements SortStrategy {
  sort(dataset: number[]): number[] {
    console.log("バブルソートを実行");
    return dataset;
  }
}

class QuickSortStrategy implements SortStrategy {
  sort(dataset: number[]): number[] {
    console.log("クイックソートを実行");
    return dataset;
  }
}

class Sorter {
  constructor(private sorter: SortStrategy) {}
  sort(dataset: number[]): number[] {
    return this.sorter.sort(dataset);
  }
}

const dataset = [1, 5, 4, 3, 2, 8];

let sorter = new Sorter(new BubbleSortStrategy());
sorter.sort(dataset);

sorter = new Sorter(new QuickSortStrategy());
sorter.sort(dataset);
