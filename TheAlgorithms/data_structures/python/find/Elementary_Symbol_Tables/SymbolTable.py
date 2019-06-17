# coding: utf-8
from __future__ import print_function


class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next


class SymbolTable:
    def __init__(self):
        pass

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass

    def contains(self, key):
        return self.get(key) != None

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        pass

    def min(self):
        pass

    def max(self):
        pass

    def floor(self, key):
        pass

    def ceiling(self, key):
        pass

    def rank(self, key):
        pass

    def select(self, k):
        pass

    def deleteMin(self):
        pass

    def deleteMax(self):
        pass

    def keys(self, lo, hi):
        pass

    def keys(self):
        pass