# coding:utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.sorts.sort_models import Selection, Insertion, Shell
from time import perf_counter_ns
from random import randint
import math


class SortCompare:

    @staticmethod
    def algTime(alg, collection):
        start = perf_counter_ns()/1000 # 微秒
        if alg == "Insertion":
            Insertion().sort(collection)
        if alg == "Selection":
            Selection().sort(collection)
        if alg == "Shell":
            Shell().sort(collection)
        # if alg == "Merge":
        #     Merge().sort(collection)
        # if alg == "Quick":
        #     Quick().sort(collection)
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


if __name__ == '__main__':
    t = [5, 4, 3, 2, 7, 6, 1]
    print(Selection().sort(t))
    print(Insertion().sort(t))
    print(Insertion().sort2(t))
    print(Insertion().sort3(t))
    # SortCompare().cmpRes("Insertion", "Selection", 1000, 100)
    print(SortCompare().timeRandomInput("Shell", p(2, 7), 10))

    print(SortCompare().timeRandomInput("Shell", p(2, 8), 10))
    print(SortCompare().timeRandomInput("Shell", p(2, 9), 10))
    print(SortCompare().timeRandomInput("Shell", p(2, 10), 10))

