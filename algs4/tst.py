"""
 *  Execution:    python tst.py < words.txt
 *  Dependencies: StdIn.java
 *  Data files:   https://algs4.cs.princeton.edu/52trie/shellsST.txt
 *
 *  A string symbol table for extended ASCII strings, implemented
 *  using a 256-way trie.
 *
 *  % python tst.py < shellsST.txt
 *  by 4
 *  sea 6
 *  sells 1
 *  she 0
 *  shells 3
 *  shore 7
 *  the 5
 *
"""

from algs4.queue import Queue


class Node:
    def __init__(self):
        self.c = None
        self.val = None
        self.left = None
        self.mid = None
        self.right = None


class TST:
    def __init__(self):
        self.size = 0
        self.root = None

    def char_at(self, s, d):
        return ord(s[d])

    def get(self, key):
        if len(key) == 0:
            raise Exception("key must have length >=1")
        x = self._get(self.root, key, 0)
        if x == None:
            return x
        return x.val

    def _get(self, x, key, d):
        if x == None:
            return None
        c = self.char_at(key, d)
        if c < x.c:
            return self._get(x.left, key, d)
        elif c > x.c:
            return self._get(x.right, key, d)
        elif d < len(key)-1:
            return self._get(x.mid, key, d+1)
        else:
            return x

    def contains(self, key):
        return self.get(key) != None

    def put(self, key, val):
        if not self.contains(key):
            self.size += 1
        elif val == None:
            self.size -= 1
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        c = self.char_at(key, d)
        if x == None:
            x = Node()
            x.c = c
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c > x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key)-1:
            x.mid = self._put(x.mid, key, val, d+1)
        else:
            x.val = val
        return x

    def keys(self):
        queue = Queue()
        self.collect(self.root, "", queue)
        return queue

    def keys_with_prefix(self, prefix):
        queue = Queue()

        x = self._get(self.root, prefix, 0)
        if x == None:
            return
        if x.val != None:
            queue.enqueue(prefix)

        self.collect(x, prefix, queue)
        return queue

    def collect(self, x, prefix, queue):
        if x == None:
            return
        self.collect(x.left, prefix, queue)
        if x.val != None:
            queue.enqueue(prefix+chr(x.c))
        self.collect(x.mid, prefix+chr(x.c), queue)
        self.collect(x.right, prefix, queue)

    def keys_that_match(self, pat):
        q = Queue()
        self.collectMatch(self.root, "", 0,  pat, q)
        return q

    def collectMatch(self, x, prefix, i, pattern, queue):
        if x == None:
            return
        c = self.char_at(pattern, i)
        if chr(c) == "." or c < x.c:
            self.collectMatch(x.left, prefix, i, pattern, queue)
        if chr(c) == "." or c == x.c:
            if i == len(pattern)-1 and x.val != None:
                queue.enqueue(prefix+chr(c))
            if i < len(pattern)-1:
                self.collectMatch(x.mid, prefix+chr(c), i+1, pattern, queue)
        if chr(c) == "." or c > x.c:
            self.collectMatch(x.right, prefix, i, pattern, queue)

    def long_prefix_of(self, query):
        if len(query) == 0:
            return ""
        length = 0
        i = 0
        x = self.root
        while x != None and i < len(query):
            c = self.char_at(query, i)
            if c < x.c:
                x = x.left
            elif c > x.c:
                x = x.right
            else:
                i += 1
                if x.val != None:
                    length = i
                x = x.mid

        return query[:length]

    def delete(self, key):
        self.root = self._put(self.root, key, None)


if __name__ == "__main__":
    import sys
    st = TST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1
    if st.size < 100:
        for key in st.keys():
            print(key, " ", st.get(key))
    print()
    print("longestPrefixOf(\"shellsort\"):")
    print(st.long_prefix_of("shellsort"))
    print()

    print("longestPrefixOf(\"quicksort\"):")
    print(st.long_prefix_of("quicksort"))
    print()

    print("keysWithPrefix(\"shor\"):")
    for s in st.keys_with_prefix("shor"):
        print(s)
    print()

    print("keysThatMatch(\".he.l.\"):")
    for s in st.keys_that_match(".he.l."):
        print(s)
