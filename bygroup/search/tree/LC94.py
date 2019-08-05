class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, node, res):
        if not node:
            return
        if node.left:
            self.dfs(node.left, res)
        res.append(node.val)
        if node.right:
            self.dfs(node.right, res)

    def inorderTraversalIteratively(self, root):
        """
        先将每个结点的左结点记录, 再每一次弹出栈自底向上添加到res, 每次弹出时即可添加当前结点, 再进入其右子结点分支
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

    def pre_Iteratively(self, root):
        if not root:
            return []
        stack, res = [], []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def mid_Iteratively(self, root):
        if not root:
            return []
        stack, res = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def post_Iteratively(self, root):
        if not root:
            return []
        stack1, stack2, res = [], [], []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            res.append(stack2.pop().val)
        return res

    def pre_loop(self, root):
        stack, res = [], []
        stack.append((root, 0))
        while stack:
            node, isVisited = stack.pop()
            if not node:
                continue
            if isVisited:
                res.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node.left, 0))
                stack.append((node, 1))
        return res

    def mid_loop(self, root):
        stack, res = [], []
        stack.append((root, 0))
        while stack:
            node, isVisited = stack.pop()
            if not node:
                continue
            if isVisited:
                res.append(node.val)
            else:
                stack.append((node.right, 0))
                stack.append((node, 1))
                stack.append((node.left, 0))
        return res

    def post_loop(self, root):
        stack, res = [], []
        stack.append((root, 0))
        while stack:
            node, isVisited = stack.pop()
            if not node:
                continue
            if isVisited:
                res.append(node.val)
            else:
                stack.append((node, 1))
                stack.append((node.right, 0))
                stack.append((node.left, 0))
        return res

    def pre_recursive(self, root):
        res = []
        self.pre_dfs(root, res)
        return res

    def pre_dfs(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.pre_dfs(node.left, res)
        self.pre_dfs(node.right, res)

    def mid_recursive(self, root):
        res = []
        self.mid_dfs(root, res)
        return res

    def mid_dfs(self, node, res):
        if not node:
            return
        self.mid_dfs(node.left, res)
        res.append(node.val)
        self.mid_dfs(node.right, res)

    def post_recursive(self, root):
        res = []
        self.post_dfs(root, res)
        return res

    def post_dfs(self, node, res):
        if not node:
            return
        self.post_dfs(node.left, res)
        self.post_dfs(node.right, res)
        res.append(node.val)


if __name__ == '__main__':
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    t.left.right.left = TreeNode(7)
    t.right = TreeNode(3)
    t.right.left = TreeNode(6)
    print(Solution().pre_recursive(t))
    print(Solution().pre_loop(t))
    print(Solution().pre_Iteratively(t))

    print(Solution().mid_recursive(t))
    print(Solution().mid_loop(t))
    print(Solution().mid_Iteratively(t))

    print(Solution().post_recursive(t))
    print(Solution().post_loop(t))
    print(Solution().post_Iteratively(t))
