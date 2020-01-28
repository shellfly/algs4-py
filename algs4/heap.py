"""
Sorts a sequence of strings from standard input using heap sort.

 
% more tiny.txt

S O R T E X A M P L E

% python heap.py < tiny.txt

A E E L M O P R S T X                 [ one string per line ]

  

% more words3.txt

bed bug dad yes zoo ... all bad yet


% python heap.py < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Heap:

    @classmethod
    def sink(cls, a, i, length):

        while (2 * i + 1 <= length):
            j = 2 * i + 1
            if (j < length and a[j] < a[j + 1]):
                j += 1
            if a[i] > a[j]:
                break
            a[i], a[j] = a[j], a[i]
            i = j

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        k = N // 2
        while k >= 0:
            cls.sink(arr, k, N - 1)
            k -= 1

        while N > 0:
            arr[0], arr[N - 1] = arr[N - 1], arr[0]
            N -= 1
            cls.sink(arr, 0, N - 1)

        return arr

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
    print('sort items: ', Heap.sort(items))
    assert Heap.is_sorted(items)
