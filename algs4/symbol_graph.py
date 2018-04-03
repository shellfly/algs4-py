"""
   Execution:    python symbol_graph.py filename.txt delimiter
   Data files:   https://algs4.cs.princeton.edu/41graph/routes.txt
                 https://algs4.cs.princeton.edu/41graph/movies.txt
                 https://algs4.cs.princeton.edu/41graph/moviestiny.txt
                 https://algs4.cs.princeton.edu/41graph/moviesG.txt
                 https://algs4.cs.princeton.edu/41graph/moviestopGrossing.txt

   %  python symbol_graph.py routes.txt " "
   JFK
      MCO
      ATL
      ORD
   LAX
      PHX
      LAS

   % python symbol_graph.py movies.txt "/"
   Tin Men (1987)
      Hershey, Barbara
      Geppi, Cindy
      Jones, Kathy (II)
      Herr, Marcia
      ...
      Blumenfeld, Alan
      DeBoy, David
   Bacon, Kevin
      Woodsman, The (2004)
      Wild Things (1998)
      Where the Truth Lies (2005)
      Tremors (1990)
      ...
      Apollo 13 (1995)
      Animal House (1978)


   Assumes that input file is encoded using UTF-8.
   % iconv -f ISO-8859-1 -t UTF-8 movies-iso8859.txt > movies.txt

 """

from algs4.st import ST
from algs4.graph import Graph


class SymbolGraph:

    def __init__(self, stream, sp):
        self.st = ST()

        for line in open(stream):
            a = line.strip().split(sp)
            for i in range(len(a)):
                if not self.st.contains(a[i]):
                    self.st.put(a[i], self.st.size())

        self.keys = ["" for _ in range(self.st.size())]
        for key in self.st.keys():
            self.keys[self.st.get(key)] = key

        self.G = Graph(self.st.size())
        for line in open(stream):
            a = line.strip().split(sp)
            v = self.st.get(a[0])
            for i in range(1, len(a)):
                self.G.add_edge(v, self.st.get(a[i]))

    def contains(self, s):
        return self.st.contains(s)

    def index(self, s):
        return self.st.get(s)

    def name(self, v):
        return self.keys[v]

    def graph(self):
        return self.G

if __name__ == "__main__":
    import sys
    filename, delimiter = sys.argv[1], sys.argv[2]
    sg = SymbolGraph(filename, delimiter)
    graph = sg.graph()

    for line in sys.stdin:
        source = line.strip()
        if sg.contains(source):
            s = sg.index(source)
            for v in graph.adj[s]:
                print("  ", sg.name(v), end='')
        else:
            print("input not contains source: ", source)
