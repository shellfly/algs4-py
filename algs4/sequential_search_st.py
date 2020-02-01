"""
 *  Execution:    python3 sequential_search_st.py
 *  Data files:   https://algs4.cs.princeton.edu/31elementary/tinyST.txt
 *  
 *  Symbol table implementation with sequential search in an
 *  unordered linked list of key-value pairs.
 *
 *  % more tinyST.txt
 *  S E A R C H E X A M P L E
 *
 *  % python3 sequential_search_st.py < tinyST.txt
 *  L 11
 *  P 10
 *  M 9
 *  X 7
 *  H 5
 *  C 4
 *  R 3
 *  A 8
 *  E 12
 *  S 0
 *
 """


from algs4.utils.st import Node, STKeyIterator


class SequentialSearchST:

    def __init__(self):
        self.first = None
        self.size = 0

    def contains(self, key):
        x = self.first
        while x:
            if key == x.key:
                return True
            x = x.next
        return False

    def get(self, key):
        x = self.first
        while x:
            if key == x.key:
                return x.val
            x = x.next
        return None

    def put(self, key, val):
        x = self.first
        while x:
            if key == x.key:
                x.val = val
                return
            x = x.next
        self.first = Node(key, val, self.first)
        self.size += 1

    def delete(self, key):
        prev = None
        curr = self.first
        while curr:
            if key == curr.key:
                if prev:
                    prev.next = curr.next
                else:
                    self.first = curr.ext
                self.size -= 1
            prev = curr
            curr = curr.next

    def Keys(self):
        return STKeyIterator(self.first)

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    import sys

    st = SequentialSearchST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1

    for key in st.Keys():
        print(key + " " + str(st.get(key)))
