class Solution:
    def letterCombinations(self, digits: str):
        """
        :param digits: str
        :return: List[str]
        """
        if not digits: return []
        dic = {
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
        if len(path) == len(digits):
            res.append(path)
            return

        for s in dic[digits[index]]:
            print(index+1, path+s)
            self.dfs(digits, dic, index+1, path+s, res)


if __name__ == "__main__":
    print(Solution().letterCombinations("234"))
    pass
