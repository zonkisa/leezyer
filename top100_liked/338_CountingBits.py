from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/4/22
# @Author: zon 
# @description:
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

class Q338_CountingBits(Solution):
    @timeit
    @solution
    def Q338_CountingBits1(self, num):
        # better
        return [bin(n).count('1') for n in range(num+1)]
    
    
    @timeit
    @solution
    def Q338_CountingBits2(self, num):
        res = [0]
        while len(res) <= num:
            res += [i + 1 for i in res]
        return res[:num + 1]
    

def main():
    q = Q338_CountingBits()
    q.add_args(4)
    q.add_args(2)
    q.test()

if __name__ == "__main__":
    main()