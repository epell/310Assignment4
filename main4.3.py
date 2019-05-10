# Project:  Linked List Queue
# Course:   CSC-310
# Author:   Ethan Pellittiere
# Date:     2/23/19


class List:
    datum = None
    nextNode = None

    def __init__(self, datum, nextNode = None):
        self.datum = datum
        self.nextNode = nextNode


class ListQueue:
    headNode = None
    nodes = []

    def __init__(self, headNode = None):
        self.headNode = headNode

    def enqueue(self, datum):
        if self.is_empty():
            self.headNode = self.list_append(self.nodes, List(datum))

        else:
            current = self.headNode
            while 1:
                if current.nextNode is None:
                    current.nextNode = self.list_append(self.nodes,(List(datum)))
                    break
                current = current.nextNode

    def dequeue(self):
        d = self.headNode.datum
        self.headNode = self.headNode.nextNode
        return d

    def first(self):
        return self.headNode.datum

    def len(self):
        current = self.headNode
        len = 1
        while 1:
            if current.nextNode is None:
                break
            current = current.nextNode
            len += 1
        return len

    def is_empty(self):
        if self.headNode is None:
            return True
        return False

    def list_append(self, lst, data):
        lst.append(data)
        return data

    def search(self, val):
        current = self.headNode
        while 1:
            if current.datum == val:
                return True
            if current.nextNode is None:
                return False
            current = current.nextNode


def main():
    LQ = ListQueue()
    print("Is empty? (T): " + str(LQ.is_empty()))
    LQ.enqueue(1)
    print("First Value: (1): " + str(LQ.first()))
    LQ.enqueue(2)
    LQ.enqueue(3)
    LQ.enqueue(4)
    LQ.enqueue(5)
    print("Length (5): " + str(LQ.len()))
    print("Dequeue (1): " + str(LQ.dequeue()))
    print("Length (4): " + str(LQ.len()))
    print("Search 3 (T): " + str(LQ.search(3)))
    print("Search 7 (F): " + str(LQ.search(7)))

main()
