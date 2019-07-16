class Solution:
	def combinationSum(self, candidates, target):
		"""
		:param candidates: List[int]
		:param target: int
		:return: List[List[int]]
		"""
		res = []
		candidates.sort()
		self.dfs(candidates, target, 0, [], res)
		return res

	def dfs(self, candidates, target, index, path, res):
		if target == 0:
			res.append(path)
			return
		for i in range(index, len(candidates)):
			if candidates[i] > target:
				break
			self.dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)

	# 按返回路径的大小返回
	def combinationSumBFS(self, candidates, target):
		res = []
		candidates.sort()
		for n in range(1, target // candidates[0] + 1):
			self.dfs2(candidates, target, 0, 0, n, [], res)
		return res


	def dfs2(self, candidates, target, start, depth, n, path, res):
		# print(candidates, target, start, depth, n, path, res)
		if depth > n:
			return
		if depth == n:
			if target == 0:
				res.append(path)
				return

		for i in range(start, len(candidates)):
			if candidates[i] > target:
				break
			self.dfs2(candidates, target-candidates[i], i, depth+1, n, path+[candidates[i]], res)
			# if path: path.pop()


if __name__ == "__main__":
	print(Solution().combinationSum([2, 3, 5, 7], 7))
	print(Solution().combinationSumBFS([2, 3, 6, 7], 7))
	pass
