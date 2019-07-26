class Solution:
	def generateParenthesis(self, n):
		res = []
		self.dfs("", n, 0, 0, res)
		return res

	def dfs(self, S, n, left, right, res):
		if len(S) == 2 * n:
			res.append(S)
			return

		if left < n:
			self.dfs(S+"(", n, left+1, right, res)
		if right < left:
			self.dfs(S+")", n, left, right+1, res)


if __name__ == '__main__':
	print(Solution().generateParenthesis(3))
	pass
