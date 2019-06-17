# coding: utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.find.Elementary_Symbol_Tables.SymbolTable import SymbolTable, Node


class BinarySearch(SymbolTable):
    """
    基于有序数组的二分查找
    N个键的有序数组中进行二分查找最多需要1+lgN次比较（无论成功或失败），查询高效
    put方法仍比较慢，向大小为N的有序数组中插入一个新元素在最坏情况下需要~2N次访问数组
    """
    def __init__(self, capacity):
        self.keys = [None] * capacity
        self.vals = [None] * capacity
        self.N = 0

    def size(self):
        return self.N

    def get(self, key):
        if self.isEmpty():
            return None
        i = self.rank(key)
        if i < self.N and self.keys[i] == key: # rank(key)判断给定键排名是否在范围内，再判断是否有该键
            return self.vals[i]
        else:
            return None

    def put(self, key, value):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            self.vals[i] = value
            return
        for j in range(self.N, i, -1): # 未被命中时，添加新键，后面的键值排名+1
            self.keys[j] = self.keys[j-1]
            self.vals[j] = self.vals[j-1]
        self.keys[i] = key
        self.vals[i] = value
        self.N += 1

    def delete(self, key):
        i = self.rank(key)
        if i < self.N and self.keys[i] == key:
            for j in range(i, self.N-1):
                self.keys[i] = self.keys[i+1]
                self.vals[i] = self.vals[i+1]
            self.keys[self.N-1] = None
            self.vals[self.N-1] = None
            self.N -= 1
        # 若该键不存在，这里默认不给提示，避免暴露内部细节

    def select(self, k):
        if k >= self.N:
            return None
        return self.keys[k]

    # 大于等于key的最小键,由rank方法可知取i即可。即使i不在范围或未命中，仍可取到
    def ceiling(self, key):
        i = self.rank(key)
        return self.keys[i]

    # 小于等于key的最大键，需要判断范围以及是否命中
    def floor(self, key):
        i = self.rank(key)
        if i < self.N:
            if self.keys[i] == key:
                return self.keys[i]
            else:
                return self.keys[i-1]
        return self.keys[self.N -1]

    def min(self):
        if self.isEmpty():
            return None
        return self.keys[0]

    def max(self):
        if self.isEmpty():
            return None
        return self.keys[self.N-1]

    # 返回表中小于该键的数量
    def recursiveRank(self, key, lo, hi):
        # 高位索引小于低位索引后停止递归，返回低位排名
        if hi < lo:
            return lo
        mid = lo + (hi - lo) // 2
        if key < self.keys[mid]:
            self.recursiveRank(key, lo, mid-1)
        elif key > self.keys[mid]:
            self.recursiveRank(key, mid+1, hi)
        else:
            return mid

    def rank(self, key):
        lo, hi = 0, self.N-1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self.keys[mid]:
                hi = mid - 1
            if key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        # 最后返回低位索引和recursiveRank的情况相同
        return lo

    def __str__(self):
        res = '{'
        for i in range(self.N):
            res += "{}: {}, ".format(self.keys[i], self.vals[i])

        return res+'}'
        # return dict(zip([str(s) for s in self.keys], [str(s) for s in self.vals]))
