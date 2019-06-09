"""
A generic stack implemented using a singly linked list.

% more tobe.txt 
to be or not to - be - - that - - - is

% python stack.py < tobe.txt
to be not that or be (2 left on stack)
"""

from algs4.utils.linklist import Node, LinkIterator


class Stack:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(i for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def push(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow")
        else:
            item = self.first.item
            self.first = self.first.next
            self.n -= 1
            return item


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        stack = Stack()
        for item in line.split():
            if item != "-":
                stack.push(item)
            elif not stack.is_empty():
                print(stack.pop() + " ", end='')
        print("(%d left on stack)" % stack.size())
