from pathos.multiprocessing import ProcessingPool as Pool


class FizzBuzzer:
    def __init__(self):
        self.n = 0

    def foo(self, _):
        self.n += 1
        if (self.n % 3) == 0:
            x = "buzz"
        else:
            x = "fizz"
        print(x)
        return x


FB = FizzBuzzer()

if __name__ == "__main__":
    with Pool(4) as p:
        p.map(FB.foo, range(100))
