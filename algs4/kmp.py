"""
 *  Execution:    python kmp.py pattern text
 *
 *  Reads in two strings, the pattern and the input text, and
 *  searches for the pattern in the input text using the
 *  KMP algorithm.
 *
 *  % python kmp.py abracadabra abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:               abracadabra
 *
 *  % python kmp.py rab abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:         rab
 *
 *  % python kmp.py bcara abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:                                   bcara
 *
 *  % python kmp.py rabrabracad abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern:                        rabrabracad
 *
 *  % python kmp.py abacad abacadabrabracabracadabrabrabracad
 *  text:    abacadabrabracabracadabrabrabracad
 *  pattern: abacad
 *
"""


class KMP:

    def __init__(self, pattern):
        self.pattern = pattern
        self.R = 256
        M = len(pattern)
        self.dfa = [[0 for x in range(M)] for y in range(self.R)]
        self.dfa[self.char_at(pattern, 0)][0] = 1
        X = 0
        for j in range(1, M):
            for c in range(self.R):
                self.dfa[c][j] = self.dfa[c][X]
            self.dfa[self.char_at(pattern, j)][j] = j + 1
            X = self.dfa[self.char_at(pattern, j)][X]

    def search(self, txt):
        N, M = len(txt), len(self.pattern)
        i, j = 0, 0
        while i < N and j < M:
            j = self.dfa[self.char_at(txt, i)][j]
            i += 1
        # Found (hit end of pattern)
            if j == M:
                return i - M
                # Not Found (hit end of text)
        return N

    def char_at(self, s, d):
        return ord(s[d])


if __name__ == "__main__":
    import sys
    pat, txt = sys.argv[1], sys.argv[2]
    kmp = KMP(pat)
    offset = kmp.search(txt)
    print("text:    " + txt)
    print("pattern: ", end="")
    for i in range(offset):
        print(" ", end="")
    print(pat)
