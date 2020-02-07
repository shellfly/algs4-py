"""
*  Execution:    python multiway.py
*  Data files:   https://algs4.cs.princeton.edu/24pq/m1.txt
*                https://algs4.cs.princeton.edu/24pq/m2.txt
*                https://algs4.cs.princeton.edu/24pq/m3.txt
*
*  Merges together the sorted input stream given as command-line arguments
*  into a single sorted output stream on standard output.
*
*  % more m1.txt
*  A B C F G I I Z
*
*  % more m2.txt
*  B D H P Q Q
*
*  % more m3.txt
*  A B E F J N
*
*  % python multiway.py m1.txt m2.txt m3.txt
*  A A B B B C D E F F G H I I J N P Q Q Z
*
"""

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
