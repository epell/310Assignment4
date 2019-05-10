# Project:  Queues and Linked Lists
# Course:   CSC-310
# Author:   Ethan Pellittiere
# Date:     2/23/19


class MyCircularDeque:
    empty = True
    full = False
    front = 0
    last = 0
    size = 0
    queue = []

    def __init__(self, size):
        self.size = size
        self.front = 0
        self.last = size-1
        for x in range(size):
            self.queue.append(0)

    def insertFront(self, data):
        if self.full:
            return False
        self.queue[self.front] = data
        if self.front % self.size == self.last % self.size:
            self.full = True
        self.front = (self.front+1) % self.size
        self.empty = False
        return True

    def insertLast(self, data):
        if self.full:
            return False
        self.queue[self.last] = data
        if self.front % self.size == self.last % self.size:
            self.full = True
        self.last = (self.last - 1) % self.size
        self.empty = False
        return True

    def deleteFront(self):
        if self.empty:
            return False
        self.front = (self.front-1) % self.size
        if self.front % self.size == self.last % self.size+1:
            self.empty = True
        self.full = False
        return True

    def deleteLast(self):
        if self.empty:
            return False
        self.last = (self.last+1) % self.size
        if not self.full:
            if self.front % self.size == self.last % self.size+1:
                self.empty = True
        self.full = False
        return True

    def getFront(self):
        if self.empty:
            return -1
        return self.queue[(self.front-1) % self.size]

    def getRear(self):
        if self.empty:
            return -1
        return self.queue[(self.last + 1) % self.size]

    def isEmpty(self):
        return self.empty

    def isFull(self):
        return self.full


def main():
    q = MyCircularDeque(4)
    print("Add 0 to start: " + str(q.insertFront(0)))
    print("Get first value (0): " + str(q.getFront()))
    print("Get last value (0): " + str(q.getRear()))
    print("Add 3 to last value: " + str(q.insertLast(3)))
    print("Fill in rest of values: " + str(q.insertLast(2)) + str(q.insertFront(1)))
    print("Is queue full? (T): " + str(q.isFull()))
    print("Is queue empty? (F): " + str(q.isEmpty()))
    print("Remove first value: " + str(q.deleteFront()))
    print("Check first value (0): " + str(q.getFront()))
    print("Remove last value: " + str(q.deleteLast()))
    print("Check last value (3): " + str(q.getRear()))
    print("Remove two more values: " + str(q.deleteLast()) + str(q.deleteLast()))
    print("Is queue empty?(T): " + str(q.isEmpty()))
    print("Is queue full?(F): " + str(q.isFull()))

main()

