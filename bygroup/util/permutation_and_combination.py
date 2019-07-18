def permutation(nums, depth, n, used, curr, ans):
	"""
	:param nums: 元素个数
	:param depth: 递归深度
	:param n: 进行全排列要取出的个数
	:param used: 集合, 描述元素是否被使用
	:param curr: 当前排列结果
	:param ans: result
	:return:
	"""
	if depth == n:
		ans.append(curr)
		return

	for i in range(len(nums)):
		if used[i]: continue
		used[i] = True
		curr.append(nums[i])
		permutation(nums, depth+1, n, used, curr, ans)
		curr.pop()
		used[i] = False


def combination(nums, depth, n, start, curr, ans):
	if depth == n:
		ans.append(curr)
		return

	for i in range(start, len(nums)):
		curr.append(nums[i])
		combination(nums, depth+1, n, i+1, curr, ans)
		curr.pop()


ans = []
permutation([1, 2, 3], 0, 3, [False] * 3, [], ans)
print(ans)

res = []
combination([1, 2, 3], 0, 3, 0, [], res)
print(res)
