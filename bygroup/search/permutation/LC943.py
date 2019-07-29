class Solution:
    def shortestSuperstring(self, A):
        res = []
        self.dfs(A, "", 0, 0, len(A), res)

        minStr = res[0]
        for i in range(1, len(res)):
            if len(res[i]) < len(minStr):
                minStr = res[i]

        return minStr

    def dfs(self, A, S, start, depth, n, res):
        if depth == n:
            res.append(S)
            return

        for i in range(start, len(A)):
            if not S:
                S += A[i]
            else:
                if A[i] in S:
                    self.dfs(A, S, start + 1, depth + 1, n, res)
                else:
                    cp = S
                    for j in range(len(S)-1, -1, -1):
                        if S[j] != A[i][len(S)-1-j]:
                            S += A[i][len(S)-1-j:]
                            break
                    self.dfs(A, S, start + 1, depth + 1, n, res)
                    S = cp

    def shortestSuperstring2(self, A):
        res = []
        self.dfs2(A, 0, len(A), [False] * len(A), "", res)
        print(res)
        minStr = "".join(A)
        for s in res:
            if self.isContains(s, A) and len(s) <= len(minStr):
                minStr = s

        return minStr

    def dfs2(self, A, depth, n, used, S, res):
        if depth == n and len(S) != 0:
            res.append(S)
            return
        for i in range(len(A)):
            curr, currS, yes = A[i], S, used[i]
            if used[i]: continue
            if A[i] in S:
                depth += 1
                used[i] = True
                continue
            used[i] = True

            cp = S
            index = self.getStartDiffStrIndex(S, A[i])
            S += A[i][index:]
            self.dfs2(A, depth+1, n, used, S, res)
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
# print(Solution().shortestSuperstring())
# print(Solution().shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"]))
print(Solution().shortestSuperstring2(a))
# print(Solution().shortestSuperstring2(a))
