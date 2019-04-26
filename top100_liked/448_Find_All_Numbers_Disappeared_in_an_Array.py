from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/4/26
# @Author: *** 
# @description:
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Q448_Find_All_Numbers_Disappeared_in_an_Array(Solution):
    @timeit
    @solution
    def Q448_Find_All_Numbers_Disappeared_in_an_Array1(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i+1 for i in range(len(nums)) if nums[i] > 0]
        pass
    
    
    @timeit
    @solution
    def Q448_Find_All_Numbers_Disappeared_in_an_Array2(self, nums):
        """
        :param nums:list[int]
        :return: list[int] taken extra space
        """
        return [set(range(1, len(nums)+1)) - set(nums)]
        return [i for i in range(1, len(nums)+1) if i not in set(nums)]
        pass    
    

def main():
    q = Q448_Find_All_Numbers_Disappeared_in_an_Array()
    # q.add_args()
    # q.add_args()
    q.test()


if __name__ == "__main__":
    main()
