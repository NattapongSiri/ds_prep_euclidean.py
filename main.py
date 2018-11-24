from itertools import islice, tee
import json
import time
import numpy as np

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

start_time = time.perf_counter()
np.set_printoptions(floatmode="maxprec", precision=15)

with open("data.txt", "r") as data_src:
    with open("processed.txt", "w") as data_sink:
        n = 5
        pair = pairwise((json.loads(line) for line in data_src))
        for records in pair:
            array = np.array(list(records), dtype=float)
            record_1 = array[ 0:1 , 0:5, : ]
            record_2 = array[ 1:2 , 0:5, : ]
            diff_sqr = (record_1 - record_2) ** 2
            sqr_sum = np.sum(diff_sqr, 2)
            dist = np.sqrt(sqr_sum).squeeze()
            data_sink.write("%s\n" % np.array2string(dist))
        
print("Done in", time.perf_counter() - start_time, "s")
