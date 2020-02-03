"""
   Execution:    python digraph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/41graph/tinyDG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumDG.txt
                 https://algs4.cs.princeton.edu/41graph/largeDG.txt
 
   A graph, implemented using an array of sets.
   Parallel edges and self-loops are permitted.
 
   % python digraph.py < tinyDG.txt
   13 vertices, 22 edges
   0: 5 1 
   1: 
   2: 0 3 
   3: 5 2 
   4: 3 2 
   5: 4 
   6: 9 4 8 0 
   7: 6 9
   8: 6 
   9: 11 10 
   10: 12 
   11: 4 12 
   12: 9 
 
 """
from algs4.bag import Bag


class Digraph:

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
                v, w = in_file.readline().split()
                self.add_edge(int(v), int(w))

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w)
                                               for w in self.adj[v])) for v in range(self.V))
        return s

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].add(w)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def max_degree(self):
        max_deg = 0
        for v in self.V:
            max_deg = max(max_deg, self.degree(v))
        return max_deg

    def number_of_self_loops(self):
        count = 0
        for v in range(self.V):
            for w in self.adj[v]:
                if w == v:
                    count += 1
        return count

    def reverse(self):
        R = Digraph(self.V)
        v = 0
        while v < self.V:
            for w in self.adj[v]:
                R.add_edge(w, v)
            v += 1
        return R


if __name__ == '__main__':
    import sys

    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    g = Digraph(V)
    for i in range(E):
        v, w = sys.stdin.readline().split()
        g.add_edge(v, w)
    print(g)
