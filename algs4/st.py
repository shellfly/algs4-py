"""
  Execution:    python st.py < input.txt
  Data files:   https://algs4.cs.princeton.edu/35applications/tinyST.txt
  
  Sorted symbol table implementation using a python collections.OrderedDict
  Does not allow duplicates.
 """

from collections import OrderedDict


class ST:

    def __init__(self):
        self.st = OrderedDict()

    def put(self, key, value):
        self.st[key] = value

    def get(self, key):
        if key is None:
            raise ValueError("calls get() with null key")

        return self.st.get(key)

    def delete(self, key):
        if key is None:
            raise ValueError("calls get() with null key")
        del self.st[key]

    def contains(self, key):
        return key in self.st

    def is_empty(self):
        self.size() == 0

    def size(self):
        return len(self.st.keys())

    def keys(self):
        return self.st.keys()

if __name__ == "__main__":
    import sys
    st = ST()
    i = 0
    for line in sys.stdin:
        st.put(line, i)
        i += 1

    for key in st.keys():
        print("%s : %s " % (key, st.get(key)))
