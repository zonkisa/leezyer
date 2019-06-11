from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/6/11
# @Author: *** 
# @description:


class Q39_Combination_Sum(Solution):
    @timeit
    @solution
    def Q39_Combination_Sum1(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        
        return res

    def dfs(self, nums, target, index, path, res):
        # if target < 0:
        #     原路返回的截止条件置于循环体开始判断
        #     return
        if target == 0:
            # 恰好找到该元素num1 + num2 + num3 =
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] <= target:
                self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
    
    
    @timeit
    @solution
    def Q39_Combination_Sum2(self, candidates, target):
    
        pass    
    

def main():
    q = Q39_Combination_Sum()
    # q.Q39_Combination_Sum1([2, 3, 6, 7], 7)
    q.add_args([2, 3, 6, 7], 7)
    q.add_args([2, 3, 5], 9)
    q.test()


if __name__ == "__main__":
    main()
