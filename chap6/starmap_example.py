from itertools import starmap

xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ys = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


loop_maxes = [max(ys[i], x) for i, x in enumerate(xs)]
map_maxes = list(starmap(max, zip(ys, xs)))

print(loop_maxes)

print(map_maxes)