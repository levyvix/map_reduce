from functools import reduce

import dill as pickle
from pathos.multiprocessing import ProcessingPool as Pool
from toolz.sandbox.parallel import fold


def add(left, right):
    return left + right


with Pool() as p:
    fold(add, range(500000), map=p.imap)

print(reduce(add, range(500)))
