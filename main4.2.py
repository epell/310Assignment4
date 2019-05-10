# Project:  Linked Lists
# Course:   CSC-310
# Author:   Ethan Pellittiere
# Date:     2/23/19


class Node:
    nextNode = None
    datum = 0

    def __init__(self, datum, nextNode):
        self.datum = datum
        self.nextNode = nextNode


def main():
    list_1_head = Node(1, None)
    list_1_1 = Node(2, None)
    list_1_2 = Node(4, None)
    list_1_head.nextNode = list_1_1
    list_1_1.nextNode = list_1_2

    list_2_head = Node(1, None)
    list_2_1 = Node(3, None)
    list_2_2 = Node(4, None)
    list_2_head.nextNode = list_2_1
    list_2_1.nextNode = list_2_2

    print("List 1")
    current_1 = list_1_head
    while 1:
        print(current_1.datum, end="")
        if current_1.nextNode is None:
            print()
            break
        current_1 = current_1.nextNode
        print(", ", end="")

    print("List 2")
    current_2 = list_2_head
    while 1:
        print(current_2.datum, end="")
        if current_2.nextNode is None:
            print()
            break
        current_2 = current_2.nextNode
        print(", ", end="")

    current_1 = list_1_head
    current_2 = list_2_head

    if current_1.datum < current_2.datum:
        sorted_head = current_1
        current_1 = current_1.nextNode
    else:
        sorted_head = current_2
        current_2 = current_2.nextNode
    sorted_current = sorted_head

    while 1:
        print("D1: " + str(current_1.datum) + " D2: " + str(current_2.datum))
        if current_1.datum < current_2.datum:
            sorted_current.nextNode = current_1
            if current_1.nextNode is None:
                sorted_current.nextNode = current_2
                break
            current_1 = current_1.nextNode
        else:
            sorted_current.nextNode = current_2
            if current_2.nextNode is None:
                sorted_current.nextNode = current_1
                break
            current_2 = current_2.nextNode
        sorted_current = sorted_current.nextNode

    print("Sorted List")
    sorted_current = sorted_head

    while 1:
        print(sorted_current.datum, end="")
        if sorted_current.nextNode is None:
            print()
            break
        sorted_current = sorted_current.nextNode
        print(", ", end="")


main()
