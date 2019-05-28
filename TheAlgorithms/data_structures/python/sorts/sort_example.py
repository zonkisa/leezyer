# coding:utf-8
from __future__ import print_function
from operator import le
"""
排序是将一组对象按照某种逻辑顺序重新排列的过程
排序算法性能：
    运行时间，关注于计算比较和交换的数量，对于不交换的算法，则计算访问数组的次数
    内存使用，原地排序算法：除了函数调用所需的栈和固定数目的实例变量之外无需额外内存
             其他排序算法：需要额外内存空间来存储一份数组副本

"""


class Example:
    def __init__(self):
        pass

    def sort(self, collection):
        pass

    @staticmethod
    def less(v, w):
        return v <= w
        # return le(v, w)

    @staticmethod
    def exch(collection, i, j):
        tmp = collection[i]
        collection[i] = collection[j]
        collection[j] = tmp

    @staticmethod
    def show(collection):
        for a in collection:
            print(a, end=" ")

    def isSorted(self, collection):
        for i in range(1, len(collection)):
            if self.less(collection[i], collection[i-1]):
                return False

        return True

