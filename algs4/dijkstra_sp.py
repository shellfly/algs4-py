"""
 *  Execution:    python dijkstra_sp.py input.txt s
 *  Data files:   https://algs4.cs.princeton.edu/44sp/tinyEWD.txt
 *                https://algs4.cs.princeton.edu/44sp/mediumEWD.txt
 *                https://algs4.cs.princeton.edu/44sp/largeEWD.txt
 *
 *  Dijkstra's algorithm. Computes the shortest path tree.
 *  Assumes all weights are nonnegative.
 *
 *  % python dijkstra_sp.py tinyEWD.txt 0
 *  0 to 0 (0.00)
 *  0 to 1 (1.05)  0->4  0.38   4->5  0.35   5->1  0.32
 *  0 to 2 (0.26)  0->2  0.26
 *  0 to 3 (0.99)  0->2  0.26   2->7  0.34   7->3  0.39
 *  0 to 4 (0.38)  0->4  0.38
 *  0 to 5 (0.73)  0->4  0.38   4->5  0.35
 *  0 to 6 (1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52
 *  0 to 7 (0.60)  0->2  0.26   2->7  0.34
 *
 *  % python dijkstra_sp.py mediumEWD.txt 0
 *  0 to 0 (0.00)
 *  0 to 1 (0.71)  0->44  0.06   44->93  0.07   ...  107->1  0.07
 *  0 to 2 (0.65)  0->44  0.06   44->231  0.10  ...  42->2  0.11
 *  0 to 3 (0.46)  0->97  0.08   97->248  0.09  ...  45->3  0.12
 *  0 to 4 (0.42)  0->44  0.06   44->93  0.07   ...  77->4  0.11
 *  ...
 *
"""

from algs4.edge_weighted_digraph import EdgeWeightedDigraph
from algs4.index_min_pq import IndexMinPQ
from algs4.stack import Stack

POSITIVE_INFINITY = 999999.0


class DijkstraSP:
    def __init__(self, g, s):
        self.edgeTo = [None for _ in range(g.V)]
        self.distTo = [float("inf") for _ in range(g.V)]
        for v in range(g.V):
            self.distTo[v] = POSITIVE_INFINITY
        self.distTo[s] = 0.0
        self.pq = IndexMinPQ(g.V)
        self.pq.insert(s, self.distTo[s])
        while not self.pq.is_empty():
            self.relax(g, self.pq.del_min())

    def relax(self, g, v):
        for e in g.adj[v]:
            w = e.To()
            if self.distTo[w] > self.distTo[v]+e.weight:
                self.distTo[w] = self.distTo[v] + e.weight
                self.edgeTo[w] = e
                if self.pq.contains(w):
                    self.pq.change(w, self.distTo[w])
                else:
                    self.pq.insert(w, self.distTo[w])

    def has_path_to(self, v):
        return self.distTo[v] < POSITIVE_INFINITY

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        edges = Stack()
        e = self.edgeTo[v]
        while e != None:
            edges.push(e)
            e = self.edgeTo[e.From()]
        return edges


if __name__ == "__main__":
    import sys
    graph = EdgeWeightedDigraph(file=open(sys.argv[1]))
    s = int(sys.argv[2])
    sp = DijkstraSP(graph, s)
    for t in range(graph.V):
        if sp.has_path_to(t):
            print("%d to %d (%.2f)  " % (s, t, sp.distTo[t]), end="")
            for e in sp.path_to(t):
                print(e, " ", end="")
            print()
        else:
            print("%d to %d  no path" % (s, t))
