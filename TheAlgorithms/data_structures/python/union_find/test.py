# coding:utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.union_find.union_find import QuickFind, QuickUnion, WeightedQuickUnion, PathCompressedWeightedQuickUnion
from time import perf_counter_ns


if __name__ == '__main__':
    ob = QuickFind(10)
    print("initial id list is %s" % ",".join([str(x) for x in ob.ids]))

    # ls = [
    #     (4, 3),
    #     (3, 8),
    #     (6, 5),
    #     (9, 4),
    #     (2, 1),
    #     (8, 9),
    #     (5, 0),
    #     (7, 2),
    #     (6, 1),
    #     (1, 0),
    #     (6, 7)
    # ]
    ls = []
    i = 0
    for line in open("C:\\zonnoz\\develop\\data\\algs4-data\\algs4-data\\largeUF.txt", "r"):
        lines = line.strip("\n").split(" ")

        if i == 0:
            ob = PathCompressedWeightedQuickUnion(int(lines[0]))
            i += 1
        else:
            ls.append((int(lines[0]), int(lines[1])))

    start = perf_counter_ns()/1000
    # print(ls)
    # print("initial id list is %s" % ",".join([str(x) for x in ob.ids]))
    for (p, v) in ls:
        # print(p, v)
        # print("{} and {} is connected? {}".format(p, v, str(ob.connected(p, v))))
        if not ob.connected(p, v):
            ob.union(p, v)
        # print("{} and {} is connected? {}".format(p, v, str(ob.connected(p, v))))
        # print("----------------------")
    end = perf_counter_ns()/1000

    print(end - start)