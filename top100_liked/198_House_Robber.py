class Solution:
    # O(n) space
    def rob1(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[-1]

    def rob2(self, nums):
        if not nums:
            return 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[0] = nums[0]
            elif i == 1:
                res[1] = max(nums[0], nums[1])
            else:
                res[i] = max(nums[i] + res[i - 2], res[i - 1])
        return res[-1]

    def rob3(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0], nums[1])   # b 是当前累计最大值
        for i in range(2, len(nums)):
            tmp = b
            b = max(nums[i] + a, b)             # 更新 b
            a = tmp                             # a 始终比 b 慢更新, 即上上一次的累计最大值
        return b




print(Solution().rob1([1, 2, 3, 1]))
print(Solution().rob1([2, 7, 9, 3, 1, 3]))
