"""
 *  Execution:    python trie_st.py < words.txt
 *  Dependencies: StdIn.java
 *  Data files:   https://algs4.cs.princeton.edu/52trie/shellsST.txt
 *
 *  A string symbol table for extended ASCII strings, implemented
 *  using a 256-way trie.
 *
 *  % python trie_st.py < shellsST.txt 
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

R = 256


class Node:
    def __init__(self):
        self.val = None
        self.next = [None for _ in range(R)]


class TrieST:
    def __init__(self):
        self.size = 0
        self.root = None

    def char_at(self, s, d):
        return ord(s[d])

    def get(self, key):
        x = self._get(self.root, key, 0)
        if x == None:
            return x
        return x.val

    def _get(self, x, key, d):
        if x == None:
            return None
        if d == len(key):
            return x
        c = self.char_at(key, d)
        return self._get(x.next[c], key, d+1)

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        if x == None:
            x = Node()
        if d == len(key):
            if x.val == None:
                self.size += 1
            x.val = val
            return x
        c = self.char_at(key, d)
        x.next[c] = self._put(x.next[c], key, val, d+1)
        return x

    def keys(self):
        return self.keys_with_prefix("")

    def keys_with_prefix(self, pre):
        q = Queue()
        self.collect(self._get(self.root, pre, 0), pre, q)
        return q

    def collect(self, x, pre, q):
        if x == None:
            return
        if x.val != None:
            q.enqueue(pre)
        for c in range(R):
            self.collect(x.next[c], pre+chr(c), q)

    def keys_that_match(self, pat):
        q = Queue()
        self.collectMatch(self.root, "", pat, q)
        return q

    def collectMatch(self, x, pre, pat, q):
        if x == None:
            return
        d = len(pre)
        if d == len(pat) and x.val != None:
            q.enqueue(pre)
        if d == len(pat):
            return
        next = self.char_at(pat, d)
        for c in range(R):
            if chr(next) == "." or next == c:
                self.collectMatch(x.next[c], pre+chr(c), pat, q)

    def long_prefix_of(self, s):
        length = self.search(self.root, s, 0, 0)
        return s[:length]

    def search(self, x, s, d, length):
        if x == None:
            return length
        if x.val != None:
            length = d
        if d == len(s):
            return length
        c = self.char_at(s, d)
        return self.search(x.next[c], s, d+1, length)

    def delete(self, key):
        self.root = self._delete(self.root, key, 0)

    def _delete(self, x, key, d):
        if x == None:
            return None
        if d == len(key):
            if x.val != None:
                self.size -= 1
            x.val = None
        else:
            c = self.char_at(key, d)
            x.next[c] = self._delete(x.next[c], key, d+1)
        if x.val == None:
            return x
        for c in range(R):
            if x.next[c] != None:
                return x
        return None


if __name__ == "__main__":
    import sys
    st = TrieST()
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
