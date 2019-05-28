# coding:utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.sorts.sort_example import Example


class Selection(Example):
    """
    选择排序：不断选择剩余元素中的最小者
    1，找到数组中最小的元素，与数组第一个元素交换位置
    2，在剩下的元素中找到最小的元素，与数组第二个元素交换位置

    N²/2比较和N次交换
    运行时间和输入无关，输入有序、无序时间相同
    交换次数最少，与数组大小是线性关系
    """
    def sort(self, collection):
        N = len(collection)
        for i in range(N):
            min_index = i
            for j in range(i+1, N):
                if self.less(collection[j], collection[min_index]):
                    min_index = j
            self.exch(collection, i, min_index)

        return collection


class Insertion(Example):
    """
    插入排序：将每一个元素插入到其他已经有序的元素中的适当位置。
    为了给要插入的元素腾出空间，需要将其余所有元素在插入前右移一位。
    与选择排序一致，当前索引左边的所有元素有序，右边位置不确定。

    对于随机排列的长度为N且主键不重复的数组，
    平均N²/4次比较+平均N²/4次交换，最坏平均N²/2次比较+平均N²/2次交换，最优N-1次比较+0次交换
    运行时间取决于输入的初始顺序
    有序情况下只要比较，无需交换
    插入排序能在线性时间内发现数组是否有序，由于<=符号，元素全部相同情况也是如此。
    """
    def sort(self, collection):
        N = len(collection)
        for i in range(1, N):
            j = i
            while j > 0 and self.less(collection[j], collection[j-1]):
                j -= 1
                self.exch(collection, j, j-1)

        return collection



