from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/6/4
# @Author: *** 
# @description:


class Q238_Product_of_Array_Except_Self(Solution):
    @timeit
    @solution
    def Q238_Product_of_Array_Except_Self1(self, nums):
        if nums.count(0) >= 2:
            return [0] * len(nums)
        p = 1
        for i in nums:
            if i != 0:
                p *= i
        if nums.count(0) == 1:
            return [p if k == 0 else 0 for k in nums]
        else:
            return [p//k for k in nums]
    
    
    @timeit
    @solution
    def Q238_Product_of_Array_Except_Self2(self, nums):
        N = len(nums)
        if nums.count(0) >= 2:
            return [0] * N
        res = []
        p = 1
        for i in range(N):
            res.append(p)
            p *= nums[i]

        p = 1
        for j in range(N-1, -1, -1):
            res[j] = res[j] * p
            p *= nums[j]

        return res
    

def main():
    q = Q238_Product_of_Array_Except_Self()
    q.add_args([0, 1, 2, 3, 4, 0])
    q.add_args([2, 3, 4])
    q.test()


if __name__ == "__main__":
    main()
