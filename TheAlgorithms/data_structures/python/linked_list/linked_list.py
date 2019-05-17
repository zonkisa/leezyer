"""
链表:
一种递归的数据结构
或为空，或指向一个结点的引用，该结点含有一个泛型元素和一个指向另一条链表的引用
其中结点是一个可能含有任意类型数据的抽象实体
"""
from __future__ import print_function


# 嵌套类的形式定义抽象实体,结点值data为泛型类型，初始化结点的引用指向为空
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
链表API
在表尾插入结点、在表头插入结点、链表遍历(大小)、删除表头结点、删除表尾结点、空链表检查、链表反转

较难：删除指定结点、在指定结点前插入一个新结点
"""
class Linked_List:
    def __init__(self):
        self.Head = None

    def insert_tail(self, data):
        """
        表尾插入结点：若链表为空，即为表头插入结点；否则遍历链表，令尾部元素引用指向Node(data)
        """
        if not self.Head:
            self.insert_tail(data)
        else:
            tmp = self.Head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(data)

    def insert_head(self, data):
        """
        表头插入：即表头元素为新结点，新结点指向旧表头元素
        """
        newNode = Node(data)
        if self.Head:
            newNode.next = self.Head
        self.Head = newNode

    """ 打印链表(链表的遍历及大小)  """
    def printList(self):
        tmp = self.Head
        ct = 1 if tmp else 0
        print("index is ", ct, "--->", tmp.data)
        while tmp.next:
            ct += 1
            tmp = tmp.next
            print("index is ", ct, "--->", tmp.data)

        print("size is ", self.size())

    def size(self):
        if not self.Head:
            return 0
        tmp = self.Head
        ct = 1
        while tmp.next:
            ct += 1
            tmp = tmp.next
        return ct

    def delete_head(self):
        """
        删除表头元素，令表头指向下一个元素来更新整个链表的引用信息
        返回被删除的表头元素
        """
        tmp = self.Head
        if tmp:
            self.Head = self.Head.next
            tmp.next = None
        return tmp

    def delete_tail(self):
        """
        删除链表最尾元素并将其返回
        注意需要更新整个链表引用信息,需要注意链表只有表头一个元素的特殊情况
        """
        res, tmp = self.Head, self.Head #避免混淆，多创建一次
        if self.Head:
            if self.Head.next is None:
                self.Head = None
            else:
                while tmp.next.next is not None:
                    tmp = tmp.next
                # 倒数第二个元素处跳出循环
                res = tmp.next
                tmp.next = None
                # tmp.next, tmp = None, tmp.next

        return res

    def isEmpty(self):
        return self.Head is None

    def reverse(self):
        """
        反转链表
        需新建空结点链表并维护
        循环更新链表有三点需要注意：
        1,循环体中，current应该始终要比pre领先一个结点位置 curr.next=pre
        2,由于反转,需要完成pre.next=pre链表顺序，所以pre需要更新为curr，衔接上面curr.next=pre
        3,循环体中curr需要接着更新，遍历下一个结点
        """
        previous = None # 预置新链表
        current = self.Head

        while current:
            next_node = current.next

            current.next = previous
            previous = current

            current = next_node
        # 最后一步，更新链表头指针
        self.Head = previous

    def delete(self, k):
        """
        1.3.20 删除链表第k个元素
        将链表k-1引用指向k+1处结点, 即x.next = x.next.next
        """
        if k < 0:
            return None
        else:
            i = 1
            new = None
            curr = self.Head
            while i < k and curr is not None:
                i += 1
                new = curr
                curr = curr.next

            # curr不为None则为当前链表第k个元素
            if curr is not None:
                new.next = curr.next #更新链表
                curr.next = None #返回指定位置结点
            return curr

    def find(self, key):
        """
        1.3.21 检查链表是否存在值为key的结点
        """
        tmp = self.Head
        while tmp:
            if tmp.data == key:
                return True
            else:
                tmp = tmp.next

        return False

    """ 方便后续操作结点信息 """
    def make_node(self, k):
        if k < 1:
            return None
        i = 1
        curr = self.Head
        while i < k and curr:
            curr = curr.next
            i += 1
        return curr

    def removeAfter(self, node):
        """
        1.3.24 删除给定结点的后一个结点
        此处是结合make_node实现，需要传入原lst对象中的结点元素
        实际是遍历链表至指定结点处进行删除操作
        若node是指定按匹配结点值进行删除，则无需make_node取原lst的结点元素
        """

        if node and node.next:
            if node.next.next:
                node.next = node.next.next
            else:
                node.next = None




def make_lst(list):
    lst = Linked_List()
    if not list:
        lst.Head = None
    else:
        pre = Node(list[0])
        lst.Head = pre
        for i, value in enumerate(list):
            if i > 0:
                curr = Node(list[i])
                pre.next = curr
                pre = curr

    return lst


def printNode(node):
    if node.next:
        print("node data is ", node.data, ", node next data is ", node.next.data)
    else:
        print("node data is ", node.data, ", node next is None")


def testMakeLst(ls):
    lst = make_lst(ls)
    lst.printList()


def testDelete(lst):
    printNode(lst.delete(3))
    lst.printList()


def testFind(lst, data):

    print(lst.find(data))
    # lst.printList()


def testRemoveAfter(node):
    lst.removeAfter(node)


if __name__ == '__main__':
    lst = make_lst([1, 2, 3, 4, 5])
    print("primary is ")
    lst.printList()

    # testMakeLst([1, 2, 333, 4, 5])
    # testDelete(lst)
    # testFind(lst, 3)
    a = lst.make_node(3)
    testRemoveAfter(a)
    print("test result is ")
    lst.printList()










