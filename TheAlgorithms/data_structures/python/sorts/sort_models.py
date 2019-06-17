# coding:utf-8
from __future__ import print_function
from TheAlgorithms.data_structures.python.sorts.sort_example import Example
from math import log, pow
import random


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

    def sort_outer(self, collection, lo, hi):
        N = hi - lo + 1
        for i in range(lo+1, N):
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
            h = h//3

        return collection


class Merge(Example):
    """
    归并排序：先递归地将大数组分成两半分别排序，然后将子结果归并起来

    优点：将任意长度为N的数组排序所需时间和NlgN成正比
    理解为树，分裂完成后有n层，对于0~n-1之间自顶向下的第k层，有2^k个子数组，
    每个数组长度为2^(n-k)，因此归并操作最多每个需要2^(n-k)次比较
    所以每层需要2^k * 2^(n-k) = 2^n，共n层,即 NlgN次比较
    缺点：所需额外空间与N成正比

    对于长度为N的任意数组，自顶向下的归并排序最多需要访问数组6NlgN次

    每一次归并操作最多需要访问数组6N次（2N次复制、2N次移动、最多2N次比较）
    """

    def sort(self, collection):
        """
        比较原始的归并排序，每次merge过程前都需要额外空间 res=[]，大小与left、right有关
        """
        def merge(left, right):
            res = []
            # 若左右有一为空，则剩下不为空的集合中都是已排序的较大的元素，直接添加到尾部即可
            while left and right:
                res.append(left.pop if left[0] <= right[0] else right.pop)
            return res + left + right

        if len(collection) <= 1:
            return collection
        mid = len(collection) // 2

        return merge(self.sort(collection[:mid]), self.sort(collection[mid:]))

    def sort2(self, collection):
        """
        原地归并排序，仅需初始复制aux数组
        """
        def sort_sup(a, lo, hi):
            if hi <= lo:
                return a
            mid = lo + (hi - lo)//2
            sort_sup(a, lo, mid)
            sort_sup(a, mid+1, hi)
            merge_sup(a, lo, mid, hi)

        def merge_sup(a, lo, mid, hi):
            i, j = lo, mid + 1
            # 这里hi是具体的索引，必须要取到，因此在range中hi+1
            for k in range(lo, hi+1):
                aux[k] = a[k]
            for k in range(lo, hi+1):
                # 左端索引大于mid，说明左边较小的元素已经取完，需要取右半边元素
                if i > mid:
                    a[k] = aux[j]
                    j += 1
                # 右端索引小于mid，说明右边较小的元素已经取完，需要取左半边元素
                elif hi < j:
                    a[k] = aux[i]
                    i += 1
                # 左右均有元素，且此时右半区起始值小于左半区起始值，先去较小的索引，即右区
                elif self.less(aux[j], aux[i]):
                    a[k] = aux[j]
                    j += 1

                # 同上
                else:
                    a[k] = aux[i]
                    i += 1

        aux = [0] * len(collection)
        sort_sup(collection, 0, len(collection)-1)

        return collection

    def sort3(self, collection):
        """
        快速归并排序，习题2.2.10
        改进1：实现一个merge方法，按降序将数组a的后半部分复制到数组aux，然后将其归并回数组a中，无需考虑半区是否取完
        """
        def sort_sup(a, lo, hi):
            if hi <= lo:
                return a
            mid = lo + (hi - lo)//2
            sort_sup(a, lo, mid)
            sort_sup(a, mid+1, hi)
            merge_sup(a, lo, mid, hi)

        def merge_sup(a, lo, mid, hi):
            for k in range(lo, mid+1):
                aux[k] = a[k]
            for k in range(mid+1, hi+1):
                aux[k] = a[hi-k+mid+1] # 取右半区倒序索引

            i, j = lo, hi
            # 此时i,j都是各自半区最小值的索引。
            # 由于右半区已经倒序，无论i++或j--都是从两头较小值开始比较，向中间较大值靠拢，消除了半区的界限，mid值也就不重要了。
            for k in range(lo, hi+1):
                if self.less(aux[j], aux[i]):
                    a[k] = aux[j]
                    j -= 1
                else:
                    a[k] = aux[i]
                    i += 1

        aux = [0] * len(collection)
        sort_sup(collection, 0, len(collection)-1)

        return collection

    def sort4(self, collection):
        """
        改进2：merge前判断数组是否有序  习题2.2.8
        若a[mid] <= a[mid+1]，则视为已经有序，无需调用merge方法
        此时归并排序处理一个已经有序的数组所需的比较次数是线性级别的
        """
        def sort_sup(a, lo, hi):
            if hi <= lo:
                return
            mid = lo + (hi - lo)//2
            sort_sup(a, lo, mid)
            sort_sup(a, mid+1, hi)
            if self.less(a[mid+1], a[mid]): # 右半区小于左半区时再调用merge
                merge_sup(a, lo, mid, hi)

        def merge_sup(a, lo, mid, hi):
            for k in range(lo, mid+1):
                aux[k] = a[k]
            for k in range(mid+1, hi+1):
                aux[k] = a[hi-k+mid+1] # 取右半区倒序索引

            i, j = lo, hi
            # 此时i,j都是各自半区最小值的索引。
            # 由于右半区已经倒序，无论i++或j--都是从两头较小值开始比较，向中间较大值靠拢，消除了半区的界限，mid值也就不重要了。
            for k in range(lo, hi+1):
                if self.less(aux[j], aux[i]):
                    a[k] = aux[j]
                    j -= 1
                else:
                    a[k] = aux[i]
                    i += 1

        aux = [0] * len(collection)
        sort_sup(collection, 0, len(collection)-1)

        # return collection

    # TODO 未通过压测
    def sort5(self, collection):
        """
        改进3：a,小规模数组使用插入排序;  b,merge前判断数组是否有序；   c,在递归中交换参数避免数组复制
        小规模的界定：算法第四版归并排序章节的命题G已给出证明，归并最多需要6NlgN次访问数组（2N复制、2N移动交换、最多2N次比较）
                    插入排序最优N-1次比较+0次交换，见https://yidao620c.iteye.com/blog/1946147
        对于小规模数组例子，见Quick._sort，官方给出规模因子为5~15，相应地需要更改插入排序的传参，见Insertion._sort_outer
        习题2.2.11
        """
        def sort_sup(a, lo, hi):
            if hi <= lo:
                return
            # if hi - lo <= insertFractor:
            #     Insertion().sort2(a)
            #     return
            mid = lo + (hi - lo)//2
            sort_sup(a, lo, mid)
            sort_sup(a, mid+1, hi)
            if self.less(a[mid+1], a[mid]): # 右半区小于左半区时再调用merge
                merge_sup(a, lo, mid, hi)

        def merge_sup(a, lo, mid, hi):
            for k in range(lo, mid+1):
                aux[k] = a[k]
            for k in range(mid+1, hi+1):
                aux[k] = a[hi-k+mid+1] # 取右半区倒序索引

            i, j = lo, hi
            # 此时i,j都是各自半区最小值的索引。
            # 由于右半区已经倒序，无论i++或j--都是从两头较小值开始比较，向中间较大值靠拢，消除了半区的界限，mid值也就不重要了。
            for k in range(lo, hi+1):
                if self.less(aux[j], aux[i]):
                    a[k] = aux[j]
                    j -= 1
                else:
                    a[k] = aux[i]
                    i += 1

        N = len(collection)
        insertFractor = int(log(N, 2))
        aux = collection.copy()
        sort_sup(collection, 0, N-1)

        return collection


class Quick(Example):
    """
    快速排序：分治，与归并排序互补
    归并排序将数组分成两个子数组分别排序，并将有序的子数组归并以将整个数组排序。递归调用发生在处理整个数组之前，先递归调用sort_sup
    快速排序是当两个子数组都有序时，整个数组即有序。递归调用发生在处理整个数组之后，先对整个数组partition，再递归调用_sort

    优点：内循环简洁，比较次数较少
    缺点：依赖于数组的切分
    复杂度 k*1.39NlgN, 移动数据的次数比归并少
    """

    def sort(self, collection):
        random.shuffle(collection)
        self._sort(collection, 0, len(collection)-1)

    def _sort(self, a, lo, hi):
        if hi <= lo + 7:  # 小数组改用插入排序
            Insertion().sort_outer(a, lo, hi)
            return
        j = self._partition(a, lo, hi)
        self._sort(a, lo, j-1)
        self._sort(a, j+1, hi)

    def _partition(self, a, lo, hi):
        i, j = lo, hi+1
        v = a[lo]
        while True:
            i += 1
            while self.less(a[i], v):
                if i == hi:
                    break
                i += 1

            j -= 1
            while self.less(v, a[j]):
                if j == lo:
                    break
                j -= 1

            if i >= j:
                break  # 根据切分数组的值v已经找到v值应该在的索引j (因为i>=j，因此v值取j正好在i索引值之前，保证左右有序)
            self.exch(a, i, j) # 循环走到这里说明有类似局部极值点的情况，未成功切分数组，需要逐个交换索引，继续循环

        self.exch(a, lo, j) # 更新v值的最终索引

        return j

    def sort2(self, collection):
        """
        习题2.3.17 + 2.3.11
        改进1，设置越界哨兵，在partition中左右边界的判断可以省略
        改进2，修改切分值左右扫描的判断条件，处理切元素值重复的情况
        改进3，给出了局部保持随机性的做法
        """
        random.shuffle(collection)
        large_index = collection.index(max(collection))
        self.exch(collection, large_index, len(collection)-1) # 习题2.3.17,设置右侧哨兵
        # min_index = collection.index(min(collection)) # 由于python索引可以为负，左端哨兵无法设置
        # self.exch(collection, min_index, 0)

        self._sort2(collection, 0, len(collection)-1)

    def _sort2(self, a, lo, hi):
        if hi <= lo + 7:  # 小数组改用插入排序
            Insertion().sort_outer(a, lo, hi)
            return
        # if hi > lo:
        j = self._partition2(a, lo, hi)
        self._sort2(a, lo, j-1)
        self._sort2(a, j+1, hi)

    def _partition2(self, a, lo, hi):
        i, j = lo, hi+1
        v = a[lo] # 此处也可以随机选择一个索引的值作为v，需和lo交换该索引，即在局部随机选取v，而不在最外层。保持随机性
        while True:
            i += 1
            # while self.less(a[i], v):
            while self.less_not_eql(a[i], v): # 避免切分元素值重复，左侧扫描应该在大于等于切分值停下
                i += 1

            j -= 1
            # while self.less(v, a[j]):
            while self.less_not_eql(v, a[j]): # 避免切分元素值重复，右侧扫描应该在小于等于切分值停下
                if j == lo:  # 由于python索引可以为负，左端哨兵无法设置
                    break
                j -= 1

            if i >= j:
                break  # 根据切分数组的值v已经找到v值应该在的索引j (因为i>=j，因此v值取j正好在i索引值之前，保证左右有序)
            self.exch(a, i, j) # 循环走到这里说明有类似局部极值点的情况，未成功切分数组，需要逐个交换索引，继续循环

        self.exch(a, lo, j) # 更新v值的最终索引

        return j

    # TODO 三取样切分 习题2.3.18
    def sort3(self, collection):
        random.shuffle(collection)
        large_index = collection.index(max(collection))
        self.exch(collection, large_index, len(collection) - 1)  # 习题2.3.17,设置右侧哨兵

        self._sort3(collection, 0, len(collection)-1)

    def _sort3(self, a, lo, hi):
        if hi <= lo + 7:  # 小数组改用插入排序
            Insertion().sort_outer(a, lo, hi)
            return
        j = self._partition3(a, lo, hi)
        self._sort3(a, lo, j-1)
        self._sort3(a, j+1, hi)

    def _partition3(self, a, lo, hi):
        setIndex = set()
        while len(setIndex) != 3:
            setIndex.add(random.randint(lo, hi))
        values = [a[q] for q in setIndex]
        Insertion().sort(values)
        medium = lo
        for k in setIndex:
            if a[k] == values[1]:
                medium = k
        self.exch(a, lo, medium)

        i, j = lo, hi+1
        v = a[lo]
        while True:
            i += 1
            while i < hi and self.less_not_eql(a[i], v):
                i += 1
            j -= 1
            while j > lo and self.less_not_eql(v, a[j]):
                j -= 1

            if i >= j:
                break
            self.exch(a, i, j)

        self.exch(a, lo, j)
        return j

    def sort4(self, collection):
        """
        三向切分，将数组分成大于、小于、等于切分元素的三部分
        对于重复元素少的情况比标准二分快排多使用了很多次交换
        见下面sort5 快速三向切分 习题2.3.22
        """
        random.shuffle(collection)
        large_index = collection.index(max(collection))
        self.exch(collection, large_index, len(collection) - 1)  # 习题2.3.17,设置右侧哨兵

        self._sort4(collection, 0, len(collection) - 1)

    def _sort4(self, a, lo, hi):
        # if hi <= lo + 7:
        #     Insertion().sort_outer(a, lo, hi)
        if hi <= lo:
            return
        lt, i, gt = lo, lo+1, hi

        v = a[lo]
        while i <= gt:
            if a[i] < v:
                self.exch(a, lt, i)
                lt += 1
                i += 1
            elif a[i] > v:
                self.exch(a, i, gt)
                gt -= 1
            else:
                i += 1

        self._sort4(a, lo, lt - 1)
        self._sort4(a, gt + 1, hi)

    def sort5(self, collection):
        self._sort5(collection, 0, len(collection)-1)

    def _sort5(self, a, lo, hi):
        N = hi - lo + 1
        insertion_sort_cutoff = 8
        MEDIAN_OF_3_CUTOFF = 40
        if(N <= insertion_sort_cutoff):
            Insertion().sort_outer(a, lo, hi)
            return
        elif N <= MEDIAN_OF_3_CUTOFF:
            m = self.median3(a, lo, lo+N//2, hi)
            self.exch(a, m, lo)
        else:
            eps = N//8
            mid = lo + N // 2
            m1 = self.median3(a, lo, lo+eps, lo+eps+eps)
            m2 = self.median3(a, mid-eps, mid, mid+eps)
            m3 = self.median3(a, hi-eps-eps, hi-eps, hi)
            ninther = self.median3(a, m1, m2, m3)
            self.exch(a, ninther, lo)

        i, j = lo, hi+1
        p, q = lo, hi+1

        v = a[lo]
        while True:
            i += 1
            while i < hi and self.less_not_eql(a[i], v):
                i += 1

            j -= 1
            while j > lo and self.less_not_eql(v, a[i]):
                j -= 1

            if i == j and a[i] == v:
                p += 1
                self.exch(a, p, i)

            if i >= j:
                break
            self.exch(a, i, j)
            if a[i] == v:
                p += 1
                self.exch(a, p, i)
            if a[j] == v:
                q -= 1
                self.exch(a, q, j)

        i = j + 1
        for k in range(lo, p+1):
            self.exch(a, k, j)
            j -= 1
        for k in range(hi, q-1, -1):
            self.exch(a, k, i)
            i += 1

        self._sort5(a, lo, j)
        self._sort5(a, i, hi)

    def median3(self, a, i, j, k):
        pass


