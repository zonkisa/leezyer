from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/5/8
# @Author: *** 
# @description:


class Q21_Merge_Two_Sorted_Lists(Solution):
    @timeit
    @solution
    def Q21_Merge_Two_Sorted_Lists1(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.Q21_Merge_Two_Sorted_Lists1(l1.next, l2)
            return l1
        else:
            l2.next = self.Q21_Merge_Two_Sorted_Lists1(l1, l2.next)
            return l2
    
    
    @timeit
    @solution
    def Q21_Merge_Two_Sorted_Lists2(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.Q21_Merge_Two_Sorted_Lists2(l1.next, l2)

        return l1 or l2
    

def main():
    q = Q21_Merge_Two_Sorted_Lists()
    q.add_args()
    q.add_args()
    q.test()


if __name__ == "__main__":
    main()
