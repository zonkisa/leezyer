# coding: utf-8
from __future__ import print_function
from queue import Queue


class Node:
    left = None
    right = None

    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.N = N  # 以该结点为根的子树中的结点总数
        # self.left = None
        # self.right = None


class BinarySearchTree:
    """
    背景：能有效结合链表插入的灵活性和有序数组查找的高效性
    二叉查找树
    """
    def __init__(self):
        self.root = Node(None, None, 0)

    def min(self):
        return self.getMinNode(self.root).key

    def getMinNode(self, node):
        if node.left is None or node.left.key is None:
            return node
        return self.getMinNode(node.left)

    def size(self):
        return self.getSize(self.root)

    def getSize(self, node):
        if node is None or node.key is None:
            return 0
        else:
            return node.N

    def get(self, key):
        return self.getKey(self.root, key)

    def getKey(self, node, key):
        """
        在以Node为根结点的子树中查找并返回key所对应的值
        """
        if not node:
            return None
        if key < node.key:
            self.getKey(node.left, key)
        elif key > node.key:
            self.getKey(node.right, key)
        else:
            return node.key

    def getNotRecursive(self, key):
        # 非递归版本的get方法，在查询次数较多时优先使用
        node = self.root
        while node:
            if key == node.key:
                return node.val
            elif key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right

        return None

    def put(self, key, val):
        self.root = self.__put(self.root, key, val)

    def __put(self, node, key, val):
        """
        若key存在于以node为根结点的子树中则更新值
        否则将以key和val为键值对的新结点插入到该子树中
        """
        if node is None or node.key is None:
            return Node(key, val, 1)
        if key < node.key:
            node.left = self.__put(node.left, key, val)
        elif key > node.key:
            node.right = self.__put(node.right, key, val)
        else:
            node.val = val
        if key != node.key:
            node.N = self.getSize(node.left) + self.getSize(node.right) + 1

        return node

    def floor(self, key):
        """
        小于等于指定键key的最大key
        在左子树中查找小于指定key的node比较容易
        若最终能匹配，则该node必定在恰好大于该key的结点的左子树中,因此最终是在k > node.key阶段中返回实际值
        """
        node = self.__floor(self.root, key)
        if not node or node.key is None:
            return None
        return node.key

    def __floor(self, node, key):
        if not node or node.key is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self.__floor(node.left, key)
        else:
            t = self.__floor(node.right, key)
            # 必须先判断空值情况,非空条件是t is not None and t.key is not None时，t返回None时会报错
            if t is None or t.key is None:
                return node
            else:
                return t

    def MyRecursiveFloor(self, key):
        if not self.root or self.root.key is None:
            return None
        node = self.root
        ct = 0
        while key != node.key:
            if key < node.key:
                if node.left and node.left.key is not None:
                    ct = 1
                    node = node.left
                else:
                    if not ct:
                        node = Node(None, None, 0)
                    break
            if key > node.key:
                if node.right and node.right.key is not None and key > node.right.key:
                    node = node.right
                else:
                    break
        return node.key

    def ceiling(self, key):
        """
        大于等于指定key的最小key
        若最终能匹配，则该node必定在恰好小于该key的结点的右子树中，因此最终是在k < node.key阶段中返回实际值
        """
        node = self.__ceiling(self.root, key)
        if node and node.key is not None:
            return node.key
        else:
            return None

    def __ceiling(self, node, key):
        if not node or node.key is None:
            return None
        if key == node.key:
            return node
        elif key > node.key:
            return self.__ceiling(node.right, key)
        else:
            t = self.__ceiling(node.left, key)
            # 必须先判断空值情况,非空条件是t is not None and t.key is not None时，t返回None时会报错
            if t is None or t.key is None:
                return node
            else:
                return t

    def select(self, k):
        """
        找到排名为k的键(即树中正好有k个键小于该键)
        假若能匹配，则该键位的左子树的结点数恰好相等
        若k过大，则需分配剩余数目到右子树
        """
        if self.root.N < k:
            return None
        elif self.root.N >= k:
            node = self.__select(self.root, k)
        if node is None or node.key is None:
            return None
        else:
            return node.key

    def __select(self, node, k):
        if node is None or node.key is None:
            return None
        t = self.getSize(node.left)
        if t == k:
            return node
        elif t > k:
            return self.__select(node.left, k)
        else:
            return self.__select(node.right, k-t-1) # 这里-1包含了node自身

    # 恰好有k个子结点的结点，应该先看该结点左右子树的总数与k的关系，这里没有考虑清楚
    def __WrongSelect(self, node, k):
        if node is None or node.key is None:
            return None
        if node.N == k:
            return node
        elif k > node.N:
            return self.__select(node.right, k)
        else:
            return self.__select(node.left, k)

    # 返回树中小于key的结点个数,注意当node.key大于key时的处理方法
    def rank(self, key):
        return self.__rank(self.root, key)

    def __rank(self, node, key):
        if node is None or node.key is None:
            return 0
        if key == node.key:
            return self.getSize(node.left)
        elif key < node.key:
            return self.__rank(node.left, key)
        else:
            return 1 + self.getSize(node.left) + self.__rank(node.right, key)

    # TODO
    def deleteMin(self):
        self.root = self.__deleteMin(self.root)

    def __deleteMin(self, node):
        """
        注意node.left = self.__deleteMin(node.left)，这个式子对delete模式有效 ！！！
        当__deleteMin返回为空时，即node.left.left is None，且将node.left置为空结点，
        此时已经找到最小结点并删除，此时要即时更新最小结点的父结点信息N，此时更新信息为自底向上
        """
        if node.left is None or node.left.key is None:
            return node.right
        node.left = self.__deleteMin(node.left)
        node.N = self.getSize(node.left) + self.getSize(node.right) + 1
        return node

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __delete(self, node, key):
        if node is None or node.key is None:
            return None
        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
        else:
            if node.right is None or node.right.key is None:
                return node.left # 左右子结点若各有空值情况，则将另一侧子结点续上，即target.side = target.side.side
            if node.left is None or node.left.key is None:
                return node.right
            tmpNode = node
            node = self.getMinNode(node.right)
            node.right = self.__deleteMin(tmpNode.right)
            node.left = tmpNode.left
        # 在当前__delete周期内更新node.N信息
        node.N = self.getSize(node.left) + self.getSize(node.right) + 1
        return node

    def findKeys(self, lo_key, hi_key):
        queue = Queue()
        self.__findKeys(self.root, queue, lo_key, hi_key)
        return queue

    def __findKeys(self, node, queue, lo_key, hi_key):
        if node is None or node.key is None:
            return
        if lo_key < node.key:
            self.__findKeys(node.left, queue, lo_key, hi_key)
        if lo_key <= node.key <= hi_key:
            queue.put(node.key)
            # queue.enqueue(node.key)
        if hi_key > node.key:
            self.__findKeys(node.right, queue, lo_key, hi_key)

    def __str__(self):
        keys, vals = [], []
        self.midTraverse(self.root, keys, vals)
        res = "{"
        for k, v in zip(keys, vals):
            res += "{}: {}, ".format(k, v)
        return res + "}"

    def midTraverse(self, node, keys, vals):
        if node is None or node.key is None:
            return
        self.midTraverse(node.left, keys, vals)
        keys.append(node.key)
        vals.append(node.val)
        self.midTraverse(node.right, keys, vals)

    """
    在一棵二叉查找树中，所有操作在最坏情况下所需的时间都和树的高度成正比
    随机键构造的二叉查找树的平均高度为树中结点树的对数级别，接近2.99lgN，不随机则参考平衡二叉树
    因此，二叉查找树的基本实现的性能优劣，依赖于其中的键的分布是否足够随机以消除长路径
    顺序或逆序插入则会出现这种情况（此时树为"单叉树"）
    """
