"""
 *  Execution:    python lazy_prim_mst.py filename.txt
 *  Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/largeEWG.txt
 *
 *  Compute a minimum spanning forest using a lazy version of Prim's
 *  algorithm.
 *
 *  %  python lazy_prim_mst.py tinyEWG.txt
 *  0-7 0.16000
 *  1-7 0.19000
 *  0-2 0.26000
 *  2-3 0.17000
 *  5-7 0.28000
 *  4-5 0.35000
 *  6-2 0.40000
 *  1.81000
 *
 *  % python lazy_prim_mst.py mediumEWG.txt
 *  0-225   0.02383
 *  49-225  0.03314
 *  44-49   0.02107
 *  44-204  0.01774
 *  49-97   0.03121
 *  202-204 0.04207
 *  176-202 0.04299
 *  176-191 0.02089
 *  68-176  0.04396
 *  58-68   0.04795
 *  10.46351
 *
 *  % python lazy_prim_mst.py largeEWG.txt
 *  ...
 *  647.66307
 *
"""

from algs4.edge_weighted_graph import EdgeWeightedGraph
from algs4.min_pq import MinPQ
from algs4.queue import Queue


class LazyPrimMST:
    def __init__(self, g):
        self.marked = [False for _ in range(g.V)]
        self.pq = MinPQ()
        self.mst = Queue()
        self.weight = 0

        for v in range(g.V):
            if not self.marked[v]:
                self.prim(g, v)

    def prim(self, g, v):
        self.visit(g, v)
        while not self.pq.is_empty():
            e = self.pq.del_min()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.enqueue(e)
            self.weight += e.weight
            if not self.marked[v]:
                self.visit(g, v)
            if not self.marked[w]:
                self.visit(g, w)

    def visit(self, g, v):
        self.marked[v] = True
        for e in g.adj[v]:
            if not self.marked[e.other(v)]:
                self.pq.insert(e)

    def edges(self):
        return self.mst


if __name__ == "__main__":
    import sys
    g = EdgeWeightedGraph(file=open(sys.argv[1]))
    mst = LazyPrimMST(g)
    for e in mst.edges():
        print(e)
    print("%.5f" % mst.weight)
