class Solution:
	def permuteUnique(self, nums):
		res = []
		nums.sort()
		self.dfs(nums, 0, len(nums), [False]*len(nums), [], res)
		return res

	def dfs(self, nums, depth, n, used, path, res):
		if depth == n:
			# print(path)
			res.append(path[:])
			return

		# for i in range(len(nums)):
		# 	if used[i]: continue	# 仍是面向全部元素访问, 此处不是break, 也不用start索引
		# 	if i > 0 and used[i-1] and nums[i] == nums[i-1]:	# i>0 使得第一个元素过关,避免py中nums[-1]干扰
		# 		continue
		# 	used[i] = True
		# 	path.append(nums[i])
		# 	print("run path is => ", path, "\t", depth, "\t", used, "\t", i, used[i-1])
		# 	self.dfs(nums, depth+1, n, used, path, res)
		# 	path.pop()
		# 	used[i] = False

		for i in range(len(nums)):
			if not used[i]: 	# 这样判断快一点
				if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
					continue
			used[i] = True
			path.append(nums[i])
			# print("run path is => ", path, "\t", depth, "\t", used, "\t", i, used[i-1])
			self.dfs(nums, depth+1, n, used, path, res)
			path.pop()
			used[i] = False


if __name__ == '__main__':
	print(Solution().permuteUnique([1, 1, 2]))
	print(Solution().permuteUnique([1, 1]))
