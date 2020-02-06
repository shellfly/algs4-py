"""
   Execution:  python msd.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python msd.py < words3.txt
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


class MSD:
    R = 256  # extended ASCII alphabet size
    CUTOFF = 15  # cutoff to insertion sort

    def __init__(self, a):
        self.aux = ["" for _ in range(len(a))]
        self.sort(a, 0, len(a)-1, 0)

    def sort(self, a, lo, hi, d):
        if hi <= lo + self.CUTOFF:
            self.insertion(a, lo, hi, d)
            return

        count = [0 for _ in range(self.R+2)]
        for i in range(lo, hi+1):
            count[self.char_at(a[i], d)+2] += 1
        for r in range(self.R+1):
            count[r+1] += count[r]
        for i in range(lo, hi+1):
            self.aux[count[self.char_at(a[i], d)+1]] = a[i]
            count[self.char_at(a[i], d)+1] += 1
        for i in range(lo, hi+1):
            a[i] = self.aux[i-lo]
        for r in range(self.R):
            self.sort(a, lo+count[r], lo+count[r+1]-1, d+1)

    def insertion(self, a, lo, hi, d):
        for i in range(lo, hi+1):
            j = i
            while j > lo and a[j][d] < a[j-1][d]:
                a[j], a[j-1] = a[j-1], a[j]
                j -= 1

    def char_at(self, s, d):
        return ord(s[d])


if __name__ == '__main__':
    import sys
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    MSD(words)
    for item in words:
        print(item)
