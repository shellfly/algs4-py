"""
    Execution:    python directed_dfs.py digraph.txt s
    Data files:   https: // algs4.cs.princeton.edu / 42digraph / tinyDG.txt
                  https://algs4.cs.princeton.edu/42digraph/mediumDG.txt
                  https://algs4.cs.princeton.edu/42digraph/largeDG.txt

    Determine single-source or multiple-source reachability in a digraph
    using depth first search.
    Runs in O(E + V) time.

    % python directed_dfs.py tinyDG.txt 1
    1

    % python directed_dfs.py tinyDG.txt 2
    0 1 2 3 4 5

    % python directed_dfs.py tinyDG.txt 1 2 6
    0 1 2 3 4 5 6 8 9 10 11 12 
"""

from algs4.digraph import Digraph


class DirectedDFS:

    def __init__(self, G, sources):
        self._marked = [False for _ in range(G.V)]
        for s in sources:
            s = int(s)
            if not self._marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self._marked[v] = True
        for w in G.adj[v]:
            if not self._marked[w]:
                self.dfs(G, w)

    def marked(self, v):
        return self._marked[v]

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    V = int(f.readline())
    E = int(f.readline())
    g = Digraph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)

    reachable = DirectedDFS(g, sys.argv[2:])

    for v in range(g.V):
        if reachable.marked(v):
            print(str(v) + " ")
