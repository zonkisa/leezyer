from __future__ import print_function

from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        return [c[0] for c in Counter(nums).most_common(k)]

    def topKFrequent2(self, nums, k):
        counter = Counter(nums)
        # print(counter.get)
        return heapq.nlargest(k, counter.keys(), key=counter.get)

    def topKFrequent3(self, nums, k):
        bucket = [None] * (len(nums) + 1)
        frequencyMap = {}

        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1

        for key, value in frequencyMap.items():
            if bucket[value] == None:
                bucket[value] = []
            bucket[value].append(key)

        res = []
        pos = len(bucket) - 1
        while pos >= 0 and len(res) < k:
            if bucket[pos] != None:
                for c in bucket[pos]:
                    if len(res) < k:
                        res.append(c)
            pos -= 1
        return res


# print(Solution().topKFrequent([1, 1, 2, 2, 3, 3], 2))
# print(Solution().topKFrequent2([1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 2))
print(Solution().topKFrequent2([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 2))
print(Solution().topKFrequent3([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 2))
