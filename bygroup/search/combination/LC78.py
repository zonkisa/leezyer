class Solution:
	def subsets(self, nums):
		res = []
		nums.sort()	# 非必须
		for n in range(len(nums)+1):
			self.dfs(nums, 0, 0, n, [], res)
		return res

	def dfs(self, nums, start, depth, n, path, res):
		# if depth > n:
		# 	return
		if depth == n:
			res.append(path)
			return

		for i in range(start, len(nums)):
			self.dfs(nums, i+1, depth+1, n, path+[nums[i]], res)

	def subsets2(self, nums):
		res = []
		nums.sort()
		self.dfs2(nums, 0, [], res)
		return res

	def dfs2(self, nums, start, path, res):
		res.append(path)

		for i in range(start, len(nums)):
			self.dfs2(nums, i+1, path+[nums[i]], res)

	def subsetsIterate(self, nums):
		res = [[]]
		# nums.sort()
		for num in nums:
			tmp = []
			for item in res:
				tmp += [item + [num]]
			res += tmp
			# print(res)
		return res


if __name__ == "__main__":
	print(Solution().subsets([1, 2, 3]))
	print(Solution().subsets2([1, 2, 3]))
	print(Solution().subsetsIterate([1, 2, 3]))

