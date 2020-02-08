class MinPQ:

    def __init__(self):
        self.pq = []

    def insert(self, v):
        self.pq.append(v)
        self.swim(len(self.pq) - 1)

    def min(self):
        return self.pq[0]

    def del_min(self, ):
        m = self.pq[0]
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        self.pq = self.pq[:-1]
        self.sink(0)
        return m

    def is_empty(self, ):
        return not self.pq

    def size(self, ):
        return len(self.pq)

    def swim(self, k):
        while k > 0 and self.pq[(k - 1) // 2] > self.pq[k]:
            self.pq[k], self.pq[
                (k - 1) // 2] = self.pq[(k - 1) // 2], self.pq[k]
            k = (k - 1) // 2

    def sink(self, k):
        N = len(self.pq)

        while 2 * k + 1 <= N - 1:
            j = 2 * k + 1
            if j < N - 1 and self.pq[j] > self.pq[j + 1]:
                j += 1

            if not self.pq[j] < self.pq[k]:
                break

            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j
