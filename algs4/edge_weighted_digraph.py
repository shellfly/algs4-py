"""
 *  Execution:    python edge_weighted_digraph.py filename.txt
 *  Data files:   https://algs4.cs.princeton.edu/43mst/tinyEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/mediumEWG.txt
 *                https://algs4.cs.princeton.edu/43mst/largeEWG.txt
 *
 *  An edge-weighted directed graph, implemented using adjacency lists.
 *  Parallel edges and self-loops are permitted.
 *
 *  % python edge_weighted_digraph.py tinyEWD.txt
 * 8 vertices, 15 edges
 * 0: 0->2 0.26000 0->4 0.38000
 * 1: 1->3 0.29000
 * 2: 2->7 0.34000
 * 3: 3->6 0.52000
 * 4: 4->7 0.37000 4->5 0.35000
 * 5: 5->1 0.32000 5->7 0.28000 5->4 0.35000
 * 6: 6->4 0.93000 6->0 0.58000 6->2 0.40000
 * 7: 7->3 0.39000 7->5 0.28000
 *
"""
from algs4.bag import Bag
from algs4.directed_edge import DirectedEdge


class EdgeWeightedDigraph:
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
    graph = EdgeWeightedDigraph(file=open(sys.argv[1]))
    print(graph)
