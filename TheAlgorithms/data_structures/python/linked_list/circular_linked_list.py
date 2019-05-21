from __future__ import print_function
from TheAlgorithms.data_structures.python.linked_list.linked_list import Linked_List, Node
""" 
环形链表：也是一条链表，与单链表不同的是环形链表中所有结点的链接/引用都不为空，即至少有一个结点被链接两次
"""


def has_circular(head):
    """
    1.3.29 前序准备，判断链表是否有成环情况
    快慢指针，速度比2:1
    """
    if not head:
        return False
    fast, slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


def is_circular(head):
    """
    1.3.29 前序准备，判断是否为环形链表
    """
    tmp = head
    while tmp.next:
        tmp = tmp.next
        if tmp == head:
            return True

    return False


class LinkedStack():
    """
    1.3.29 平行 用链表实现栈
    """

    def __init__(self):
        self._stack = Linked_List()

    def isEmpty(self):
        return self._stack.isEmpty()

    # len(s)
    def __len__(self):
        return self._stack.size()

    # str(s)
    def __str__(self):
        return "[" + ",".join(map(str, self)) + "]"

    # iter(s) or for item in s
    def __iter__(self):
        tmp_list = []
        tmp = self._stack.Head
        while tmp and tmp.next != self._stack.Head: # 避免环形链干扰
            tmp_list.append(tmp)

        return iter(tmp_list)

    # item in s: return True/False
    def __contains__(self, item):
        return self._stack.find(item)

    # s1 + s2
    def __add__(self, other):
        """
        此处add操作即将A链尾指向B链头
        """
        if other is not None:
            tmp = self._stack.Head
            while tmp.next and tmp.next != self._stack.Head:
                tmp = tmp.next
            tmp.next = other.Head

    # s == anyObject
    def __eq__(self, other):
        t1, t2 = self._stack.Head, other.Head
        while t1 and t2:
            if t1.data == t2.data:
                t1 = t1.next
                t2 = t2.next
            else:
                return False
        if t1 and not t2:
            return False
        if t2 and not t1:
            return False
        return True

    def clear(self):
        self._stack.Head = None

    def peek(self):
        """ 栈顶在链表头部 """
        return self._stack.Head.data

    def push(self, item):
        """ 进栈元素应该在链表头部"""
        node = Node(item)
        tmp = self._stack.Head
        node.next = tmp
        self._stack.Head = node

    def pop(self):
        tmp = self._stack.Head
        self._stack.Head = tmp.next
        tmp.next = None
        return tmp.data


class LinkedQueue():
    """
    1.3.29 用链表实现队列
    """
    pass
