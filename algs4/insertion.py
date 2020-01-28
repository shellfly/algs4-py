"""
Sorts a sequence of strings from standard input using insertion sort.


% more tiny.txt

S O R T E X A M P L E

% python insertion.py < tiny.txt

A E E L M O P R S T X                 [ one string per line ]



% more words3.txt

bed bug dad yes zoo ... all bad yet


% python insertion.py < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Insertion:

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        for i in range(1, N):
            j = i
            while j >= 1:
                if arr[j] > arr[j - 1]:
                    break
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
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
    print('sort items: ', Insertion.sort(items))
    assert Insertion.is_sorted(items)
