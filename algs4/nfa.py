"""
 *  Execution:    python nfa.py regexp text
 *
 *  % python nfa.py "(A*B|AC)D" AAAABD
 *  true
 *
 *  % python nfa.py "(A*B|AC)D" AAAAC
 *  false
 *
 *  % python nfa.py "(a|(bc)*d)*" abcbcd
 *  true
 *
 *  % python nfa.py "(a|(bc)*d)*" abcbcbcdaaaabcbcdaaaddd
 *  true
 *
 *  Remarks
 *  -----------
 *  The following features are not supported:
 *    - The + operator
 *    - Multiway or
 *    - Metacharacters in the text
 *    - Character classes.
 *
"""

from algs4.bag import Bag
from algs4.digraph import Digraph
from algs4.directed_dfs import DirectedDFS
from algs4.stack import Stack


class NFA:
    def __init__(self, regexp):
        ops = Stack()
        M = len(regexp)
        G = Digraph(M+1)
        for i in range(M):
            lp = i
            if regexp[i] == "(" or regexp[i] == "|":
                ops.push(i)
            elif regexp[i] == ")":
                op = ops.pop()
                if regexp[op] == "|":
                    lp = ops.pop()
                    G.add_edge(lp, op+1)
                    G.add_edge(op, i)
                else:
                    lp = op
            if i < M-1 and regexp[i+1] == "*":
                G.add_edge(lp, i+1)
                G.add_edge(i+1, lp)
            if regexp[i] in ("(", "*", ")"):
                G.add_edge(i, i+1)
        self.M = M
        self.G = G
        self.re = regexp

    def recognizes(self, txt):
        pc = Bag()
        dfs = DirectedDFS(self.G, [0])
        for v in range(self.G.V):
            if dfs.marked(v):
                pc.add(v)
        for i in range(len(txt)):
            match = Bag()
            for v in pc:
                if v < self.M:
                    if self.re[v] == txt[i] or self.re[v] == ".":
                        match.add(v+1)
            pc = Bag()
            dfs = DirectedDFS(self.G, match)
            for v in range(self.G.V):
                if dfs.marked(v):
                    pc.add(v)
        for v in pc:
            if v == self.M:
                return True
        return False

    def char_at(self, s, d):
        return ord(s[d])


if __name__ == "__main__":
    import sys
    pattern, txt = sys.argv[1], sys.argv[2]
    nfa = NFA(pattern)
    print(nfa.recognizes(txt))
