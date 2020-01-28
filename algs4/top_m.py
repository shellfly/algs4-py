"""
 * Execution:    python top_m.py m < input.txt
 *  Data files:   https://algs4.cs.princeton.edu/24pq/tinyBatch.txt
 *
 *  Given an integer m from the command line and an input stream where
 *  each line contains a String and a long value, this MinPQ client
 *  prints the m lines whose numbers are the highest.
 *
 *  % python top_m.py 5 < tinyBatch.txt
 *  Thompson    2/27/2000  4747.08
 *  vonNeumann  2/12/1994  4732.35
 *  vonNeumann  1/11/1999  4409.74
 *  Hoare       8/18/1992  4381.21
 *  vonNeumann  3/26/2002  4121.85
 *
 """

import sys

from algs4.min_pq import MinPQ
from algs4.stack import Stack
from algs4.transaction import Transaction

M = int(sys.argv[1])
pq = MinPQ()
for line in sys.stdin:
    pq.insert(Transaction(line))
    if pq.size() > M:
        pq.del_min()

stack = Stack()
while not pq.is_empty():
    stack.push(pq.del_min())
for t in stack:
    print(t)
