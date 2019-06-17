# coding: utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.sorts.priority_queue.MaxPQTemplate import PriorityQueueInArray, PriorityQueueInHeap, IndexMaxPQ
from TheAlgorithms.data_structures.python.sorts.priority_queue.heap_sort import HeapSort
import random


def getInput():
    N = random.randint(0, 10)
    t = []
    for i in range(N):
        t.append(random.randint(0, 10))
    return t


def testPriorityQueueInArray():
    inputs = getInput()
    M = 5
    while len(inputs) <= M:
        inputs += getInput()
    pq = PriorityQueueInArray(inputs)
    print("init inputs list is ", inputs)
    while pq.size() > M:
        m = pq.delMax()
        print(m)
    print("size is ", pq.size())
    print("result list is ", inputs)


def testPriorityQueueInHeap(k, insert, delete):
    pq = PriorityQueueInHeap(k)
    print("init --> ", pq)
    for i in range(insert):
        r = random.randint(0, k)
        pq.insert(r)
    print("after insert --> ", pq)

    for i in range(delete):
        pq.delMax()
    print("after delete --> ", pq)


def testIndexMaxPQ():
    # strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"]
    strings = [2, 3, 3, 4, 2, 5, 8, 7, 6, 9]
    pq = IndexMaxPQ(len(strings))
    print("init ---------> ")
    print(pq)
    for i, key in enumerate(strings):
        pq.insert(i, key)
    print("after insert --------->\n ", pq)
    #
    for i in range(len(strings)):
        if random.random() < 0.5:
            pq.increaseKey(i, 2 * strings[i])
        else:
            pq.decreaseKey(i, strings[i] // 2)
    print("after increaseKey --------->\n ", pq)


if __name__ == '__main__':
    # testPriorityQueueInArray()
    # testPriorityQueueInHeap(10, 7, 2)
    # testIndexMaxPQ()
    a = [8, 9, 7, 6, 5, 2, 3, 10, 4, 1, -1]
    HeapSort().sort(a)
    print(a)
    print("ok")
