"""
  Execution:    python nonrecursive_depth_first_search.py filename.txt s
  Data files:   https: // algs4.cs.princeton.edu / 41graph / tinyG.txt
                https: // algs4.cs.princeton.edu / 41graph / mediumG.txt

  Run nonrecurisve depth-first search on an undirected graph.
  Runs in O(E + V) time using O(V) extra space.

 % python nonrecursive_depth_first_search.py tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python nonrecursive_depth_first_search.py tinyG.txt 9
  9 10 11 12
  NOT connected

 """

from algs4.graph import Graph
from algs4.stack import Stack


class NRDepthFirstSearch:

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.count = 0

        stack = Stack()
        stack.push(s)

        while not stack.is_empty():
            v = stack.peek()
            stack.pop()

            if not self.marked[v]:
                self.marked[v] = True
                self.count += 1

            for node in G.adj[v]:
                if not self.marked[node]:
                    stack.push(node)


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    s = int(sys.argv[2])
    V = int(f.readline())
    E = int(f.readline())
    g = Graph(V)
    for i in range(E):
        v, w = f.readline().split()
        g.add_edge(v, w)
    search = NRDepthFirstSearch(g, s)
    for v in range(g.V):
        if search.marked[v]:
            print(str(v) + " ")
    if search.count == g.V:
        print("connected")
    else:
        print("not connected")
