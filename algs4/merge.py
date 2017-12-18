"""
Sorts a sequence of strings from standard input using merge sort.

 
% more tiny.txt

S O R T E X A M P L E

% python merge < tiny.txt

A E E L M O P R S T X                 [ one string per line ]

  

% more words3.txt

bed bug dad yes zoo ... all bad yet


% python merge < words3.txt

all bad bed bug dad ... yes yet zoo    [ one string per line ]
"""


class Merge:

    @classmethod
    def merge(cls, arr):

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        h = 1
        while h < N / 3:
            h = 3 * h + 1  # 1, 4, 13, 40...

        while h >= 1:
            for i in range(h, N):
                j = i
                while j >= h:
                    if arr[j] > arr[j - h]:
                        break
                    arr[j], arr[j - h] = arr[j - h], arr[j]
                    j -= h
            h /= 3
        return arr

if __name__ == '__main__':
    import sys

    for line in sys.stdin:
        items = line.split()
        print('     items: ', items)
        print('sort items: ', Merge.sort(items))
