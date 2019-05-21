"""
首先需设计好队列API
Queue() --> 创建空队列
def enqueue(Item item) -> Unit , 添加一个元素
def dequeue() -> Item , 删除最早添加的元素
def isEmpty() -> Boolean , 判断队列是否为空
def size() -> Int , 队列中元素的数量
"""


class Queue():

    def __init__(self):
        self.entries = []
        self.length = 0
        self.front = 0

    def __str__(self):
        """返回一个对象的描述信息"""
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    """ enqueue """
    def put(self, item):
        self.entries.append(item)
        self.length += 1

    """ dequeue """
    def get(self):
        if self.length:
            self.length = self.length - 1
            dequeued = self.entries[self.front]
            self.front -= 1
            self.entries = self.entries[self.front:]
        else:
            dequeued = None
        return dequeued

    """ 队列循环rotation n次 """
    def rotate(self, rotation):
        for i in range(rotation):
            self.put(self.get())

    """ 返回队首元素 """
    def front(self):
        return self.entries[0]

    def size(self):
        return self.length







