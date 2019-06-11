from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/6/10
# @Author: ***
# @description:


class Q287_Find_the_Duplicate_Number(Solution):
    @timeit
    @solution
    def Q287_Find_the_Duplicate_Number1(self, nums):
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            ct = 0
            for i in range(n):
                if nums[i] <= mid:
                    ct += 1
            if ct <= mid:
                lo = mid + 1
            else:
                hi = mid
        return hi
    
    
    @timeit
    @solution
    def Q287_Find_the_Duplicate_Number2(self, nums):
    
        pass    
    

def main():
    q = Q287_Find_the_Duplicate_Number()
    q.add_args([4, 1, 4, 4, 2, 3, 4, 5, 4])
    # q.add_args()
    q.test()


if __name__ == "__main__":
    main()
