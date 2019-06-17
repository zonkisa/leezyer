# coding: utf-8
from __future__ import print_function


class ResizingArrayStackWithPython:
    def __init__(self):
        self.ls = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.ls)

    def push(self, elem):
        self.ls.append(elem)

    def pop(self):
        if self.isEmpty():
            return None
        return self.ls.pop()


class ResizingArrayStack:
    """
    下压栈的实现
    背景：定容栈几乎为空时浪费内存；扩容不方便；
    由于python语法特性，ResizingArrayStackWithPython无需考虑容量内存
    """

    def __init__(self, nums):
        self.ls = [None] * nums
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def push(self, elem):
        if self.N == len(self.ls):
            self._resize(2 * self.N)
        self.ls[self.N] = elem
        self.N += 1

    # 防止容量不足
    def _resize(self, k):
        tmp = [None] * k
        for i in range(self.N):
            tmp[i] = self.ls[i]
        self.ls = tmp

    def pop(self):
        self.N -= 1
        elem = self.ls[self.N]
        self.ls[self.N] = None  # 避免对象处于游离状态
        if self.N > 0 and self.N == len(self.ls) // 4:  # 严格=，保证使用率不低于1/4
            self._resize(len(self.ls) // 2)

        return elem


class PriorityQueueInArray:
    """
    优先队列：在队列中当前优先级最高的元素先出队
    基于数组实现的无序优先队列
    此处维持算法第四版对索引的操作，见上面ResizingArrayStack
    补充：若要限制队列中个数，需对N进行判断并删除最小值
        若要保证队列中有序，需要修改insert
    """

    def __init__(self, collection):
        self.que = collection
        self.N = len(self.que)  # 默认初始化传参数组中无None类型，否则要遍历+交换索引

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, elem):
        if self.N == len(self.que):
            self._resize(2 * self.N)
        self.que[self.N] = elem
        self.N += 1

    def _resize(self, k):
        tmp = [None] * k
        for i in range(self.N):
            tmp[i] = self.que[i]
        self.que = tmp

    def pop(self):
        if self.isEmpty():
            return None
        self.N -= 1
        elem = self.Max()
        self.que[self.N] = None
        if self.N > 0 and self.N == len(self.que) // 4:
            self._resize(len(self.que) // 4)
        return elem

    def Max(self):
        max_idx = 0
        for i in range(1, self.N):
            if self.que[max_idx] < self.que[i]:
                max_idx = i
        tmp = self.que[max_idx]
        self.que[max_idx] = self.que[self.N - 1]
        self.que[self.N - 1] = tmp

        return tmp

    def delMax(self):
        return self.pop()


class PriorityQueueInHeap:
    """
    基于堆的优先队列
    二叉堆特性：在二叉堆的数组中，每个元素都要保证大于等于另两个特定位置的元素，以此类推
    在堆有序的二叉树中，每个结点都小于等于它的父结点，即此树中根结点最大
    """

    def __init__(self, maxN):
        """
        默认大小为N，且装载元素的索引为 1 ~ N
        """
        self.pq = [None] * (maxN + 1)
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N

    def insert(self, elem):
        """
        新元素加到数组末尾，增加堆的大小，然后让这个新元素上浮到合适的位置
        """
        if self.N == len(self.pq):
            self._resize(2 * self.N)
        self.N += 1
        self.pq[self.N] = elem
        self.swim(self.N)

    def delMax(self):
        if self.isEmpty():
            return None
        elem = self.pq[1]
        # 这里书中将索引1和N处元素作了交换，但最大值elem已取出，所以此处仅将末尾元素置顶即可，减少一次数组访问
        self.pq[1] = self.pq[self.N]
        self.N -= 1
        # 注意这里N是先减1再防止对象游离，维持N作为容量的语义一致性
        self.pq[self.N+1] = None
        self.sink(1)
        lenth = len(self.pq)
        if self.N > 0 and self.N == lenth // 4:
            self._resize(lenth // 2)

        return elem

    def sink(self, k):
        """
        下沉是由于删除最大值后，末尾元素暂时在根结点位置，若此时子结点比该末尾结点大，则需要调整整个堆的顺序
        首先结点位置为k时，其子结点位置为2k/2k+1，找到二叉堆子结点中较大者，再进行比较，或下沉或停止
        """
        while 2 * k <= self.N:
            j = 2 * k
            # 保证下沉时比较的都是左右子结点中最大的一个
            if j < self.N and self.less(j, j + 1):
                j += 1
            # 当子结点小于等于时停止
            if self.less(k, j):
                self.exch(k, j)
                k = j
            else:
                break

    def swim(self, k):
        """
        上浮是由于新结点比其父结点更大，因此需要移动到合适的位置
        结点位置为k时，其父结点的位置为 k//2
        """
        while k > 1 and self.less(k // 2, k):
            self.exch(k // 2, k)
            k = k // 2

    # 习题2.4.22
    def _resize(self, k):
        tmp = [None] * k
        for i in range(self.N):
            tmp[i] = self.pq[i]

        self.pq = tmp

    def less(self, i, j):
        return self.pq[i] < self.pq[j]

    def exch(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t

    def __str__(self):
        return "N is {}, pq lenth is {}, pq is {}".format(self.N, len(self.pq), self.pq)


class IndexMaxPQ:
    """
    允许其它用例引用已经进入优先队列中的元素是必要的，此时需要给优先队列中每个元素一个索引
    即此时其它用例可能已经在使用一个整数索引（索引优先队列）来引用这些元素

    索引优先队列，可以被视为一个能够快速访问其中最小元素的数组
    最好能支持快速访问数组的一个特定子集的最小元素（比如所有被插入的元素）
    """
    def __init__(self, maxN):
        self.N = 0                      # 表示PQ中的元素数量
        self.keys = [None] * (maxN + 1) # 有优先级区分的元素,new
        self.pq = [None] * (maxN + 1)   # 索引二叉堆，从1开始
        self.qp = [-1] * (maxN + 1)     # 逆序， qp[pq[i]] = pq[qp[j]] = i, new

    def isEmpty(self):
        return self.N == 0

    def contains(self, k):
        """
        这里基于exch的解释换一种理解方式
        若qp[k] = x , 此时pq[x] = value
        若keys中存在该value，则x有效，值不为-1
        """
        return self.qp[k] != -1

    def size(self):
        return self.N

    def insert(self, k, key):
        """
        在keys中插入一个元素key，将它和keys的下标k相关联。这里默认如果k存在会返回提示，如需要改变，见changeKey
        若不存在，需要跟新qp、pq、keys，再调整顺序swim
        """
        if self.contains(k):
            raise Exception("index is already in the priority queue")
        self.N += 1
        self.qp[k] = self.N
        self.pq[self.N] = k
        self.keys[k] = key
        self.swim(self.N)

    def maxIndex(self):
        if self.N == 0:
            raise Exception("Priority queue underflow")
        return self.pq[1]

    def maxKey(self):
        if self.N == 0:
            raise Exception("Priority queue underflow")
        return self.keys[self.pq[1]]

    def delMax(self):
        if self.N == 0:
            raise Exception("Priority queue underflow")
        maxIndex = self.pq[1]
        self.exch(1, self.N)
        self.N -= 1
        self.sink(1)

        assert self.pq[self.N+1] == maxIndex
        self.qp[maxIndex] = -1
        self.keys[maxIndex] = None
        self.pq[self.N + 1] = -1

        return maxIndex

    def keyOf(self, i):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        else:
            return self.keys[i]

    def changeKey(self, i, key):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        self.keys[i] = key
        self.swim(self.qp[i])
        self.sink(self.qp[i])

    def change(self, i, key):
        self.changeKey(i, key)

    def increaseKey(self, i, key):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        if self.keys[i] >= key:
            raise Exception("Calling decreaseKey() with given argument would not strictly decrease the key")

        self.keys[i] = key
        self.swim(self.qp[i])

    def decreaseKey(self, i, key):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        if self.keys[i] <= key:
            raise Exception("Calling decreaseKey() with given argument would not strictly decrease the key")

        self.keys[i] = key
        self.sink(self.qp[i])

    def delete(self, i):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        index = self.qp[i]
        self.exch(index, self.N)
        self.N -= 1
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1

    def less(self, i, j):
        return self.keys[self.pq[i]] < self.keys[self.pq[j]]

    def exch(self, i, j):
        """
        索引优先队列的上浮和下沉操作是实际更改的部分，而具体变化体现在比较和交换操作。
        keys、pq和qp的关系：
        首先keys装载的是实际的值，pq是对应此值数组keys的下标优先队列，qp是对应pq的逆序数组；
        由于pq装载的是keys中各个key值对应的数组下标，因此pq中每个元素不大于maxN，且由于第0位不用，pq中值范围是1 ~ maxN；
        假设keys中第i个元素值为key，在pq中存的第a个元素值是i，则qp中存的第i个元素就是a；
        即keys[i]=key, pq[a]=i, qp[i]=a。qp负责维护keys数组的下标i和索引优先队列pq的下标a的对应关系。
        因此pq与qp的逆序关系体现在： pq[qp[i]] = i  或  qp[pq[a]] = a
        """
        swap = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def sink(self, k):
        """
        下沉是由于删除最大值后，末尾元素暂时在根结点位置，若此时子结点比该末尾结点大，则需要调整整个堆的顺序
        首先结点位置为k时，其子结点位置为2k/2k+1，找到二叉堆子结点中较大者，再进行比较，或下沉或停止
        """
        while 2 * k <= self.N:
            j = 2 * k
            # 保证下沉时比较的都是左右子结点中最大的一个
            if j < self.N and self.less(j, j + 1):
                j += 1
            # 当子结点小于等于时停止
            if self.less(k, j):
                self.exch(k, j)
                k = j
            else:
                break

    def swim(self, k):
        """
        上浮是由于新结点比其父结点更大，因此需要移动到合适的位置
        结点位置为k时，其父结点的位置为 k//2
        """
        while k > 1 and self.less(k // 2, k):
            self.exch(k // 2, k)
            k = k // 2

    def __str__(self):
        return " N is... {} \n keys is... {} \n pq is... {} \n qp is... {} ".format(self.N, self.keys, self.pq, self.qp)
