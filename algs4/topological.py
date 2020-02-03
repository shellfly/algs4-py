"""
 *  Execution:    python topological.py filename.txt delimiter
 *  Data files:   https://algs4.cs.princeton.edu/42digraph/jobs.txt
 *
 *  Compute topological ordering of a DAG or edge-weighted DAG.
 *  Runs in O(E + V) time.
 *
 *  % python topological.py jobs.txt "/"
 *  Calculus
 *  Linear Algebra
 *  Introduction to CS
 *  Advanced Programming
 *  Algorithms
 *  Theoretical CS
 *  Artificial Intelligence
 *  Robotics
 *  Machine Learning
 *  Neural Networks
 *  Databases
 *  Scientific Computing
 *  Computational Biology
 *
"""

from algs4.depth_first_order import DepthFirstOrder
from algs4.directed_cycle import DirectedCycle
from algs4.symbol_digraph import SymbolDigraph


class Topological:
    def __init__(self, g):
        self.order = None
        finder = DirectedCycle(g)
        if not finder.has_cycle():
            dfs = DepthFirstOrder(g)
            self.order = dfs.reversePost()

    def has_order(self):
        return self.order != None


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    delimiter = sys.argv[2]
    sg = SymbolDigraph(filename, delimiter)
    topological = Topological(sg.digraph())
    for v in topological.order:
        print(sg.name(v))
