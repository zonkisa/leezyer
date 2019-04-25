from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/4/25
# @Author: *** 
# @description:
"""
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Q283_Move_Zeroes(Solution):
    @timeit
    @solution
    def Q283_Move_Zeroes1(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    
    
    @timeit
    @solution
    def Q283_Move_Zeroes2(self, nums):
        nums.sort(key=lambda x: 1 if x == 0 else 0)
        # nums.sort(key=bool, reverse=True)

    

def main():
    q = Q283_Move_Zeroes()
    q.add_args([0,1,0,3,12])
    # q.add_args()
    q.test()


if __name__ == "__main__":
    main()
