class Solution:
	def letterCombinations(self, digits):
		"""
		:param digits: str
		:return: List[str]
		"""
		if not digits: return []
		dic = {
			"0": " ",
			"1": "",
			"2": "abc",
			"3": "def",
			"4": "ghi",
			"5": "jkl",
			"6": "mno",
			"7": "pqrs",
			"8": "tuv",
			"9": "wxyz",
		}
		res = []
		self.dfs(digits, dic, 0, "", res)
		return res

	def dfs(self, digits, dic, index, path, res):
		"""
		:param digits:str
		:param dic: dict
		:param index: int
		:param path: str
		:param res: List[str]
		:return: recursive update path, finally update res
		"""
		if len(path) == len(digits):
			res.append(path)
			return

		for s in dic[digits[index]]:
			self.dfs(digits, dic, index+1, path+s, res)

	def letterCombinationsBFS(self, digits):
		if not digits: return []
		dic = {
			"0": " ",
			"1": "",
			"2": "abc",
			"3": "def",
			"4": "ghi",
			"5": "jkl",
			"6": "mno",
			"7": "pqrs",
			"8": "tuv",
			"9": "wxyz",
		}
		res = [""]	# i 处的解
		for digit in digits:
			tmp = []	# i+1处的解
			for r in res:
			# for i in range(len(res)):
				for s in dic[digit]:
					tmp.append(r + s)
					# tmp.append(res[i] + s)
			res = tmp

		return res


if __name__ == "__main__":
	print(Solution().letterCombinations("234"))
	print(Solution().letterCombinations("012"))

	print(Solution().letterCombinationsBFS("234"))
