class Solution:
	def permute(self, nums):
		N = len(nums)
		res = []
		self.dfs(nums, 0, N, [False]*N, [], res)
		return res

	def dfs(self, nums, depth, n, used, path, res):
		if depth == n:
			res.append(path[:])
			return

		for i in range(len(nums)):
			if used[i]: continue
			used[i] = True
			path.append(nums[i])
			self.dfs(nums, depth+1, n, used, path, res)
			path.pop()
			used[i] = False

	def permuteBFS(self, nums):
		res = [[]]
		for num in nums:
			tmp = []
			for ls in res:
				for i in range(len(ls)+1):
					tmp.append(ls[:i] + [num] + ls[i:])
			res = tmp
		return res


if __name__ == '__main__':
	print(Solution().permute([1, 2, 3]))
	print(Solution().permuteBFS([1, 2, 3]))

