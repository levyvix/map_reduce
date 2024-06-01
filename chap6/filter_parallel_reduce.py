from functools import reduce

import dill as pickle
from pathos.multiprocessing import ProcessingPool as Pool
from toolz.sandbox.parallel import fold


def map_combinations(left, right):
    return left + right


def keep_if_even(acc, nxt):
    if nxt % 2 == 0:
        return acc + [nxt]
    else:
        return acc


# with Pool() as p:
#    fold(keep_if_even, range(500000), [], map=p.imap, combine=map_combinations)

print(reduce(keep_if_even, range(500), []))
