# coding:utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.sorts.sort_example import Example


class Selection(Example):
    """
    选择排序：不断选择剩余元素中的最小者
    1，找到数组中最小的元素，与数组第一个元素交换位置
    2，在剩下的元素中找到最小的元素，与数组第二个元素交换位置

    N²/2比较和N次交换
    运行时间和输入无关，输入有序、无序时间相同
    交换次数最少，与数组大小是线性关系
    """
    def sort(self, collection):
        N = len(collection)
        for i in range(N):
            min_index = i
            for j in range(i+1, N):
                if self.less(collection[j], collection[min_index]):
                    min_index = j
            self.exch(collection, i, min_index)

        return collection


class Insertion(Example):
    """
    插入排序：将每一个元素插入到其他已经有序的元素中的适当位置。
    为了给要插入的元素腾出空间，需要将其余所有元素在插入前右移一位。
    与选择排序一致，当前索引左边的所有元素有序，右边位置不确定。

    对于随机排列的长度为N且主键不重复的数组，
    平均N²/4次比较+平均N²/4次交换，最坏平均N²/2次比较+平均N²/2次交换，最优N-1次比较+0次交换
    运行时间取决于输入的初始顺序
    有序情况下只要比较，无需交换
    插入排序能在线性时间内发现数组是否有序，由于<=符号，元素全部相同情况也是如此。
    """
    def sort(self, collection):
        N = len(collection)
        for i in range(1, N):
            j = i
            while j > 0 and self.less(collection[j], collection[j-1]):
                self.exch(collection, j, j-1)
                j -= 1

        return collection

    """
    插入排序对如下部分有序的数组很有效（倒置数小于数组大小某个倍数为部分有序）：
    1，数组中每个元素距离它最终位置较近
    2，一个有序的大数组接一个小数组
    3，数组中只有几个元素的位置不正确
    
    上述三种情况都说明同一个条件，数组中需要倒置的数量较少。
    
    插入排序需要的交换操作和数组中倒置的数量相同，
    需要比较的次数大于等于倒置的数量，小于等于倒置的数量+N-1
    注意： EXAMPLE 有11对倒置
    """

    # 改进1，减少交换次数  --> 算法第四版习题 2.1.25
    # 这里实际是拿当前值与左边各个索引值做比较，若小于，则将左侧值大的索引+1
    # 元素实际移动路径与原插入排序无区别，但由于tmp临时变量，减少了数组的访问次数
    def sort2(self, collection):
        N = len(collection)
        for i in range(1, N):
            tmp = collection[i]
            j = i
            while j > 0 and self.less(tmp, collection[j-1]):
                collection[j] = collection[j-1]
                j -= 1
            collection[j] = tmp

        return collection

    # 改进2，规避边界测试，插入排序哨兵 --> 算法第四版习题 2.1.24
    def sort3(self, collection):
        N = len(collection)

        min_index = 0
        for i in range(1, N):
            if self.less(collection[i], collection[min_index]):
                min_index = i
        self.exch(collection, min_index, 0)

        for i in range(2, N):
            tmp = collection[i]
            j = i
            while self.less(tmp, collection[j - 1]): # 此时无需判断j>0
                collection[j] = collection[j - 1]
                j -= 1
            collection[j] = tmp

        return collection


class Shell(Example):
    """
    前面已经提到，插入排序对部分有序的数组是比较有效的
    希尔排序的思想是使数组中任意间隔为h的元素都是有效的（h有效数组）
    希尔排序由于权衡了子数组的规模和有序性。

    官方例子中规模因子为3，关于局部有序性如下：（注意这里的局部有序并不严谨，仅为加深理解）
    由于规模因子为3，初始h会接近N/3附近。
    先做极端假设的实例，此时假设初始三部分数据形如[大, 小, 未知],即恰好初始h的左侧均大于右侧部分，
    这样第一层外循环在走完"大"部分的数据后，会使得初始h索引两侧的约N/3数据相对有序。即会倾向于[小, 大, 未知]
    第一层外循环结束后，h = h/3，此时再关注"小"部分数据，几乎又会重复上述过程。
    经过类似过程完成数组的部分有序

    希尔排序时间复杂度：O(n^(1.3—2))，官方建议中等大小数组可临时使用
    """
    def sort(self, collection):
        N = len(collection)
        h = 1
        while h < N/3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h and self.less(collection[j], collection[j - h]):
                    self.exch(collection, j, j-h)
                    j -= h
            h = int(h/3)

        return collection


class Merge(Example):
    """
    归并排序：先递归地将大数组分成两半分别排序，然后将子结果归并起来

    优点：将任意长度为N的数组排序所需时间和NlgN成正比
    理解为树，分裂完成后有n层，对于0~n-1之间自顶向下的第k层，有2^k个子数组，
    每个数组长度为2^(n-k)，因此归并操作最多每个需要2^(n-k)次比较
    所以每层需要2^k * 2^(n-k) = 2^n，共n层
    缺点：所需额外空间与N成正比
    """

    def sort(self, collection):
        def merge(left, right):
            res = []
            # 若左右有一为空，则剩下不为空的集合中都是已排序的较大的元素，直接添加到尾部即可
            while left and right:
                res.append(left.pop(0) if left[0] <= right[0] else right.pop[0])
            return res + left + right

        if len(collection) <= 1:
            return collection
        mid = len(collection) // 2

        return merge(self.sort(collection[:mid]), self.sort(collection[mid:]))





