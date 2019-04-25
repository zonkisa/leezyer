from leeyzer import solution, timeit, Solution, make_tree, TreeNode

# @Date: 2019/4/25
# @Author: *** 
# @description:
import collections


class Q226_Invert_Binary_Tree(Solution):
    @timeit
    @solution
    def Q226_Invert_Binary_Tree1(self, root):
        if root:
            root.left, root.right = \
                self.Q226_Invert_Binary_Tree1(root.right), \
                self.Q226_Invert_Binary_Tree2(root.left)
        return root

    
    
    @timeit
    @solution
    def Q226_Invert_Binary_Tree2(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


    # @timeit
    # @solution
    # def Q226_Invert_Binary_Tree3(self, root):
    #     queue = collections.deque([(root)])
    #     while queue:
    #         node = queue.popleft()
    #         if node:
    #             node.left, node.right = node.right, node.left
    #             queue.append(node.left)
    #             queue.append(node.right)
    #     return root
    

def main():
    q = Q226_Invert_Binary_Tree()
    q.add_args(make_tree([4,2,1,3,7,6,9]))
    # q.add_args()
    q.test()


if __name__ == "__main__":
    main()
