# coding: utf-8
from __future__ import print_function


class HeapSort:
    """
    基于最大堆的堆排序
    2NlgN次比较和恒定的额外空间（即数组本身）
    无法利用缓存
    """

    def sort(self, pq):
        N = len(pq)
        # 第一个循环是构造最大堆，自底向上的下沉操作，使得每个根结点都是当前子树的最大值，以此重复
        for k in range(N, 0, -1):
            self.sink(pq, k, N)

        # 排序在第二个循环，首先将上述构造的最大堆的根结点移动到末尾，N-=1，自顶向下的下沉操作使得次大元素移动到堆顶，以此重复
        while N > 1:
            self.exch(pq, 1, N)
            N -= 1
            self.sink(pq, 1, N)

    def sink(self, pq, k, N):
        while 2 * k <= N:
            j = 2 * k
            if j < N and self.less(pq, j, j+1):
                j += 1
            if self.less(pq, k, j):
                self.exch(pq, k, j)
                k = j
            else:
                break

    @staticmethod
    def less(pq, i, j):
        """
        这里索引进来减1，是由于N是容量，不是最后一位元素的索引，参考优先队列中的N
        """
        return pq[i-1] < pq[j-1]

    @staticmethod
    def exch(pq, i, j):
        swap = pq[i-1]
        pq[i-1] = pq[j-1]
        pq[j-1] = swap
