"""
 *  Execution:    python binary_search_st
 *  Data files:   https://algs4.cs.princeton.edu/31elementary/tinyST.txt  
 *  
 *  Symbol table implementation with binary search in an ordered array.
 *
 *  % more tinyST.txt
 *  S E A R C H E X A M P L E
 *  
 *  % python binary_search_st < tinyST.txt
 *  C 4
 *  E 12
 *  H 5
 *  L 11
 *  M 9
 *  P 10
 *  R 3
 *  S 0
 *  X 7
 *
 """


class BinarySearchST:
    init_capacity = 2

    def __init__(self):
        self.keys = [None]*self.init_capacity
        self.vals = [None]*self.init_capacity
        self.n = 0

    def rank(self, arr, key):
        lo, hi = 0, self.n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (key < arr[mid]):
                hi = mid - 1
            elif (key > arr[mid]):
                lo = mid + 1
            else:
                return mid
        return lo

    def resize(self, capacity):
        self.keys = self.keys + [None]*(capacity-len(self.keys))
        self.vals = self.vals + [None]*(capacity-len(self.vals))

    def contains(self, key):
        return self.get(key) != None

    def get(self, key):
        i = self.rank(self.keys, key)
        if i < self.n and self.keys[i] == key:
            return self.vals[i]
        return None

    def put(self, key, val):
        i = self.rank(self.keys, key)
        if i < self.n and self.keys[i] == key:
            self.vals[i] = val
            return

        if self.n == len(self.keys):
            self.resize(self.n*2)

        j = self.n
        while j > i:
            self.keys[j], self.vals[j] = self.keys[j-1], self.vals[j-1]
            j -= 1
        self.keys[i], self.vals[i] = key, val
        self.n += 1

    def delete(self, key):
        self.put(key, None)

    def is_empty(self):
        return self.n == 0

    def Size(self):
        return self.n

    def Keys(self):
        return self.keys[:self.n]


if __name__ == '__main__':
    import sys
    st = BinarySearchST()
    i = 0
    for line in sys.stdin:
        for key in line.split():
            st.put(key, i)
            i += 1
    for s in st.Keys():
        print(s + " " + str(st.get(s)))
