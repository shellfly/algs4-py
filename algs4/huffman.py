"""
 *  Execution:    python huffman.py - < input.txt   (compress)
 *  Execution:    python huffman.py + < input.txt   (expand)
 *  Data files:   https://algs4.cs.princeton.edu/55compression/abra.txt
 *                https://algs4.cs.princeton.edu/55compression/tinytinyTale.txt
 *                https://algs4.cs.princeton.edu/55compression/medTale.txt
 *                https://algs4.cs.princeton.edu/55compression/tale.txt
 *
 *  Compress or expand a binary input stream using the Huffman algorithm.
 *
 *  % python huffman.py - < abra.txt | python binarydump.py 60
 *  010100000100101000100010010000110100001101010100101010000100
 *  000000000000000000000000000110001111100101101000111110010100
 *  120 bits
 *
 *  % python huffman.py - < abra.txt | python huffman.py +
 *  ABRACADABRA!
 *
"""

from algs4.binarystdin import BinaryStdin
from algs4.binarystdout import BinaryStdout
from algs4.min_pq import MinPQ


class Node:
    def __init__(self, ch, freq, left, right):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return "%s %d" % (self.ch, self.freq)

    def is_leaf(self):
        return self.left == None and self.right == None

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq


class Huffman:
    R = 256
    @classmethod
    def compress(cls):
        s = BinaryStdin.read_str()
        freq = [0 for _ in range(cls.R)]
        for i in range(len(s)):
            freq[ord(s[i])] += 1

        # build huffman trie
        root = cls.build_trie(freq)

        # build code table
        st = [None for _ in range(cls.R)]
        cls.build_code(st, root, "")

        # print trie for decoder
        cls.write_trie(root)

        # print number of bytes in original uncompressed message
        BinaryStdout.write_int(len(s))
        # use Huffman code to encode input
        for i in range(len(s)):
            code = st[ord(s[i])]
            for j in range(len(code)):
                if code[j] == "0":
                    BinaryStdout.write_bit(False)
                elif code[j] == "1":
                    BinaryStdout.write_bit(True)
        BinaryStdout.close()

    @classmethod
    def build_trie(cls, freq):
        pq = MinPQ()
        for c in range(cls.R):
            if freq[c] > 0:
                pq.insert(Node(chr(c), freq[c], None, None))
        while pq.size() > 1:
            left = pq.del_min()
            right = pq.del_min()
            parent = Node(chr(0), left.freq+right.freq, left, right)
            pq.insert(parent)
        return pq.del_min()

    @classmethod
    def write_trie(cls, x):
        if x.is_leaf():
            BinaryStdout.write_bit(True)
            BinaryStdout.write_byte(ord(x.ch))
            return
        BinaryStdout.write_bit(False)
        cls.write_trie(x.left)
        cls.write_trie(x.right)

    @classmethod
    def build_code(cls, st, x, s):
        if not x.is_leaf():
            cls.build_code(st, x.left, s+"0")
            cls.build_code(st, x.right, s+"1")
        else:
            st[ord(x.ch)] = s

    @classmethod
    def expand(cls):
        root = read_trie()
        length = BinaryStdin.read_int()
        for i in range(length):
            x = root
            while not x.is_leaf():
                bit = BinaryStdin.read_bool()
                if bit:
                    x = x.right
                else:
                    x = x.left
            BinaryStdout.write_byte(ord(x.ch))


def read_trie():
    is_leaf = BinaryStdin.read_bool()
    if is_leaf:
        return Node(chr(BinaryStdin.read_byte()), 0, None, None)
    return Node(chr(0), 0, read_trie(), read_trie())


if __name__ == '__main__':
    import sys
    if sys.argv[1] == "-":
        Huffman.compress()
    else:
        Huffman.expand()
