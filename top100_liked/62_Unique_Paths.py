import math


class Solution:
	# math C(m+n-2,n-1)
	def uniquePaths1(self, m, n):
		if not m or not n:
			return 0
		return math.factorial(m + n - 2) // (math.factorial(n - 1) * math.factorial(m - 1))

	# O(m*n) space
	def uniquePaths2(self, m, n):
		if not m or not n:
			return 0
		dp = [[1 for _ in range(n)] for _ in range(m)]
		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[-1][-1]

	# O(n) space
	def uniquePaths(self, m, n):
		if not m or not n:
			return 0
		cur = [1] * n
		for i in range(1, m):
			for j in range(1, n):
				cur[j] += cur[j - 1]
		return cur[-1]

	def uniquePaths3(self, m, n):
		def rec(i, j):
			if i == 1 and j == 1:
				return 1
			elif i == 1:
				return rec(i, j - 1)
			elif j == 1:
				return rec(i - 1, j)
			return rec(i - 1, j) + rec(i, j - 1)

		return rec(m, n)


print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths1(3, 2))
print(Solution().uniquePaths2(3, 2))
print(Solution().uniquePaths3(3, 2))
