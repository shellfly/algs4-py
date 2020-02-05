class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        return "%d->%s %.5f" % (self.v, self.w, self.weight)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def From(self):
        return self.v

    def To(self):
        return self.w
