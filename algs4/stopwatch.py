"""
 Execution:    python stopwatch.py n
 utility class to measure the running time (wall clock) of a program.
 
 % python stopwatch.py 10000000
2.108185e+10 3.60 seconds
2.108185e+10 4.53 seconds
 
 """
import time


class StopWatch:

    def __init__(self):
        self.start = time.time()

    def elapsed_time(self):
        return round(time.time() - self.start, 2)


if __name__ == '__main__':
    import sys
    import math

    n = int(sys.argv[1])
    timer1 = StopWatch()
    sum1 = 0.0
    for i in range(n):
        sum1 += math.sqrt(i)
    print("%e %.2f seconds" % (sum1, timer1.elapsed_time()))

    timer2 = StopWatch()
    sum2 = 0.0
    for i in range(n):
        sum2 += math.pow(i, 0.5)
    print("%e %.2f seconds" % (sum2, timer2.elapsed_time()))
