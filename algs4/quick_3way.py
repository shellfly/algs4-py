"""
Sorts a sequence of strings from standard input using quick 3-way sort.

 
% more tiny.txt

S O R T E X A M P L E

% python quick 3-way < tiny.txt

A E E L M O P R S T X                 [ one string per line ]

  

% more words3.txt

bed bug dad yes zoo ... all bad yet


% python quick_3way < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Quick3Way:

    @classmethod
    def quicksort(cls, arr, lo, hi):
        if lo >= hi:
            return

        lt = lo
        gt = hi
        i = lo + 1
        v = arr[lo]
        while i <= gt:
            if arr[i] < v:
                arr[i], arr[lt] = arr[lt], arr[i]
                lt += 1
            elif arr[i] > v:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        cls.quicksort(arr, lo, lt - 1)
        cls.quicksort(arr, gt + 1, hi)
        return arr

    @classmethod
    def sort(cls, arr):
        return cls.quicksort(arr, 0, len(arr) - 1)

if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        items = line.split()
        print('     items: ', items)
        print('sort items: ', Quick3Way.sort(items))
