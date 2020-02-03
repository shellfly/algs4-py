"""
 *  Execution:    python depth_first_order.py digraph.txt
 *  Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt
 *                https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
 *
 *  Compute preorder and postorder for a digraph or edge-weighted digraph.
 *  Runs in O(E + V) time.
 *
 *  % python depth_first_order.py tinyDAG.txt
 *     v  pre post
 *  --------------
 *     0    0    8
 *     1    3    2
 *     2    9   10
 *     3   10    9
 *     4    2    0
 *     5    1    1
 *     6    4    7
 *     7   11   11
 *     8   12   12
 *     9    5    6
 *    10    8    5
 *    11    6    4
 *    12    7    3
 *  Preorder:  0 5 4 1 6 9 11 12 10 2 3 7 8
 *  Postorder: 4 5 1 12 11 10 9 6 0 3 2 7 8
 *  Reverse postorder: 8 7 2 3 0 6 9 10 11 12 1 5 4
 *
"""
from algs4.queue import Queue
from algs4.stack import Stack
from algs4.digraph import Digraph


class DepthFirstOrder:

    def __init__(self, G):
        self.marked = [False for _ in range(G.V)]
        self.pre = Queue()
        self.post = Queue()
        for w in range(G.V):
            if not self.marked[w]:
                self.dfs(G, w)

    def dfs(self, G, v):
        self.pre.enqueue(v)
        self.marked[v] = True

        for w in G.adj[v]:
            if not self.marked[w]:
                self.dfs(G, w)
        self.post.enqueue(v)

    def reverse_post(self):
        reverse = Stack()
        for v in self.post:
            reverse.push(v)
        return reverse


if __name__ == '__main__':
    import sys
    g = Digraph(file=open(sys.argv[1]))
    dfs = DepthFirstOrder(g)

    print("Preorder: ")
    for v in dfs.pre:
        print(v, " ", end="")
    print()

    print("Postorder: ")
    for v in dfs.post:
        print(v, " ", end="")
    print()

    print("ReversePostorder: ")
    for v in dfs.reverse_post():
        print(v, " ", end="")
    print()
