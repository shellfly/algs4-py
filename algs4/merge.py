"""
Sorts a sequence of strings from standard input using merge sort.

 
% more tiny.txt

S O R T E X A M P L E

% python merge.py < tiny.txt

A E E L M O P R S T X                 [ one string per line ]

  

% more words3.txt

bed bug dad yes zoo ... all bad yet


% python merge.py < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Merge:

    @classmethod
    def merge(cls, arr, lo, mid, hi):
        aux = list(arr)  # copy to aux
        i = lo
        j = mid + 1
        k = lo
        while k <= hi:
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
            k += 1

    @classmethod
    def mergesort(cls, arr, lo, hi):
        if lo >= hi:
            return

        mid = (lo + hi) // 2
        cls.mergesort(arr, lo, mid)
        cls.mergesort(arr, mid + 1, hi)
        cls.merge(arr, lo, mid, hi)
        return arr

    @classmethod
    def sort(cls, arr):
        return cls.mergesort(arr, 0, len(arr) - 1)

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
    print('sort items: ', Merge.sort(items))
    assert Merge.is_sorted(items)
