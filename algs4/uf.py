class UF:

    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.sz = [1] * n

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    # quick-find
    # def find(self, p):
    #     return self.id[p]

    # def union(self, p, q):
    #     pId = self.find(p)
    #     qId = self.find(q)
    #     if pId == qId:
    #         return
    #     for index, i in enumerate(self.id):
    #         if i == pId:
    #             self.id[index] = qId
    #     self.count -= 1

    # quick-union
    # def find(self, p):
    #     while self.id[p] != p:
    #         p = self.id[p]
    #     return p

    # def union(self, p, q):
    #     pId = self.find(p)
    #     qId = self.find(q)
    #     if pId == qId:
    #         return
    #     self.id[pId] = qId
    #     self.count -= 1

    # weighted quick-union
    def find(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]]  # path compression
            p = self.id[p]
        return p

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        if self.sz[pId] < self.sz[qId]:
            self.id[pId] = qId
            self.sz[qId] += self.sz[pId]
        else:
            self.id[qId] = pId
            self.sz[pId] += self.sz[qId]
        self.count -= 1


if __name__ == '__main__':
    import sys

    n = int(sys.stdin.readline())
    uf = UF(n)
    for line in sys.stdin:
        p, q = [int(i) for i in line.split()]
        if (uf.connected(p, q)):
            continue
        else:
            uf.union(p, q)
            print("%s %s" % (p, q))
    print(uf.count, "components")
