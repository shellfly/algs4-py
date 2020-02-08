import sys


class BinaryStdin:
    buffer = 0
    n = 0
    initialized = False

    @classmethod
    def read_str(cls):
        if cls.is_empty():
            raise Exception("reading from empty input stream")
        s = []
        while not cls.is_empty():
            b = cls.read_byte()
            s.append(chr(b))
        return "".join(s)

    @classmethod
    def read_int(cls):
        if cls.is_empty():
            raise Exception("reading from empty input stream")
        x = 0
        for i in range(4):
            b = cls.read_byte()
            x <<= 8
            x |= b
        return x

    @classmethod
    def read_int_r(cls, r):
        if r < 1 or r > 32:
            raise Exception("invalid r")
        if r == 32:
            return cls.read_int()
        x = 0
        for i in range(r):
            x <<= 1
            bit = cls.read_bool()
            if bit:
                x |= 1
        return x

    @classmethod
    def read_byte(cls):
        if cls.is_empty():
            raise Exception("reading from empty input stream")
        if cls.n == 8:
            b = cls.buffer
            cls.fill_buffer()
            return b
        x = cls.buffer
        x <<= (8-cls.n)
        old_n = cls.n
        cls.fill_buffer()
        cls.n = old_n
        x |= (cls.buffer >> cls.n)
        return x & 0xff

    @classmethod
    def read_bool(cls):
        if cls.is_empty():
            raise Exception("reading from empty input stream")
        cls.n -= 1
        bit = (cls.buffer >> cls.n & 1) == 1
        if cls.n == 0:
            cls.fill_buffer()
        return bit

    @classmethod
    def fill_buffer(cls):
        byte = sys.stdin.buffer.read(1)
        if byte == b'':
            cls.buffer = EOFError
            cls.n = -1
            return
        cls.n = 8
        cls.buffer = ord(byte)

    @classmethod
    def initialize(cls):
        cls.fill_buffer()
        cls.initialized = True

    @classmethod
    def is_empty(cls):
        if not cls.initialized:
            cls.initialize()
        return cls.buffer == EOFError
