from algs4.utils.st import Node, STKeyIterator


class BinarySearchST:

    def __init__(self):
        self.keys = []
        self.vals = []
        self.size = 0

    def contains(self, key):
        x = self.first
        while x:
            if key == x.key:
                return True
            x = x.next
        return False

    def rank(self, key):
        lo = 0
        hi = self.size - 1
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = lo + 1
            else:
                return mid
        return lo

    def get(self, key):
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            return self.vals[i]
        else:
            return None

    def put(self, key, val):
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            self.vals[i] = val
            return

        self.keys.append(key)
        self.vals.append(val)
        j = self.size - 1
        while j > i:
            self.keys[j] = self.keys[j - 1]
            self.vals[j] = self.vals[j - 1]
        self.keys[i] = key
        self.vals[i] = val
        self.size += 1

    def delete(self, key):
        i = self.rank(key)
        if i < self.size and self.keys[i] == key:
            self.size -= 1
            for j in range(i, self.size):
                self.keys[j] = self.keys[j + 1]
                self.vals[j] = self.vals[j + 1]
            self.keys[-1] = None
            self.vals[-1] = None

    def is_empty(self):
        return self.size == 0

    def min(self):
        return self.keys[0]

    def max(self):
        return self.keys[-1]

    def select(self, k):
        return self.keys[k]

    def ceiling(self, key):
        i = self.rank(key)
        if i == self.size:
            return None

        return self.keys[i]

    def floor(self, key):
        i = self.rank(key)
        if i == 0:
            return None
        return self.keys[i - 1]
