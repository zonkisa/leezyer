from leeyzer import solution, timeit, Solution, make_tree, TreeNode


# @Date: 2019/6/24
# @Author: 
# @description:
class Q406_Queue_Reconstruction_by_Height(Solution):
	@timeit
	@solution
	def Solution1(self, people):
		"""
		将数据以身高降序、人数升序排列，然后以人数为列表下标插入到空列表中。由于身高降序，后出现的较小的身高必定在前面
		有使用额外空间 takes O(n^2) because each insert into the list takes O(n).
		"""
		if not people:
			return []
		people = sorted(people, key=lambda x: (-x[0], x[1]))
		res = []
		for p in people:
			res.insert(p[1], p)
		return res

	@timeit
	@solution
	def Solution2(self, people):
		# blocks = [[]]
		# for p in sorted(people, key=lambda x: (-x[0], x[1])):
		# 	index = p[1]
		#
		# 	for i, block in enumerate(blocks):
		# 		m = len(block)
		# 		if index <= m:
		# 			break
		# 		index -= m
		# 	block.insert(index, p)
		# 	if m * m > len(people):
		# 		blocks.insert(i + 1, block[m // 2:])
		# 		del block[m // 2:]
		#
		# return [p for block in blocks for p in block]
		pass


def main():
	q = Q406_Queue_Reconstruction_by_Height()
	q.add_args([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
	# q.add_args([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
	q.test()


if __name__ == "__main__":
	main()
