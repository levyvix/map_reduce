from pathos.multiprocessing import ProcessingPool as Pool

def print_and_return(x):
 print(x); return x


if __name__ == '__main__':
    with Pool(4) as p:
        p.map(print_and_return, range(100))