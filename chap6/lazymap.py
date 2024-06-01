from time import time
from multiprocessing import Pool

def times_two(x):
    return x*2

def lazy_map(xs):
    return list(map(times_two, xs))

def parallel_map(xs, chunk=8500):
    
    with Pool(2) as p:
        x = p.map(times_two, xs, chunk)
    return x



for i in range(0, 7):
    N = 10 ** i
    t1 = time()
    lazy_map(range(N))
    lm_time = time() - t1
    
    t1 = time()
    parallel_map(range(N))
    pm_time = time() - t1
    
    print(f"N = {N}")
    print(f"Lazy: {lm_time}, Parallel: {pm_time}")