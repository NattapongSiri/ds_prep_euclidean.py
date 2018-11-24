import ast
from itertools import islice, tee
import json
from math import sqrt
import time
from numba import float64, int32, jit

@jit(float64(int32, int32, int32, int32, int32, int32), nopython=True, cache=True)
def _euc_dist(x1, y1, z1, x2, y2, z2):
    return sqrt(
        pow(x1 - x2, 2) +
        pow(y1 - y2, 2) +
        pow(z1 - z2, 2)
    )

start_time = time.perf_counter()
with open("data.txt", "r", buffering=32*2**20) as data_src:
    with open("processed.txt", "w", buffering=32*2**20) as data_sink:
        n = 5
        records = []
        records.append(json.loads(next(data_src)))
        records.append(json.loads(next(data_src)))
        distance = [0 for i in range(0, n)]

        for line in data_src:
            for i in range(0, n):
                distance[i] = _euc_dist(records[0][i][0], records[0][i][1], records[0][i][2], records[1][i][0], records[1][i][1], records[1][i][2])
            data_sink.write("%s" % line)
            records[0] = records[1]
            records[1] = json.loads(line)
            
                
print("Done in", time.perf_counter() - start_time, "s")