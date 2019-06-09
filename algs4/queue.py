"""
Execution:    python queue.py < input.txt

% more tobe.txt 
to be or not to - be - - that - - - is

% python queue.py < tobe.txt
to be or not to be (2 left on queue)
"""

from algs4.utils.linklist import Node, LinkIterator


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def __str__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def enqueue(self, item):
        oldlast = self.last
        self.last = Node(item, None)
        if self.is_empty():
            self.first = self.last
        else:
            oldlast.next = self.last
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue empty")
        else:
            item = self.first.item
            self.first = self.first.next
            if self.is_empty():
                self.last = None
            self.n -= 1
            return item


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        queue = Queue()
        for item in line.split():
            if item != "-":
                queue.enqueue(item)
            elif not queue.is_empty():
                print(queue.dequeue() + " ", end='')
        print("(%d left on queue)" % queue.size())
