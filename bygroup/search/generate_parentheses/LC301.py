class Solution:

	def isValid(self, s):
		ct = 0
		for c in s:
			if c == "(":
				ct += 1
			if c == ")":
				ct -= 1
			if ct < 0:
				return False
		return ct == 0

	def removeInvalidParenthesis(self, s):
		left, right = 0, 0
		for c in s:
			left += 1 if c == "(" else 0
			if c == ")":
				if left == 0:
					right += 1
				else:
					left -= 1
		print(left, right)
		res = []
		self.dfs(s, 0, left, right, res)
		return res

	def dfs(self, s, start, left, right, res):
		if right == left == 0:
			if self.isValid(s):
				res.append(s)
			return

		for i in range(start, len(s)):
			if i != start and s[i] == s[i-1]:
				continue
			if s[i] in "()":
				curr = list(s)
				curr = "".join(curr[:i]) + "".join(curr[i+1:])
				if right > 0:
					self.dfs(curr, i, left, right-1, res)
				elif left > 0:
					self.dfs(curr, i, left-1, right, res)


if __name__ == '__main__':
	print(Solution().removeInvalidParenthesis("()())))(("))

