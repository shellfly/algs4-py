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
        i = lo + 1
        j = hi
        while True:
            while i < hi and arr[i] < v:
                i += 1
            while j > lo and arr[j] > v:
                j -= 1
            if i >= j or i == hi or j == lo:
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


if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        items = line.split()
        print('     items: ', items)
        print('sort items: ', Quick.sort(items))
