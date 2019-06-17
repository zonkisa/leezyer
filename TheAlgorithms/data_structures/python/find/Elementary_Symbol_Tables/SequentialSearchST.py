# coding: utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.find.Elementary_Symbol_Tables.SymbolTable import SymbolTable, Node


class SequentialSearchST(SymbolTable):
    """
    基于无序链表的顺序查找
    """
    def __init__(self):
        self.head = None

    def get(self, key):
        tmp = self.head
        while tmp:
            if tmp.key == key:
                return tmp.value
            else:
                tmp = tmp.next

        return None

    def put(self, key, value):
        tmp = self.head
        while tmp:
            if tmp.key == key:
                tmp.value = value
                return
            else:
                tmp = tmp.next
        first = Node(key, value, self.head)
