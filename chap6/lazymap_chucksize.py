
from time import time
from multiprocessing import Pool

def times_two(x):
    return x*2+7

def parallel_map(xs, chunk=8500):
    
    with Pool(2) as p:
        x = p.map(times_two, xs, chunk)
    return x


print("""
{:<10} | {}
----------------------------""".format("chunksize", "runtime"))

for i in range(9):
    N = 1000000
    chunk_size = 5 * (10 ** i)
    
    
    t1 = time()
    parallel_map(range(N), chunk_size)
    pm_time = time() - t1
    
    
    
    print(""" {:>10} | {}""".format(chunk_size, pm_time))
    
    
