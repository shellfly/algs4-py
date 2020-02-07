
"""
Execution:    python bag.py < input.txt

% more tobe.txt
to be or not to - be - - that - - - is

% python bag.py < tobe.txt
to be or not to - be - - that - - - is
"""

from algs4.utils.linklist import Node, LinkIterator


class Bag:

    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = Node(item, oldfirst)
        self.n += 1


if __name__ == '__main__':
    import sys
    for line in sys.stdin:
        bag = Bag()
        for item in line.split():
            bag.add(item)
        print("size of bag = ", bag.size())
        for i in bag:
            print(i)
