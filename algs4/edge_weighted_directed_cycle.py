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
import random

from algs4.stack import Stack
from algs4.directed_edge import DirectedEdge
from algs4.edge_weighted_digraph import EdgeWeightedDigraph


class EdgeWeightedDirectedCycle:
    def __init__(self, G):
        self.cycle = None
        self.marked = [False for _ in range(G.V)]
        self.on_stack = [False for _ in range(G.V)]
        self.edge_to = [None for _ in range(G.V)]
        for v in range(G.V):
            if not self.marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self.on_stack[v] = True
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.To()
            if self.cycle is not None:
                return
            elif not self.marked[w]:
                print("push stack", e)
                self.edge_to[w] = e
                self.dfs(G, w)
            elif self.on_stack[w]:
                # trace back directed cycle
                self.cycle = Stack()
                f = e
                while f.From() != w:
                    self.cycle.push(f)
                    f = self.edge_to[f.From()]
                self.cycle.push(f)
                return
        self.on_stack[v] = False

    def has_cycle(self):
        return self.cycle is not None


if __name__ == "__main__":
    import sys

    V, E, F = sys.argv[1:]
    V = int(V)
    E = int(E)
    F = int(F)
    graph = EdgeWeightedDigraph(V)
    for _ in range(int(E)):
        v = 0
        w = 0
        while v >= w:
            v = random.randint(0, V - 1)
            w = random.randint(0, V - 1)
        weight = random.uniform(0, 1)
        graph.add_edge(DirectedEdge(v, w, weight))
    #  add F extra edges
    for _ in range(int(E)):
        v = random.randint(0, V - 1)
        w = random.randint(0, V - 1)
        weight = random.uniform(0, 1)
        graph.add_edge(DirectedEdge(v, w, weight))
    print(graph)

    finder = EdgeWeightedDirectedCycle(graph)
    if finder.has_cycle():
        print("find cycle:\n")
        for e in finder.cycle:
            print(e, " ")
        print()
    else:
        print("No directed cycle")
