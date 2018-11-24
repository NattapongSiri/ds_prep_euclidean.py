from itertools import islice, tee
import json
from math import sqrt
import time

def _euc_dist(p1, p2):
    return sqrt(
        pow(p1[0] - p2[0], 2) +
        pow(p1[1] - p2[1], 2) +
        pow(p1[2] - p2[2], 2)
    )

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

start_time = time.perf_counter()
with open("data.txt", "r") as data_src:
    with open("processed.txt", "w") as data_sink:
        n = 5
        val = (_euc_dist(pair[0][i], pair[1][i]) for pair in pairwise((json.loads(line) for line in data_src)) for i in range(0, n))
        dist = []
        for v in val:
            dist.append(v)
            
            if len(dist) == 5:
                data_sink.write("%s\n" % dist)
                dist.clear()
                
print("Done in", time.perf_counter() - start_time, "s")
