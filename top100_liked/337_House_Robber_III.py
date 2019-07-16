# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def rob(self, root):
		return self.dfs(root)[1]

	def dfs(self, node):
		if not node:
			return [0, 0]
		robleft = self.dfs(node.left)
		robright = self.dfs(node.right)
		notcurr = robleft[1] + robright[1]
		robcurr = max(robleft[0] + robright[0] + node.val, notcurr)
		return [notcurr, robcurr]

	def rob2(self, root):
		res = []
		a = self.dfs2(root, res)[1]
		print(res)
		return a

	def dfs2(self, node, res):
		if not node:
			return [0, 0]
		robleft = self.dfs2(node.left, res)
		robright = self.dfs2(node.right, res)
		notcurr = robleft[1] + robright[1]
		robcurr = max(robleft[0] + robright[0] + node.val, notcurr)
		res.append([notcurr, robcurr])
		return [notcurr, robcurr]


node = TreeNode(1)
node.left = TreeNode(20)
node.right = TreeNode(3)
node.left.left = TreeNode(40)
node.right.left = TreeNode(5)

print(Solution().rob(node))
