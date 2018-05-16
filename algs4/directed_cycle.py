"""
  Execution:    python directed_cycle.py input.txt
  Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
                https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt

  Finds a directed cycle in a digraph.
  Runs in O(E + V) time.

  % python directed_cycle.py tinyDG.txt
  Directed cycle: 3 5 4 3

  %  python directed_cycle.py tinyDAG.txt
  No directed cycle

 """
from algs4.stack import Stack
from algs4.digraph import Digraph


class DirectedCycle:

    def __init__(self, G):
        self._marked = [False for _ in range(G.V)]
        self.edge_to = [False for _ in range(G.V)]
        self.on_stack = [False for _ in range(G.V)]
        self.cycle = None
        for v in range(G.V):
            if not self._marked[v]:
                self.dfs(G, v)

    def dfs(self, G, v):
        self._marked[v] = True
        self.on_stack[v] = True

        for w in G.adj[v]:
            if self.has_cycle():
                return
            if not self._marked[w]:
                self.edge_to[w] = v
                self.dfs(G, w)
            elif self.on_stack[w]:
                self.cycle = Stack()
                x = v
                while x != w:
                    self.cycle.push(x)
                    x = self.edge_to[x]
                self.cycle.push(w)
                self.cycle.push(v)
        self.on_stack[v] = False

    def marked(self, v):
        return self._marked[v]

    def has_cycle(self):
        return self.cycle is not None

if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    V = int(f.readline())
    E = int(f.readline())
    g = Digraph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)

    finder = DirectedCycle(g)
    if finder.has_cycle():
        for v in finder.cycle:
            print(v, end=" ")
    else:
        print("No directed cycle")
