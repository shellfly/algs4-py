"""
   Execution:  python nonrecursive_depth_first_paths.py G s

   Data files:   https://algs4.cs.princeton.edu/41graph/tinyCG.txt
                 https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt

   Run depth first search (non-recursive implementation) on an undirected graph.
   Runs in O(E + V) time.

   %  python graph.py tinyCG.txt
   6 8
   0: 2 1 5
   1: 0 2
   2: 0 1 3 4
   3: 5 4 2
   4: 3 2
   5: 3 0

   % python nonrecursive_depth_first_paths.py tinyCG.txt 0
   0 to 0:  0
   0 to 1:  0-2-1
   0 to 2:  0-2
   0 to 3:  0-2-3
   0 to 4:  0-2-3-4
   0 to 5:  0-2-3-5

"""
from algs4.stack import Stack
from algs4.graph import Graph


class NRDepthFirstPaths:

    def __init__(self, G, s):
        self.marked = [False for _ in range(G.V)]
        self.edge_to = [0 for _ in range(G.V)]
        self.s = s

        stack = Stack()
        stack.push(s)

        while not stack.is_empty():
            v = stack.peek()
            stack.pop()

            if not self.marked[v]:
                self.marked[v] = True

            for node in G.adj[v]:
                if not self.marked[node]:
                    self.edge_to[node] = v
                    stack.push(node)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return
        path = Stack()
        x = v
        while x != self.s:
            path.push(x)
            x = self.edge_to[x]
        path.push(s)
        return path


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
    dfs = NRDepthFirstPaths(g, s)
    for v in range(g.V):
        if dfs.has_path_to(v):
            print("%d to %d: " % (s, v), end='')
            for x in dfs.path_to(v):
                if x == s:
                    print(x, end='')
                else:
                    print('-%s' % x, end='')
            print()
        else:
            print("%d and %d: not connected" % (s, v))
