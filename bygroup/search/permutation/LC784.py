class Solution:

	# def toggle(self, S, i):
	# 	S = list(S)
	# 	acii = ord(S[i]) ^ (1 << 5)
	# 	S[i] = chr(acii)
	# 	S = "".join(S)
	# 	return S

	def toggle(self, S, i):
		cp = ""
		for j in range(len(S)):
			c = S[j]
			if i == j:
				c = chr(ord(c) ^ (1 << 5))
			cp += c
		S = cp
		return S

	def letterCasePermutation(self, S):
		res = []
		self.dfs(S, 0, res)
		return res

	def dfs(self, S, start, res):
		if start == len(S):
			res.append(S)
			return

		self.dfs(S, start+1, res)
		if S[start].isalpha():
			S = self.toggle(S, start)
			self.dfs(S, start+1, res)
			S = self.toggle(S, start)

	def letterCasePermutation2(self, S):
		res = [""]
		for c in S:
			if c.isalpha():
				res = [i+j for i in res for j in [c.upper(), c.lower()]]
			else:
				res = [i+c for i in res]
		return res


print(Solution().letterCasePermutation("a1b2"))
print(Solution().letterCasePermutation2("a1b2"))

