class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(0, n)

    def helper(self, curr: int, n: int) -> int:
        if curr > n:
            return 0
        if curr == n:
            return 1
        return self.helper(curr + 1, n) + self.helper(curr + 2, n)

    def climbStairs2(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.helper2(0, n, memo)

    def helper2(self, curr: int, n: int, memo: list) -> int:
        if curr > n:
            return 0
        if curr == n:
            return 1
        if memo[curr] > 0:
            return memo[curr]
        memo[curr] = self.helper2(curr + 1, n, memo) + self.helper2(curr + 2, n, memo)
        return memo[curr]

print(Solution().climbStairs2(3))

