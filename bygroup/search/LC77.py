class Solution:
    def combine(self, n, k):
        res = []
        self.dfs(n+1, 1, 0, k, [], res)
        return res
        # return [r for r in res if r[0] != r[1]]

    def dfs(self, n, start, depth, k, path, res):
        # if depth > k:
        #     return
        if depth == k:
            res.append(path)
            return

        for i in range(start, n):
            print(n, k, start, depth, path, res)
            print("-----------------")
            self.dfs(n, i+1, depth+1, k, path+[i], res)
            print("-------------------------------------------")

    def combine2(self, n: int, k: int):
        res = []
        self.dfs2(n + 1, k, 1, 0, [], res)
        return res

    def dfs2(self, n, k, start, depth, path, res):
        if depth == k:
            res.append(path)
            return
        for i in range(start, n - (k - len(path)) + 1):
            self.dfs2(n, k, i + 1, depth + 1, path + [i], res)


if __name__ == "__main__":
    print(Solution().combine(4, 2))
    print(Solution().combine2(4, 2))
    # print(Solution().combine2(3, 1))
    pass
