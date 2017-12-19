import sys

from algs4.min_pq import MinPQ
from algs4.stack import Stack
from algs4.transaction import Transaction

M = int(sys.argv[1])
pq = MinPQ()
for line in sys.stdin:
    Transaction(line)
    pq.insert(Transaction(line))
    if pq.size() > M:
        pq.del_min()

stack = Stack()
while not pq.is_empty():
    stack.push(pq.del_min())
for t in stack:
    print(t)
