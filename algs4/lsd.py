"""
   Execution:  python lsd.py < input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python lsd.py < words3.txt
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


class LSD:
    R = 256
    @classmethod
    def sort(cls, a, w):
        n = len(a)
        aux = ['' for _ in range(n)]
        for d in range(w-1, -1, -1):
            count = [0 for _ in range(cls.R+1)]
            for i in range(n):
                count[ord(a[i][d])+1] += 1
            for r in range(cls.R):
                count[r+1] += count[r]
            for i in range(n):
                aux[count[ord(a[i][d])]] = a[i]
                count[ord(a[i][d])] += 1
            for i in range(n):
                a[i] = aux[i]


if __name__ == '__main__':
    import sys
    words = []
    for line in sys.stdin:
        words.extend(line.split())
    LSD.sort(words, len(words[0]))
    for item in words:
        print(item)
