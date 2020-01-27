"""
Sorts a sequence of strings from standard input using quick sort.

 
% more tiny.txt

S O R T E X A M P L E

% python quick.py < tiny.txt

A E E L M O P R S T X                 [ one string per line ]

  

% more words3.txt

bed bug dad yes zoo ... all bad yet


% python quick.py < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Quick:

    @classmethod
    def partition(cls, arr, lo, hi):
        v = arr[lo]
        i = lo
        j = hi+1
        while True:
            while True:
                i += 1
                if not (i < hi and arr[i] < v):
                    break
            while True:
                j -= 1
                if not (j > lo and arr[j] > v):
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        arr[lo], arr[j] = arr[j], arr[lo]
        return j

    @classmethod
    def quicksort(cls, arr, lo, hi):
        if lo >= hi:
            return

        j = cls.partition(arr, lo, hi)
        cls.quicksort(arr, lo, j - 1)
        cls.quicksort(arr, j + 1, hi)
        return arr

    @classmethod
    def sort(cls, arr):
        return cls.quicksort(arr, 0, len(arr) - 1)

    @classmethod
    def is_sorted(cls, arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True


if __name__ == '__main__':
    import sys

    items = []
    for line in sys.stdin:
        items.extend(line.split())
    print('     items: ', items)
    print('sort items: ', Quick.sort(items))
    assert Quick.is_sorted(items)
