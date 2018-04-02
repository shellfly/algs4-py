"""
  Execution:    python depth_first_search.py filename.txt s
  Data files:   https: // algs4.cs.princeton.edu / 41graph / tinyG.txt
                https: // algs4.cs.princeton.edu / 41graph / mediumG.txt

  Run depth first search on an undirected graph.
  Runs in O(E + V) time.

 % python depth_first_search tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python depth_frist_search tinyG.txt 9
  9 10 11 12
  NOT connected

 """
from algs4.graph import Graph


class DepthFirstSearch:

    def __init__(self, G, s):
        self._marked = [False for _ in range(G.V)]
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G, v):
        self._marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self._marked[w]:
                self.dfs(G, w)

    def marked(self, s):
        return self._marked[s]

if __name__ == '__main__':
    import sys
    print(sys.argv)
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    search = DepthFirstSearch(g, s)
    for v in range(g.V):
        if search.marked(v):
            print(str(v) + " ")
    if search.count == g.V:
        print("connected")
    else:
        print("not connected")
