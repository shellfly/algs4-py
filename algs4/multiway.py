from algs4.index_min_pq import IndexMinPQ


class Multiway:

    @classmethod
    def merge(cls, streams):
        n = len(streams)
        pq = IndexMinPQ(n)
        for i in range(n):
            pq.insert(i, streams[i][0])
            streams[i] = streams[i][1:]

        while not pq.is_empty():
            print(pq.min())
            i = pq.del_min()
            if streams[i]:
                pq.insert(i, streams[i][0])
                streams[i] = streams[i][1:]

if __name__ == "__main__":
    import sys
    streams = []
    n = len(sys.argv)
    for i in range(1, n):
        streams.append(open(sys.argv[i]).readline().split())
    Multiway.merge(streams)
