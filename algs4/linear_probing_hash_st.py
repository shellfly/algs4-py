"""
   Execution:    python linear_probing_hash_st.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/33balanced/tinyST.txt

   A symbol table implemented using a linear probing hash.
   This is the 2-3 version.

   % more tinyST.txt
   S E A R C H E X A M P L E

   % python linear_probing_hash_st.py < tinyST.txt
   A 8
   C 4
   E 12
   H 5
   L 11
   M 9
   P 10
   R 3
   S 0
   X 7
"""
from algs4.queue import Queue


class LinearProbingHashST:
    INIT_CAPACITY = 4

    def __init__(self, m=None):
        self.n = 0  # key size
        self.m = m or LinearProbingHashST.INIT_CAPACITY  # hash table size
        self.keys = [None for _ in range(m)]
        self.vals = [None for _ in range(m)]

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.m

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

    def get(self, key):
        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.vals[i]
            i = (i + 1) % self.m

        return None

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        # double table size if 50% full
        if (self.n >= self.m / 2):
            self.resize(2 * self.m)

        i = self.hash(key)
        while self.keys[i] is not None:
            if self.keys[i] == key:
                self.vals[i] = val
                return
            i = (i + 1) % self.m
        self.keys[i] = key
        self.vals[i] = val
        self.n += 1

    def delete(self, key):
        if not self.contains(key):
            return

        i = self.hash(key)
        while self.keys[i] != key:
            i = (i + 1) % self.m
        self.keys[i] = None
        self.vals[i] = None

        # rehash all keys in same cluster
        i = (i + 1) % self.m
        while self.keys[i] is not None:
            key_to_hash = self.keys[i]
            val_to_hash = self.vals[i]
            self.keys[i] = None
            self.vals[i] = None
            self.n -= 1
            self.put(key_to_hash, val_to_hash)
            i = (i + 1) % self.m

        self.n -= 1
        # halves size of array if it's 12.5% full or less
        if self.n > 0 and self.n <= self.m / 8:
            self.resize(self.m / 2)

    def resize(self, capacity):
        tmp = LinearProbingHashST(capacity)
        for i in range(self.m):
            if self.keys[i] is not None:
                tmp.put(self.keys[i], self.vals[i])

        self.m = tmp.m
        self.keys = tmp.keys
        self.vals = tmp.vals

if __name__ == '__main__':
    import sys

    st = LinearProbingHashST(100)
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for s in st.keys:
        if s:
            print(s + " " + str(st.get(s)))
