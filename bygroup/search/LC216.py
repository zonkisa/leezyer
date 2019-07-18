"""
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
	def combinationSum3(self, k, n):
		res = []
		self.dfs(n, 1, 0, k, [], res)
		return res

	def dfs(self, target, start, depth, n, path, res):
		if depth == n:
			if target == 0:
				res.append(path[:])
				return

		for i in range(start, 10):
			if i > target:
				return
				# break
			path.append(i)
			self.dfs(target-i, i+1, depth+1, n, path, res)
			path.pop()


if __name__ == '__main__':
	print(Solution().combinationSum3(3, 9))
	print(Solution().combinationSum3(3, 7))
	pass