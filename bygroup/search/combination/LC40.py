class Solution:
	def combinationSum2(self, candidates, target):
		res = []
		candidates.sort()
		self.dfs(candidates, target, 0, [], res)
		return res

	def dfs(self, candidates, target, start, path, res):
		if target == 0:
			res.append(path)
			return

		for i in range(start, len(candidates)):
			if candidates[i] > target:
				break
			if i > start and candidates[i] == candidates[i - 1]:
				continue
			self.dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
