class Solution:

    def shortestSuperstring(self, A):
        minStr = "".join(A)
        res = [minStr]
        self.dfs(A, 0, len(A), [False] * len(A), "", res)
        return res[0]

    def dfs(self, A, depth, n, used, S, res):
        if depth == n and len(S) < len(res[0]):
            res[0] = S
            return
        for i in range(len(A)):
            if used[i]: continue
            used[i] = True

            cp = S
            if A[i] in S:
                self.dfs(A, depth + 1, n, used, S, res)
            else:
                index = self.getStartDiffStrIndex(S, A[i])
                S += A[i][index:]
                self.dfs(A, depth+1, n, used, S, res)
            S = cp
            used[i] = False

    def getStartDiffStrIndex(self, S1, S2):
        ct = 0
        for i in range(len(S2)):
            if S1[-(i+1):] == S2[:i+1]:
                ct = i+1
        return ct

    def isContains(self, S, ls):
        for s in ls:
            if s not in S:
                return False
        return True


a = ["alex", "loves", "leetcode"]
b = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
c = ["gcta", "ttca", "atgcatc", "catg", "ctaagt"]
d = ["uhozqhxcqmkifljvcie","epuhozqhxcqmkifljvci","ugmqnepuhozqhxcqm","iexdudtvurjkrovrhmpa","rovrhmpaasblgaosw","qmkifljvciexdudtv","zsgtuowskyzphybeugm","uowskyzphybeugmq","qhxcqmkifljvciex"]
# print(Solution().shortestSuperstring())
# print(Solution().shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
print(Solution().shortestSuperstring(c))
print(Solution().shortestSuperstring(b))
import time
t1 = time.time()
print(Solution().shortestSuperstring(d))
print(time.time() - t1)
