"""
   Execution:  python quick3_string.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python quick3_string.py < words3.txt
   all
   bad
   bed
   bug
   dad
   ...
   yes
   yet
   zoo
"""


class Quick3string:
    R = 256  # extended ASCII alphabet size
    CUTOFF = 15  # cutoff to insertion sort

    def __init__(self, a):
        self.aux = ["" for _ in range(len(a))]
        self.sort(a, 0, len(a)-1, 0)

    def sort(self, a, lo, hi, d):
        if hi <= lo + self.CUTOFF:
            self.insertion(a, lo, hi, d)
            return

        lt, gt = lo, hi
        v = self.char_at(a[lo], d)
        i = lo + 1
        while i <= gt:
            t = self.char_at(a[i], d)
            if t < v:
                self.exch(a, lt, i)
                lt += 1
                i += 1
            elif t > v:
                self.exch(a, i, gt)
                gt -= 1
            else:
                i += 1
        self.sort(a, lo, lt-1, d)
        if v >= 0:
            self.sort(a, lt, gt, d+1)
        self.sort(a, gt+1, hi, d)

    def insertion(self, a, lo, hi, d):
        for i in range(lo, hi+1):
            j = i
            while j > lo and a[j][d] < a[j-1][d]:
                a[j], a[j-1] = a[j-1], a[j]
                j -= 1

    def char_at(self, s, d):
        return ord(s[d])

    def exch(self, a, i, j):
        a[i], a[j] = a[j], a[i]


if __name__ == '__main__':
    import sys
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    Quick3string(words)
    for item in words:
        print(item)
