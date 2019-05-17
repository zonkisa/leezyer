from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/5/9
# @Author: *** 
# @description:


class Q543_Diameter_of_Binary_Tree(Solution):
    @timeit
    @solution
    def Q543_Diameter_of_Binary_Tree1(self, root):
        self.ct = 0

        def depth(tree):
            if not tree:
                return 0
            left, right = depth(tree.left), depth(tree.right)
            self.ct = max(self.ct, left+right)
            return 1 + max(left, right)

        depth(root)
        return self.ct
    
    
    @timeit
    @solution
    def Q543_Diameter_of_Binary_Tree2(self, root):
        self.best = 1

        def depth(root):
            if not root: return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR + 1)
            return 1 + max(ansL, ansR)

        depth(root)
        return self.best - 1
    

def main():
    q = Q543_Diameter_of_Binary_Tree()
    q.add_args()
    q.add_args()
    q.test()


if __name__ == "__main__":
    main()
