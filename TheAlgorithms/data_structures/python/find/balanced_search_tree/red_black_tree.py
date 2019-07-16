# coding: utf-8
from __future__ import print_function


RED, BLACK = True, False


class Node(object):
    left = None
    right = None

    def __init__(self, key, val, N, color):
        self.key = key
        self.val = val
        self.N = N
        self.color = color

    def isRed(self) -> object:
        return self.color == RED


class RedBlackBST(object):

    def __init__(self):
        self.root = Node(None, None, 0, False)

    def isRed(self, node: Node):
        return node.isRed()

    def size(self):
        return self.getSize(self.root)

    def getSize(self, node):
        if node is None or node.key is None:
            return 0
        else:
            return node.N

    def rotateLeft(self, node: Node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        x.N = node.N
        node.N = 1 + self.getSize(node.left) + self.getSize(node.right)
