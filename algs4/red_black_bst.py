"""
   Execution:    python RedBlackBST.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/33balanced/tinyST.txt

   A symbol table implemented using a left-leaning red-black BST.
   This is the 2-3 version.

   % more tinyST.txt
   S E A R C H E X A M P L E

   % python RedBlackBST.py < tinyST.txt
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

    def __init__(self, key, val, color, size):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.color = color
        self.size = size


class RedBlackBST:
    RED = True
    BLACK = False

    def __init__(self):
        self.root = None

    def is_red(self, x):
        if x is None:
            return False
        return x.color == RedBlackBST.RED

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x is None:
            return 0
        return x.size

    def is_empty(self):
        return self.root is None

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, x, key):
        while x is not None:
            if x.key == key:
                return x.val
            elif x.key < key:
                x = x.right
            else:
                x = x.left
        return None

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)
        self.root.color = RedBlackBST.BLACK

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val, RedBlackBST.RED, 1)
        if x.key > key:
            x.left = self._put(x.left, key, val)
        elif x.key < key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val

        # fix-up any right-leaning links
        if self.is_red(x.right) and not self.is_red(x.left):
            x = self.rotate_left(x)
        if self.is_red(x.left) and self.is_red(x.left.left):
            x = self.rotate_right(x)
        if self.is_red(x.left) and self.is_red(x.right):
            self.flip_colors(x)

        x.size = self._size(x.left) + self._size(x.right) + 1
        return x

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RedBlackBST.RED
        x.size = h.size
        h.size = self._size(h.left) + self._size(h.right) + 1
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RedBlackBST.RED
        x.size = h.size
        h.size = self._size(h.left) + self._size(h.right) + 1
        return x

    def flip_colors(self, h):
        """
        flip the colors of a node and its two children
        """

        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def move_red_left(self, h):
        """
        Assuming that h is red and both h.left and h.left.left
        are black, make h.left or one of its children red.
        """
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def move_red_right(self, h):
        """
        Assuming that h is red and both h.right and h.right.left
        are black, make h.right or one of its children red.
        """
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def height(self):
        return self._height(self.root)

    def _height(self, x):
        if x is None:
            return -1
        return 1 + max(self._height(x.left), self._height(x.right))

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

    def Keys(self):
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
        return self._max(self.root).key

    def _max(self, x):
        if x.right is None:
            return x

        return self._max(x.right)

    def min(self):
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
        if key is None:
            raise ValueError("argument is null")

        # if both children of root are black, set root to red
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RedBlackBST.RED

        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = RedBlackBST.BLACK

    def _delete(self, h, key):
        if h is None:
            return None

        if h.key > key:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and h.right is None:
                return None
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)

            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.val = x.val
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)

        return self.balance(h)

    def delete_min(self):
        if self.is_empty():
            raise ValueError("BST underflow")

        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RedBlackBST.RED

        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = RedBlackBST.BLACK

    def _delete_min(self, h):
        if h.left is None:
            return None
        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_red_left(h)

        h.left = self._delete_min(h.left)
        return self.balance(h)

    def balance(self, h):
        if self.is_red(h) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.size = self._size(h.left) + self._size(h.right) + 1
        return h


if __name__ == '__main__':
    import sys

    st = RedBlackBST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1
    for s in st.level_order():
        print(s + " " + str(st.get(s)))
    print()
    for s in st.Keys():
        print(s + " " + str(st.get(s)))
