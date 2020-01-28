"""
Sorts a sequence of strings from standard input using selection sort.

 
% more tiny.txt

S O R T E X A M P L E

% python selection.py < tiny.txt

A E E L M O P R S T X                 [ one string per line ]

  

% more words3.txt

bed bug dad yes zoo ... all bad yet


% python selection.py < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Selection:

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        for i in range(N - 1):
            minIndex = i
            for j in range(i, N):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
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
    print('sort items: ', Selection.sort(items))
    assert Selection.is_sorted(items)
