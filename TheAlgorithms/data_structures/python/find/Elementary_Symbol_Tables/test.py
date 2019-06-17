# coding: utf-8
from __future__ import print_function
import random
from TheAlgorithms.data_structures.python.find.Elementary_Symbol_Tables.binary_search import BinarySearch
from TheAlgorithms.data_structures.python.find.Elementary_Symbol_Tables.binary_search_tree import BinarySearchTree


if __name__ == '__main__':
    bs = BinarySearch(10)
    bs.put(1, 2)
    print(bs)

    bst = BinarySearchTree()
    bst.put(5, 55)
    bst.put(2, 22)
    bst.put(1, 11)
    # bst.put(3, 33)
    bst.put(6, 66)
    bst.put(7, 77)
    bst.put(9, 99)
    # bst.put(5, 555)
    print(bst)
    print(bst.MyRecursiveFloor(6.5))
    print(bst.floor(6.5))
    print(bst.ceiling(0))
    print(bst.size())
    print(bst.select(5))
    print(bst.rank(1))



