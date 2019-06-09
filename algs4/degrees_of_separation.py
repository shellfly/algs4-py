"""
      Execution:
        python degrees_of_separation.py filename delimiter source
      Data files:
        https:
            //algs4.cs.princeton.edu / 41graph / routes.txt
                    https:
        //algs4.cs.princeton.edu / 41graph / movies.txt
    
    
     % python degrees_of_separation.py routes.txt " " "JFK"
      LAS
         JFK
         ORD
         DEN
         LAS
      DFW
         JFK
         ORD
         DFW
      EWR
         Not in database.
    
     % python degrees_of_separation.py movies.txt "/" "Bacon, Kevin"
      Kidman, Nicole
         Bacon, Kevin
         Woodsman, The(2004)
         Grier, David Alan
         Bewitched(2005)
         Kidman, Nicole
      Grant, Cary
         Bacon, Kevin
         Planes, Trains & Automobiles(1987)
         Martin, Steve(I)
         Dead Men Don't Wear Plaid(1982)
         Grant, Cary
    
     % python degrees_of_separation.py movies.txt "/" "Animal House (1978)"
      Titanic(1997)
         Animal House(1978)
         Allen, Karen(I)
         Raiders of the Lost Ark(1981)
         Taylor, Rocky(I)
         Titanic(1997)
      To Catch a Thief(1955)
         Animal House(1978)
         Vernon, John(I)
         Topaz(1969)
         Hitchcock, Alfred(I)
         To Catch a Thief(1955)
    
"""
from algs4.symbol_graph import SymbolGraph
from algs4.breadth_first_paths import BreadthFirstPaths

if __name__ == "__main__":
    import sys
    filename, delimiter, source = sys.argv[1], sys.argv[2], sys.argv[3]
    sg = SymbolGraph(filename, delimiter)
    graph = sg.graph()

    if not sg.contains(source):
        print(source, " not in database.")
    else:
        s = sg.index(source)
        bfs = BreadthFirstPaths(graph, s)

        for line in sys.stdin:
            sink = line.strip()
            if sg.contains(sink):
                t = sg.index(sink)
                if bfs.has_path_to(t):
                    for v in bfs.path_to(t):
                        print(" ", sg.name(v))
                else:
                    print("not connected")
            else:
                print("input not contains source: ", source)
