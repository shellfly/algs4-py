class DepthFirstSearch:

    def __init__(self, g, s):
        self._marked = {}
        self.count = 0
        self.dfs(g, s)

    def dfs(self, g, v):
        self._maked[v] = True
        self.count += 1
        for w in g.adj[v]:
            if not self._marked[w]:
                self.dfs(g, w)

    def marked(self, w):
        return self._marked[w]

    def count(self):
        return self.count
