"""
 *  Execution:    python edge_weighted_directed_cycle.py V E F
 *  Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/largeEWG.txt
 *
 *  Finds a directed cycle in an edge-weighted digraph.
 *  Runs in O(E + V) time..
 *
 *
"""
from algs4.bag import Bag
from algs4.directed_edge import DirectedEdge


class EdgeWeightedDirectedCycle:
    def __init__(self, v=0, **kwargs):
        self.V = v
        self.E = 0
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = Bag()

        if 'file' in kwargs:
            # init a digraph by a file input
            in_file = kwargs['file']
            self.V = int(in_file.readline())
            for v in range(self.V):
                self.adj[v] = Bag()
            E = int(in_file.readline())
            for i in range(E):
                v, w, weight = in_file.readline().split()
                self.add_edge(DirectedEdge(int(v), int(w), float(weight)))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for i in range(self.V):
            adjs = " ".join([str(x) for x in self.adj[i]])
            s += "%d: %s\n" % (i, adjs)
        return s

    def add_edge(self, e):
        self.adj[e.From()].add(e)
        self.E += 1

    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                edges.append(e)
        return edges


if __name__ == "__main__":
    import sys
    V, E, F = sys.argv[1:]
    graph = EdgeWeightedDirectedCycle(int(V), int(E), int(F))

    print(graph)
