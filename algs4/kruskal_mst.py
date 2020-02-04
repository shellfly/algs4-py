"""
 *  Execution:    python kruskal_mst.py filename.txt
 *  Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/largeEWG.txt
 *
 *  Compute a minimum spanning forest using a lazy version of Prim's
 *  algorithm.
 *
 *  %  python kruskal_mst.py tinyEWG.txt
 *  0-7 0.16000
 *  1-7 0.19000
 *  0-2 0.26000
 *  2-3 0.17000
 *  5-7 0.28000
 *  4-5 0.35000
 *  6-2 0.40000
 *  1.81000
 *
 *  % python kruskal_mst.py mediumEWG.txt
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
 *  % python kruskal_mst.py largeEWG.txt
 *  ...
 *  647.66307
 *
"""

from algs4.edge_weighted_graph import EdgeWeightedGraph
from algs4.min_pq import MinPQ
from algs4.queue import Queue
from algs4.uf import UF


class KruskalMST:
    def __init__(self, g):
        self.weight = 0
        self.mst = Queue()
        self.pq = MinPQ()
        for e in g.edges():
            self.pq.insert(e)

        uf = UF(g.V)
        while not self.pq.is_empty() and self.mst.size() < g.V - 1:
            e = self.pq.del_min()
            v = e.either()
            w = e.other(v)
            if uf.connected(v, w):
                continue
            uf.union(v, w)
            self.mst.enqueue(e)
            self.weight += e.weight

    def edges(self):
        return self.mst


if __name__ == "__main__":
    import sys
    g = EdgeWeightedGraph(file=open(sys.argv[1]))
    mst = KruskalMST(g)
    for e in mst.edges():
        print(e)
    print("%.5f" % mst.weight)
