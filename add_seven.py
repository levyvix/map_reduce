def add_seven(n):
    return n + 7


plus_seven = map(add_seven, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


for n in plus_seven:
    print(n)
