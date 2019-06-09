class Node:

    def __init__(self, key, val, next_node):
        self.key = key
        self.val = val
        self.next = next_node


class STKeyIterator:

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            key = self.current.key
            self.current = self.current.next
            return key


class STValueIterator:

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        else:
            val = self.current.val
            self.current = self.current.next
            return val
