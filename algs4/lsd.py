"""
   Execution:  python lsd.py input.txt

   Data files:   https://algs4.cs.princeton.edu/51radix/words3.txt

   % python lsd.py words3.txt
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

    @classmethod
    def sort(cls, a, w):
        n = len(a)
        R = 256
        aux = ['' for _ in range(n)]
        for d in range(w-1, -1, -1):
            count = [0 for _ in range(R+1)]
            for i in range(n):
                count[ord(a[i][d])+1] += 1
            for r in range(R):
                count[r+1] += count[r]
            for i in range(n):
                aux[count[ord(a[i][d])]] = a[i]
                count[ord(a[i][d])] += 1
            for i in range(n):
                a[i] = aux[i]

if __name__ == '__main__':
    import sys
    lst = []
    with open(sys.argv[1]) as fp:
        for line in fp:
            for x in line.split(' '):
                lst.append(x.strip())
    LSD.sort(lst, len(lst[0]))
    for item in lst:
        print(item)
