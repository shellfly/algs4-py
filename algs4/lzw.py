"""
 *  Execution:    python lzw.py - < input.txt   (compress)
 *  Execution:    python lzw.py + < input.txt   (expand)
 *  Data files:   https://algs4.cs.princeton.edu/55compression/abraLZW.txt
 *                https://algs4.cs.princeton.edu/55compression/ababLZW.txt
 *
 *  % python lzw.py - < abraLZW.txt | python lzw.py +
 *  ABRACADBRACRAACRA
 *
"""

from algs4.binarystdin import BinaryStdin
from algs4.binarystdout import BinaryStdout
from algs4.tst import TST


class LZW:
    R = 256
    L = 4096
    W = 12

    @classmethod
    def compress(cls):
        input = BinaryStdin.read_str()
        st = TST()
        for i in range(cls.R):
            st.put(chr(i), i)
        code = cls.R+1
        while len(input) > 0:
            s = st.long_prefix_of(input)
            BinaryStdout.write_bits(st.get(s), cls.W)
            t = len(s)
            if t < len(input) and code < cls.L:
                st.put(input[:t+1], code)
                code += 1
            input = input[t:]
        BinaryStdout.write_bits(cls.R, cls.W)
        BinaryStdout.close()

    @classmethod
    def expand(cls):
        st = ["" for _ in range(cls.L)]
        for i in range(cls.R):
            st[i] = chr(i)
        st[i] = " "
        i += 1
        codeword = BinaryStdin.read_int_r(cls.W)
        val = st[codeword]
        while True:
            BinaryStdout.write_str(val)
            codeword = BinaryStdin.read_int_r(cls.W)
            if codeword == cls.R:
                break
            s = st[codeword]
            if i == codeword:
                s = val + val[0]
            if i < cls.L:
                st[i] = val + s[0]
                i += 1
            val = s
        BinaryStdout.close()


if __name__ == '__main__':
    import sys
    if sys.argv[1] == "-":
        LZW.compress()
    else:
        LZW.expand()
