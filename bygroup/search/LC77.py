class Solution:

	def combine1(self, n: int, k: int):
		res = []
		self.dfs1(n + 1, k, 1, 0, [], res)
		return res

	def dfs1(self, n, k, start, depth, path, res):
		if depth == k:
			res.append(path[:])
			return
		for i in range(start, n):
			path.append(i)
			self.dfs1(n, k, i + 1, depth + 1, path, res)
			path.pop()

	def combine2(self, n: int, k: int):
		res = []
		self.dfs2(n + 1, k, 1, 0, [], res)
		return res

	def dfs2(self, n, k, start, depth, path, res):
		if depth == k:
			res.append(path)
			return
		for i in range(start, n - (k - len(path)) + 1):
			self.dfs2(n, k, i + 1, depth + 1, path + [i], res)

