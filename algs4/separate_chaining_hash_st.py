"""
   Execution:    python separate_chaining_hash_st.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/33balanced/tinyST.txt

   A symbol table implemented using a separate chaining hash.
   This is the 2-3 version.

   % more tinyST.txt
   S E A R C H E X A M P L E

   % python separate_chaining_hash_st.py < tinyST.txt
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
from algs4.sequential_search_st import SequentialSearchST


class SeparateChainingHashST:
    INIT_CAPACITY = 4

    def __init__(self, m=None):
        self.n = 0  # key size
        self.m = m or SeparateChainingHashST.INIT_CAPACITY  # hash table size
        self.st = [SequentialSearchST() for _ in range(m)]

    def hash(self, key):
        return (hash(key) & 0x7FFFFFFF) % self.m

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

    def get(self, key):
        return self.st[self.hash(key)].get(key)

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        # double table size if 50% full
        if (self.n >= self.m * 10):
            self.resize(2 * self.m)

        self.st[self.hash(key)].put(key, val)

    def keys(self):
        """
         Returns all keys in the symbol table
         To iterate over all of the keys in the symbol table named {@code st},
         use the foreach notation: {for key in st.keys}
        """
        queue = Queue()
        for s in self.st:
            for key in s.keys():
                queue.enqueue(key)
        return queue

    def delete(self, key):
        self.st[self.hash(key)].delete(key)

    def resize(self, chains):
        tmp = SeparateChainingHashST(chains)
        for i in range(self.m):
            for key in self.st[i].keys():
                tmp.put(key, self.st[i].get(key))
        self.m = tmp.m
        self.n = tmp.n
        self.st = tmp.st


if __name__ == '__main__':
    import sys

    st = SeparateChainingHashST(100)
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for s in st.keys():
        print(s + " " + str(st.get(s)))
