"""
 *  Execution:    python edge_weighted_graph.py filename.txt
 *  Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/largeEWG.txt
 *
 *  An edge-weighted undirected graph, implemented using adjacency lists.
 *  Parallel edges and self-loops are permitted.
 *
 *  % python edge_weighted_graph.py tinyEWG.txt
 *  8 16
 *  0: 6-0 0.58000  0-2 0.26000  0-4 0.38000  0-7 0.16000
 *  1: 1-3 0.29000  1-2 0.36000  1-7 0.19000  1-5 0.32000
 *  2: 6-2 0.40000  2-7 0.34000  1-2 0.36000  0-2 0.26000  2-3 0.17000
 *  3: 3-6 0.52000  1-3 0.29000  2-3 0.17000
 *  4: 6-4 0.93000  0-4 0.38000  4-7 0.37000  4-5 0.35000
 *  5: 1-5 0.32000  5-7 0.28000  4-5 0.35000
 *  6: 6-4 0.93000  6-0 0.58000  3-6 0.52000  6-2 0.40000
 *  7: 2-7 0.34000  1-7 0.19000  0-7 0.16000  5-7 0.28000  4-7 0.37000
 *
"""
from algs4.bag import Bag
from algs4.edge import Edge


class EdgeWeightedGraph:
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
                self.add_edge(Edge(int(v), int(w), float(weight)))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        for i in range(self.V):
            adjs = " ".join([str(x) for x in self.adj[i]])
            s += "%d: %s\n" % (i, adjs)
        return s

    def add_edge(self, e):
        v = e.either()
        w = e.other(v)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1

    def edges(self):
        edges = []
        for v in range(self.V):
            for e in self.adj[v]:
                if e.other(v) > v:
                    edges.append(e)
        return edges


if __name__ == "__main__":
    import sys
    graph = EdgeWeightedGraph(file=open(sys.argv[1]))
    print(graph)
