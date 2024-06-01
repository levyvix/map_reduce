from functools import reduce
from random import choice
from time import time

import dill as pickle
from pathos.multiprocessing import ProcessingPool as Pool
from toolz.sandbox.parallel import fold


def combine_counts(a, b):
    unique_keys = set(a.keys()).union(set(b.keys()))
    return {k: a.get(k, 0) + b.get(k, 0) for k in unique_keys}


def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc


xs = (choice([1, 2, 3, 4, 5, 6]) for _ in range(500000))

tic = time()
with Pool() as p:
    a = fold(make_counts, xs, {}, map=p.imap, combine=combine_counts)
# rand_nums = (choice([1, 2, 3, 4, 5, 6]) for _ in range(500))
# print(reduce(make_counts, xs, {}))
tac = time() - tic

print(tac)

print(a)
