# coding:utf-8
from __future__ import print_function
"""
动态连通性问题 --> 过滤掉序列中所有无意义的整数对
A,给出两个节点，判断它们是否连通，如果连通，不需要给出具体的路径
B,给出两个节点，判断它们是否连通，如果连通，需要给出具体的路径

其中union-find是解决问题A，而问题B可以使用基于深度优先的算法

动态连通性的应用场景：

1.网络连接判断：
如果每个pair中的两个整数分别代表一个网络节点，那么该pair就是用来表示这两个节点是需要连通的。那么为所有的pairs建立了动态连通图后，就能够尽可能少的减少布线的需要，因为已经连通的两个节点会被直接忽略掉。
2.变量名等同性(类似于指针的概念)：
在程序中，可以声明多个引用来指向同一对象，这个时候就可以通过为程序中声明的引用和实际对象建立动态连通图来判断哪些引用实际上是指向同一对象。


基础假设，对于连通的所有节点，可以认为它们属于一个组，因此不连通的节点必然就于不同的组。
随着Pair的输入，需要首先判断输入的两个节点是否连通。
如何判断呢？按照上面的假设，可以通过判断它们属于的组，然后看看这两个组是否相同，如果相同，那么这两个节点连通，反之不连通。
为简单起见，将所有的节点以整数表示，即对N个节点使用0到N-1的整数表示。
而在处理输入的Pair之前，每个节点必然都是孤立的，即分属于不同的组，可以使用数组来表示这一层关系，
数组的index是节点的整数表示，而相应的值就是该节点的组号
数组的index是节点的整数表示，而相应的值就是该节点的组号
数组的index是节点的整数表示，而相应的值就是该节点的组号
"""

"""
quick-find 复杂度分析：
union和connect都是基于find操作，在进行Union时，根据p、v值分别访问数组(2次)，
若不等，需要检查整个数组（N次），可能的改变次数为1~N-1次。 N+3 ~ 2N+1
若最后只有一个连通分量，最少连接是邻居互连，共N-1次。
平方复杂度
9条 0.024s
900条 36.5s  1600呗
"""

class QuickFind:
    # count的含义为等价类/组的数量
    def __init__(self, N):
        if N <= 0:
            raise ValueError(" N should be greater than 0 ")
        self.count = N
        self.ids = list(range(self.count))

    # 连接两个节点，使之属于同一个组
    def union(self, p, v):
        pID = self.find(p)
        qID = self.find(v)
        if pID == qID:
            return
        if pID != qID:
            for i in range(len(self.ids)):
                if self.ids[i] == pID:
                    self.ids[i] = qID

        self.count -= 1

    # 查询节点属于的组,数组对应位置的值即为组号
    def find(self, p):
        return self.ids[p]

    # 判断两个节点是否属于同一个组,分别得到两个节点的组号，然后判断组号是否相等
    def connected(self, p, v):
        return self.find(p) == self.find(v)
        # return self.ids[p] == self.ids[v]

    # 获取组的数目
    def count(self):
        return self.count()


class QuickUnion:
    def __init__(self, N):
        if N <= 0:
            raise ValueError(" N should be greater than 0 ")
        self.count = N
        self.ids = list(range(self.count))

    def connected(self, p, v):
        return self.find(p) == self.find(v)

    # 获取组的数目
    def count(self):
        return self.count()

    def find(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        if pRoot != qRoot:
            self.ids[pRoot] = qRoot
        self.count -= 1


class WeightedQuickUnion:
    def __init__(self, N):
        if N <= 0:
            raise ValueError(" N should be greater than 0 ")
        self.count = N
        self.ids = list(range(N))
        self.size = [1] * N

    def connected(self, p, v):
        return self.find(p) == self.find(v)

    # 获取组的数目
    def count(self):
        return self.count()

    def find(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def union(self, p, q):
        """
        分配权重
        重点在于父节点与权重的更新
        父节点权重大，则将权重小的父节点指向权重大的父节点，同时更新父节点权重
        """
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        elif self.size[pRoot] < self.size[qRoot]:
            self.ids[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
        else:
            self.ids[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]
        self.count -= 1


class PathCompressedWeightedQuickUnion:
    """
    1.5.12 使用路径压缩的加权quick-union
    要实现路径压缩，需要为find方法添加循环，将路径上的所有节点直接链接到根节点，得到几乎完全扁平的树
    """
    def __init__(self, N):
        if N <= 0:
            raise ValueError(" N should be greater than 0 ")
        self.count = N
        self.ids = list(range(N))
        self.size = [1] * N

    def find_bad(self, p):
        """
        循环将从p到根节点的路径上的每个节点都连接到节点，这里用到两次循环
        """
        tmp = p
        while p != self.ids[p]:
            p = self.ids[p]
        pRoot = p
        p = tmp
        while pRoot != self.ids[p]:
            tmp = self.ids[p]
            self.ids[p] = pRoot
            p = tmp

        return pRoot

    def find(self, p):
        """
        循环将从p到根节点的路径上的每个节点都连接到节点
        此处路径压缩体现在，更新父节点时，由于p != self.ids[p]，故每次多往前走一部
        """
        while p != self.ids[p]:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]

        return p

    def connected(self, p, v):
        return self.find(p) == self.find(v)

    # 获取组的数目
    def count(self):
        return self.count()

    def union(self, p, q):
        """
        分配权重
        重点在于父节点与权重的更新
        父节点权重大，则将权重小的父节点指向权重大的父节点，同时更新父节点权重
        """
        pRoot = self.find(p)
        qRoot = self.find(q)
        if pRoot == qRoot:
            return
        elif self.size[pRoot] < self.size[qRoot]:
            self.ids[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
        else:
            self.ids[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]
        self.count -= 1
