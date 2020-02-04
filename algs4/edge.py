class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return "%d-%s %.5f" % (self.v, self.w, self.weight)

    def __cmp__(self, other):
        if self.weihgt < other.weight:
            return -1
        elif self.weight > other.weight:
            return 1
        else:
            return 0

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v:
            return self.w
        elif v == self.w:
            return self.v
        else:
            raise Exception("invalid edge")
