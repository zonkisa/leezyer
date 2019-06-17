# coding:utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.sorts.sort_models import Selection, Insertion, Shell, Merge, Quick
from time import perf_counter_ns
from random import randint
import math, random


class SortCompare:

    @staticmethod
    def algTime(alg, collection):
        start = perf_counter_ns()/1000 # 微秒
        if alg == "Insertion":
            Insertion().sort3(collection)
        if alg == "Selection":
            Selection().sort(collection)
        if alg == "Shell":
            Shell().sort(collection)
        if alg == "Merge":
            Merge().sort5(collection)
        if alg == "Quick":
            Quick().sort4(collection)
        # if alg == "Heap":
        #     Heap().sort(collection)
        return perf_counter_ns()/1000 - start

    def timeRandomInput(self, alg, N, T):
        total = 0.0
        collection = [0] * N
        for i in range(T):
            for j in range(N):
                collection[j] = randint(0, N-1)
            total += self.algTime(alg, collection)

        return total

    def cmpRes(self, alg1, alg2, N, T):
        t1 = self.timeRandomInput(alg1, N, T)
        t2 = self.timeRandomInput(alg2, N, T)
        print("{} is {} times faster than {}".format(alg1, round(t2/t1, 2), alg2))


def p(x, y):
    return int(math.pow(x, y))


# dropped， 归并中插入排序的小规模因子不应超过lgN
def testMergeInsertSort(N, T, factor):
    total = 0.0
    collection = [0] * N
    for i in range(T):
        for j in range(N):
            collection[j] = randint(0, N - 1)
            start = perf_counter_ns() / 1000  # 微秒
            Merge().sort5(collection)
            total += perf_counter_ns() / 1000 - start

    print(Merge().isSorted(collection))
    return total


def testQuickSort(t, N, sor):
    total = 0.0
    for i in range(N):
        random.shuffle(t)
        start = perf_counter_ns() / 1000
        if sor == "sort":
            Quick().sort(t)
        else:
            Quick().sort4(t)
        end = perf_counter_ns() / 1000
        total += end - start
    return total


if __name__ == '__main__':
    # t = [5, 4, 3, 2, 7, 6, 1, 8, 888, 88, 999, 9]
    # t = [5, 4, 3, 2, 1, 6, 7, 8, 88, 99, 999]
    t = [5, 4, 4, 5, 4, 5, 4, 5, 4, 5, 4, 3, 4, 5, 6, 4, 5, 4]
    # Selection().sort(t)

    # Insertion().sort(t)
    # Insertion().sort2(t)
    # Insertion().sort3(t)

    # SortCompare().cmpRes("Insertion", "Selection", 1000, 100)
    # print(SortCompare().timeRandomInput("Shell", p(2, 7), 10))
    # print(SortCompare().timeRandomInput("Shell", p(2, 8), 10))
    # print(SortCompare().timeRandomInput("Shell", p(2, 9), 10))
    # print(SortCompare().timeRandomInput("Shell", p(2, 10), 10))

    # print(Merge().sort5(t))
    # print(t)
    # print(testMergeInsertSort(1000, 10, 5))
    # print(testMergeInsertSort(1000, 10, 10))
    # print(testMergeInsertSort(1000, 10, 20))
    # print(testMergeInsertSort(1000, 10, 50))
    # print(testMergeInsertSort(1000, 1, 100))

    # print(Quick()._partition(t, 0, len(t)-1))
    # print(testQuickSort(t, 1000, "sort"))
    # print(testQuickSort(t, 1000, "sort4"))
    # testQuickSort(t, 1000, "sort4")
    # Quick().sort4(t)
    print(t)

    SortCompare().cmpRes("Quick", "Merge", 1000, 100)

