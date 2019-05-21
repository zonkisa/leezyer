from __future__ import print_function
from TheAlgorithms.data_structures.python.linked_list import linked_list
from TheAlgorithms.data_structures.python.linked_list import circular_linked_list


def testHasCircle(lst):
    print(lst.has_circular())


def testIsCircle(lst):
    print(lst.is_circular())


if __name__ == '__main__':
    lst = linked_list.make_circular_list([1, 2, 3])
    # lst = linked_list.make_lst([1, 2, 3, 1])
    lst.printList()
    print("------")
    testHasCircle(lst)
    testIsCircle(lst)


    pass