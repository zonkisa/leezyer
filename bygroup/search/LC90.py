class Solution:

	def subsetsWithDup(self, nums):
		res = []
		nums.sort()
		for n in range(len(nums)+1):
			self.dfs(nums, 0, 0, n, [], res)
		return res

	def dfs(self, nums, start, depth, n, path, res):
		if depth == n:
			res.append(path)
			return

		for i in range(start, len(nums)):
			if i > start and nums[i] == nums[i-1]:
				continue
			self.dfs(nums, i+1, depth+1, n, path+[nums[i]], res)

	# def subsetsWithDup2(self, nums):
	# 	res = []
	# 	nums.sort()
	# 	for n in range(len(nums)+1):
	# 		self.dfs2(nums, 0, 0, n, [], res)
	# 	return res
	#
	# def dfs2(self, nums, start, depth, n, path, res):
	# 	if depth == n:
	# 		res.append(path)
	# 		return
	#
	# 	for i in range(start, len(nums)):
	# 		if i > start and nums[i] == nums[i-1]:
	# 			continue
	# 		self.dfs2(nums, i+1, depth+1, n, path+[nums[i]], res)


if __name__ == '__main__':
	print(Solution().subsetsWithDup([1, 2, 2]))
	pass
