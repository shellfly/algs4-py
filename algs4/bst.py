"""
   Execution:    python bst.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/32bst/tinyST.txt  
 
   A symbol table implemented with a binary search tree.
  
   % more tinyST.txt
   S E A R C H E X A M P L E
   
   % python bst.py < tinyST.txt
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


class Node:

    def __init__(self, key, val, N):
        self.key = key
        self.val = val
        self.N = N
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x is None:
            return 0

        return x.N

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        if x is None:
            return

        if x.key > key:
            return self._get(x.left, key)
        elif x.key < key:
            return self._get(x.right, key)
        else:
            return x.val

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val, 1)
        if x.key > key:
            x.left = self._put(x.left, key, val)
        elif x.key < key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def level_order(self):
        """Return the keys in the BST in level order"""
        keys = Queue()
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            x = queue.dequeue()
            if x is None:
                continue

            keys.enqueue(x.key)
            queue.enqueue(x.left)
            queue.enqueue(x.right)
        return keys

    def keys(self):
        """
         Returns all keys in the symbol table
         To iterate over all of the keys in the symbol table named {@code st},
         use the foreach notation: {for key in st.keys}
        """
        queue = Queue()
        self._keys(self.root, queue, self.min(), self.max())
        return queue

    def _keys(self, x, queue, lo, hi):
        if x is None:
            return
        if x.key > lo:
            self._keys(x.left, queue, lo, hi)
        if lo <= x.key <= hi:
            queue.enqueue(x.key)
        if x.key < hi:
            self._keys(x.right, queue, lo, hi)

    def max(self):
        if self.is_empty():
            raise Exception("empty bst")
        return self._max(self.root).key

    def _max(self, x):
        if x.right is None:
            return x

        return self._max(x.right)

    def min(self):
        if self.is_empty():
            raise Exception("empty bst")
        return self._min(self.root).key

    def _min(self, x):
        if x.left is None:
            return x

        return self._min(x.left)

    def floor(self, key):
        x = self._floor(self.root, key)
        if x is None:
            return x
        else:
            return x.key

    def _floor(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        elif x.key > key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def ceiling(self):
        x = self._ceiling(self.root, key)
        if x is None:
            return x
        else:
            return x.key

    def _ceiling(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        elif x.key < key:
            return self._ceiling(x.left, key)
        t = self._ceiling(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def select(self, k):
        return self._select(self.root, k).key

    def _select(self, x, k):
        if x is None:
            return
        t = self._size(x.left)
        if t > k:
            return self._select(x.left, k)
        elif t < k:
            return self._select(x.right, k - t - 1)
        else:
            return x

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, x, key):
        if x is None:
            return 0

        if x.key > key:
            return self._rank(x.left, key)
        elif x.key < key:
            return 1 + self._size(x.left) + self._rank(x.right, key)
        else:
            return self._size(x.left)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x is None:
            return None

        if x.key > key:
            x.left = self._delete(x.left, key)
        elif x.key < key:
            x.right = self._delete(x.right, key)
        else:
            if x.right is None:
                return x.left
            if x.left is None:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._deleteMin(t.right)
            x.left = t.left

    def delete_min(self):
        self.root = self._deleteMin(self.root)

    def _delete_min(self, x):
        if x.left is None:
            return x.right
        x.left = self._deleteMin(x.left)
        x.N = self._size(x.left) + self._size(x.right) + 1
        return x

    def is_empty(self):
        return self.root == None


if __name__ == '__main__':
    import sys

    st = BST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1
    for s in st.level_order():
        print(s + " " + str(st.get(s)))
    print()
    for s in st.keys():
        print(s + " " + str(st.get(s)))
