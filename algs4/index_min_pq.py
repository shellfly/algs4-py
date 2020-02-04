class IndexMinPQ:

    def __init__(self, n):
        self.pq = []
        self.qp = [-1] * n
        self.keys = [None] * n

    def insert(self, i, item):
        self.pq.append(i)
        n = len(self.pq) - 1
        self.qp[i] = n
        self.keys[i] = item
        self.swim(n)

    def change(self, i, item):
        self.keys[i] = item
        self.sink(self.qp[i])
        self.swim(self.qp[i])

    def contains(self, index):
        return index in self.keys

    def delete(self, i):
        index = self.qp[i]
        item = self.pq[index]
        self.pq[index], self.pq[-1] = self.pq[-1], self.pq[index]
        self.swim(index)
        self.sink(index)
        self.keys[i] = None
        self.qp[i] = -1
        return item

    def decrease_key(self, i, key):
        if self.keys[i] <= key:
            raise Exception("calling decrease key with invalid value")
        self.keys[i] = key
        self.swim(self.qp[i])

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def min(self):
        return self.keys[self.pq[0]]

    def del_min(self):
        m = self.pq[0]
        self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
        self.pq = self.pq[:-1]
        self.sink(0)

        self.qp[m] = -1
        return m

    def is_empty(self, ):
        return not self.pq

    def size(self, ):
        return len(self.pq)

    def swim(self, k):
        while k > 0 and self.greater((k - 1) // 2, k):
            self.pq[k], self.pq[
                (k - 1) // 2] = self.pq[(k - 1) // 2], self.pq[k]
            k = (k - 1) // 2

    def sink(self, k):
        N = len(self.pq)

        while 2 * k + 1 <= N - 1:
            j = 2 * k + 1
            if j < N - 1 and self.greater(j, j + 1):
                j += 1

            if not self.greater(k, j):
                break

            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j
