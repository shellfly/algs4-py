class Node:

    def __init__(self, item, nextItem):
        self.item = item
        self.next = nextItem


class LinkIterator:

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            item = self.current.item
            self.current = self.current.next
            return item
