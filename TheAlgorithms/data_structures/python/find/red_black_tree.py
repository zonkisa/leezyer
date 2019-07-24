# coding: utf-8
from __future__ import print_function


RED = True
BLACK = False


class Node(object):
	left = None
	right = None

	def __init__(self, key, val , N, color):
		self.key = key
		self.val = val
		self.N = N
		self.color = color


class RedBlackTree(object):
	def __init__(self):
		pass

	def isRed(self, node: Node):
		if node is None or node.val is None:
			return False

		return node.color == RED


