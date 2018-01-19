from algs4.utils.st import Node, STKeyIterator


class SequentialSearchST:

    def __init__(self):
        self.first = None
        self.size = 0

    def contains(self, key):
        x = self.first
        while x:
            if key == x.key:
                return True
            x = x.next
        return False

    def get(self, key):
        x = self.first
        while x:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = self.first
        while x:
            if key == x.key:
                x.val = val
                return
            x = x.next
        self.first = Node(key, val, self.first)
        self.size += 1

    def delete(self, key):
        prev = None
        curr = self.first
        while curr:
            if key == curr.key:
                if prev:
                    prev.next = curr.next
                else:
                    self.first = curr.ext
                self.size -= 1
            prev = curr
            curr = curr.next

    def keys(self):
        return STKeyIterator(self.first)
